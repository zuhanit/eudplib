# Copyright 2014 by trgk.
# All rights reserved.
# This file is part of EUD python library (eudplib),
# and is released under "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import weakref
from dataclasses import dataclass

from typing_extensions import Self

from .. import core as c
from .. import ctrlstru as cs
from .. import utils as ut
from ..core.variable import eudv as ev
from ..localize import _
from .eudarray import EUDArray


class _ObjPoolData(c.ConstExpr):
    def __new__(cls, *args, **kwargs) -> Self:
        return super().__new__(cls, None)

    def __init__(self, size: int, max_fieldn: int = 8) -> None:
        super().__init__()
        self._vdict: weakref.WeakKeyDictionary = weakref.WeakKeyDictionary()
        self.size = size
        self.max_fieldn = max_fieldn

    def Evaluate(self):  # noqa: N802
        evb = ev.get_current_varbuffer()
        try:
            return evb._vdict[self].Evaluate()
        except KeyError:
            ret = evb.create_vartriggers(self, [0] * (self.max_fieldn * self.size))
            return ret.Evaluate()


class ObjPool:
    def __init__(self, size: int, max_fieldn: int = 8) -> None:
        self.size = size
        self.max_fieldn = max_fieldn
        self.remaining = c.EUDVariable(size)

        self.baseobj = _ObjPoolData(size, max_fieldn)
        self.data = EUDArray([72 * max_fieldn * i for i in range(size)])

    def full(self) -> c.Condition:
        return self.remaining == 0

    @c.EUDMethod
    def _alloc(self):
        """Allocate one object from pool"""
        if cs.EUDIf()(self.full()):
            c.EUDReturn(0)
        cs.EUDEndIf()

        self.remaining -= 1
        data = self.data[self.remaining]
        return data + self.baseobj

    def alloc(self, basetype, *args, **kwargs):
        ut.ep_assert(
            len(basetype._fielddict) <= self.max_fieldn,
            _("Only structs less than {} fields can be allocated").format(
                self.max_fieldn
            ),
        )
        data = self._alloc()
        data = basetype.cast(data)
        data.constructor(*args, **kwargs)
        return data

    def free(self, basetype, data) -> None:
        ut.ep_assert(
            len(basetype._fielddict) <= self.max_fieldn,
            _("Only structs less than {} fields can be allocated").format(
                self.max_fieldn
            ),
        )

        data = basetype.cast(data)
        data.destructor()
        self.data[self.remaining] = data - self.baseobj
        self.remaining += 1


@dataclass
class _GlobalObjPool:
    pool: ObjPool | None
    max_fieldn: int = 8
    max_object_num: int = 32768


_global_pool = _GlobalObjPool(pool=None, max_fieldn=8, max_object_num=32768)


def SetGlobalPoolFieldN(fieldn: int) -> None:  # noqa: N802
    global _global_pool
    ut.ep_assert(
        _global_pool.pool is None, "Global object pool is already initialized."
    )
    _global_pool.max_fieldn = fieldn


def get_global_pool() -> ObjPool:
    global _global_pool
    if _global_pool.pool is None:
        size, max_fieldn = _global_pool.max_object_num, _global_pool.max_fieldn
        _global_pool.pool = ObjPool(size, max_fieldn)
    return _global_pool.pool
