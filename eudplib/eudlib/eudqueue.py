#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2022 Armoha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from .. import core as c
from ..core import Add, EUDVArray, Memory, SetMemory
from ..core.eudfunc.eudf import _EUDPredefineParam
from ..ctrlstru import EUDSetContinuePoint, EUDWhile
from ..ctrlstru.loopblock import _UnsafeWhileNot
from ..utils import EPD, cachedfunc, ep_assert


@cachedfunc
def EUDQueue(capacity):
    """A single-ended queue implemented with a fixed-size variable array."""
    ep_assert(isinstance(capacity, int) and capacity > 0)

    class _EUDQueue:
        def __init__(self):
            ret = c.EUDVariable()
            pop = c.EUDVariable(ret, c.SetTo, 0)
            queue = EUDVArray(capacity)(dest=EPD(pop.getValueAddr()), nextptr=pop.GetVTable())
            append_act = SetMemory(queue + 348, c.SetTo, 0)
            jump = c.Forward()
            self._length = c.EUDVariable(0)

            c.PushTriggerScope()
            iter_start, iter_jump = c.Forward(), c.Forward()
            iter_init = c.RawTrigger(
                actions=[
                    SetMemory(iter_start + 16, c.SetTo, EPD(queue) + 87),
                    c.SetNextPtr(iter_jump, queue - 72),
                    c.SetNextPtr(iter_start, iter_jump),
                    c.SetMemoryX(iter_start + 2376, c.SetTo, 1, 1),
                ],
            )
            c.RawTrigger(
                conditions=self._length.AtLeast(1),
                actions=c.SetMemoryX(iter_start + 2404, c.SetTo, 1 << 24, 255 << 24),
            )
            iter_start << c.RawTrigger(
                nextptr=0,  # by iter_init
                conditions=Memory(append_act + 16, c.Exactly, 0),  # by iter_init, iter_contpoint
                actions=c.SetNextPtr(iter_start, 0),  # end by __iter__ call
            )
            iter_jump << c.RawTrigger(
                nextptr=0,  # by iter_init, iter_contpoint
                actions=[
                    c.SetNextPtr(pop.GetVTable(), 0),  # yield_point by __iter__ call
                    SetMemory(iter_start + 16, Add, 18),
                    SetMemory(iter_jump + 4, Add, 72),
                    c.SetMemoryX(iter_start + 2376, c.SetTo, 0, 1),
                ],
            )
            iter_contpoint = c.RawTrigger(
                nextptr=iter_start,
                conditions=Memory(iter_start + 16, c.AtLeast, EPD(queue) + 87 + 18 * capacity),
                actions=[
                    SetMemory(iter_start + 16, Add, -(18 * capacity)),
                    SetMemory(iter_jump + 4, Add, -(72 * capacity)),
                ],
            )
            c.PopTriggerScope()

            def iter():
                yield_point, end = c.Forward(), c.Forward()
                c.RawTrigger(
                    nextptr=iter_init,
                    actions=[
                        SetMemory(iter_start + 348, c.SetTo, end),
                        SetMemory(iter_jump + 348, c.SetTo, yield_point),
                    ],
                )
                yield_point << c.NextTrigger()
                yield ret
                c.SetNextTrigger(iter_contpoint)
                end << c.NextTrigger()

            @_EUDPredefineParam((EPD(append_act) + 5,))
            @c.EUDFunc
            def append(value):
                check_wrap, wrap_tail, wrap_head = c.Forward(), c.Forward(), c.Forward()
                c.RawTrigger(
                    actions=[
                        append_act,
                        SetMemory(append_act + 16, Add, 18),
                        self._length.AddNumber(1),
                    ],
                )
                check_wrap << c.RawTrigger(
                    nextptr=wrap_head,
                    conditions=self._length.AtLeast(capacity + 1),
                    actions=[
                        c.SetNextPtr(check_wrap, wrap_tail),
                        SetMemory(jump + 4, Add, 72),
                        SetMemory(iter_init + 348, Add, 18),
                        SetMemory(iter_init + 380, Add, 72),
                        self._length.SubtractNumber(1),
                    ],
                )
                wrap_tail << c.RawTrigger(
                    conditions=Memory(jump + 4, c.AtLeast, queue + 72 * (capacity - 1)),
                    actions=[
                        c.SetNextPtr(check_wrap, wrap_head),
                        SetMemory(jump + 4, Add, -(72 * capacity)),
                        SetMemory(iter_init + 348, Add, -(18 * capacity)),
                        SetMemory(iter_init + 380, Add, -(72 * capacity)),
                    ],
                )
                wrap_head << c.RawTrigger(
                    conditions=Memory(append_act + 16, c.AtLeast, EPD(queue) + 87 + 18 * capacity),
                    actions=SetMemory(append_act + 16, Add, -(18 * capacity)),
                )

            @c.EUDFunc
            def popleft():
                # ret = queue[tail]
                # tail %+ 1
                # return ret
                nonlocal jump
                wraparound = c.Forward()
                jump << c.RawTrigger(
                    nextptr=queue - 72,
                    actions=[
                        c.SetNextPtr(pop.GetVTable(), wraparound),
                        SetMemory(jump + 4, Add, 72),
                        SetMemory(iter_init + 348, Add, 18),
                        SetMemory(iter_init + 380, Add, 72),
                        self._length.SubtractNumber(1),
                    ],
                )
                wraparound << c.RawTrigger(
                    conditions=Memory(jump + 4, c.AtLeast, queue + 72 * (capacity - 1)),
                    actions=[
                        SetMemory(jump + 4, Add, -(72 * capacity)),
                        SetMemory(iter_init + 348, Add, -(18 * capacity)),
                        SetMemory(iter_init + 380, Add, -(72 * capacity)),
                    ],
                )
                return ret

            self._append = append
            self._popleft = popleft
            self._iter = iter

            c.PushTriggerScope()
            append(0)  # prevent 'Cannot evaluate <ConstExpr>...' error
            popleft()  # by always instantiate triggers
            c.PopTriggerScope()

        def __iter__(self):
            return self._iter()

        def append(self, value, **kwargs):
            self._append(value, **kwargs)

        def popleft(self, **kwargs):
            return self._popleft(**kwargs)

        def empty(self):
            return self._length == 0

        @property  # FIXME: eudplib code can mutate length
        def length(self):
            return self._length

        def eqattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length == k
            raise AttributeError

        def neattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length != k
            raise AttributeError

        def leattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length <= k
            raise AttributeError

        def ltattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length < k
            raise AttributeError

        def geattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length >= k
            raise AttributeError

        def gtattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length > k
            raise AttributeError

    return _EUDQueue


@cachedfunc
def EUDDeque(capacity):
    """A double-ended queue implemented with a fixed-size variable array."""
    ep_assert(isinstance(capacity, int) and capacity > 0)

    class _EUDDeque:
        def __init__(self):
            ret = c.EUDVariable()
            pop = c.EUDVariable(ret, c.SetTo, 0)
            deque = EUDVArray(capacity)(dest=EPD(pop.getValueAddr()), nextptr=pop.GetVTable())
            append_act = SetMemory(deque + 348, c.SetTo, 0)
            appendleft_act = SetMemory(deque + 348, c.SetTo, 0)
            jump, jumpleft = c.Forward(), c.Forward()
            self._length = c.EUDVariable(0)

            c.PushTriggerScope()
            iter_start, iter_jump = c.Forward(), c.Forward()
            iter_init = c.RawTrigger(
                actions=[
                    SetMemory(iter_start + 16, c.SetTo, EPD(deque) + 87),
                    c.SetNextPtr(iter_jump, deque - 72),
                    c.SetNextPtr(iter_start, iter_jump),
                    c.SetMemoryX(iter_start + 2376, c.SetTo, 1, 1),
                ],
            )
            c.RawTrigger(
                conditions=self._length.AtLeast(1),
                actions=c.SetMemoryX(iter_start + 2404, c.SetTo, 1 << 24, 255 << 24),
            )
            iter_start << c.RawTrigger(
                nextptr=0,  # by iter_init
                conditions=Memory(append_act + 16, c.Exactly, 0),  # by iter_init, iter_contpoint
                actions=c.SetNextPtr(iter_start, 0),  # end by __iter__ call
            )
            iter_jump << c.RawTrigger(
                nextptr=0,  # by iter_init, iter_contpoint
                actions=[
                    c.SetNextPtr(pop.GetVTable(), 0),  # yield_point by __iter__ call
                    SetMemory(iter_start + 16, Add, 18),
                    SetMemory(iter_jump + 4, Add, 72),
                    c.SetMemoryX(iter_start + 2376, c.SetTo, 0, 1),
                ],
            )
            iter_contpoint = c.RawTrigger(
                nextptr=iter_start,
                conditions=Memory(iter_start + 16, c.AtLeast, EPD(deque) + 87 + 18 * capacity),
                actions=[
                    SetMemory(iter_start + 16, Add, -(18 * capacity)),
                    SetMemory(iter_jump + 4, Add, -(72 * capacity)),
                ],
            )
            c.PopTriggerScope()

            def iter():
                yield_point, end = c.Forward(), c.Forward()
                c.RawTrigger(
                    nextptr=iter_init,
                    actions=[
                        SetMemory(iter_start + 348, c.SetTo, end),
                        SetMemory(iter_jump + 348, c.SetTo, yield_point),
                    ],
                )
                yield_point << c.NextTrigger()
                yield ret
                c.SetNextTrigger(iter_contpoint)
                end << c.NextTrigger()

            @_EUDPredefineParam((EPD(append_act) + 5,))
            @c.EUDFunc
            def append(value):
                # deque[head] = value
                # head %+ 1
                check_wrap, wrap_tail, wrap_head = c.Forward(), c.Forward(), c.Forward()
                c.RawTrigger(
                    actions=[
                        append_act,
                        SetMemory(append_act + 16, Add, 18),
                        SetMemory(jump + 4, Add, 72),
                        self._length.AddNumber(1),
                    ],
                )
                check_wrap << c.RawTrigger(
                    nextptr=wrap_head,
                    conditions=self._length.AtLeast(capacity + 1),
                    actions=[
                        c.SetNextPtr(check_wrap, wrap_tail),
                        SetMemory(appendleft_act + 16, Add, 18),
                        SetMemory(jumpleft + 4, Add, 72),
                        SetMemory(iter_init + 348, Add, 18),
                        SetMemory(iter_init + 380, Add, 72),
                        self._length.SubtractNumber(1),
                    ],
                )
                wrap_tail << c.RawTrigger(
                    conditions=Memory(jump + 4, c.AtLeast, deque + 72 * (capacity - 1)),
                    actions=[
                        c.SetNextPtr(check_wrap, wrap_head),
                        SetMemory(appendleft_act + 16, Add, -(18 * capacity)),
                        SetMemory(jumpleft + 4, Add, -(72 * capacity)),
                        SetMemory(iter_init + 348, Add, -(18 * capacity)),
                        SetMemory(iter_init + 380, Add, -(72 * capacity)),
                    ],
                )
                wrap_head << c.RawTrigger(
                    conditions=Memory(append_act + 16, c.AtLeast, EPD(deque) + 87 + 18 * capacity),
                    actions=[
                        SetMemory(append_act + 16, Add, -(18 * capacity)),
                        SetMemory(jump + 4, Add, -(72 * capacity)),
                    ],
                )

            @c.EUDFunc
            def _pop():
                # head %- 1
                # return deque[head]
                nonlocal jump
                retpoint = c.Forward()
                c.RawTrigger(
                    conditions=Memory(jump + 4, c.AtMost, deque),
                    actions=[
                        SetMemory(append_act + 16, Add, 18 * capacity),
                        SetMemory(jump + 4, Add, 72 * capacity),
                    ],
                )
                jump << c.RawTrigger(
                    nextptr=deque,
                    actions=[
                        c.SetNextPtr(pop.GetVTable(), retpoint),
                        SetMemory(append_act + 16, Add, -18),
                        SetMemory(jump + 4, Add, -72),
                        self._length.SubtractNumber(1),
                    ],
                )
                retpoint << c.NextTrigger()
                return ret

            @_EUDPredefineParam((EPD(appendleft_act) + 5,))
            @c.EUDFunc
            def appendleft(value):
                # tail %- 1
                # deque[tail] = value
                check_wrap, wrap_head, wrap_tail = c.Forward(), c.Forward(), c.Forward()
                check_wrap << c.RawTrigger(
                    nextptr=wrap_tail,
                    conditions=self._length.AtLeast(capacity),
                    actions=[
                        c.SetNextPtr(check_wrap, wrap_head),
                        SetMemory(append_act + 16, Add, -18),
                        SetMemory(jump + 4, Add, -72),
                        self._length.SubtractNumber(1),
                    ],
                )
                wrap_head << c.RawTrigger(
                    conditions=Memory(jump + 4, c.AtMost, deque),
                    actions=[
                        c.SetNextPtr(check_wrap, wrap_tail),
                        SetMemory(append_act + 16, Add, 18 * capacity),
                        SetMemory(jump + 4, Add, 72 * capacity),
                    ],
                )
                wrap_tail << c.RawTrigger(
                    conditions=Memory(appendleft_act + 16, c.AtMost, EPD(deque) + 87),
                    actions=[
                        SetMemory(appendleft_act + 16, Add, 18 * capacity),
                        SetMemory(jumpleft + 4, Add, 72 * capacity),
                        SetMemory(iter_init + 348, Add, 18 * capacity),
                        SetMemory(iter_init + 380, Add, 72 * capacity),
                    ],
                )
                c.RawTrigger(
                    actions=[
                        SetMemory(appendleft_act + 16, Add, -18),
                        SetMemory(jumpleft + 4, Add, -72),
                        appendleft_act,
                        self._length.AddNumber(1),
                    ],
                )

            @c.EUDFunc
            def popleft():
                # ret = deque[tail]
                # tail %+ 1
                # return ret
                nonlocal jumpleft
                wraparound = c.Forward()
                jumpleft << c.RawTrigger(
                    nextptr=deque - 72,
                    actions=[
                        c.SetNextPtr(pop.GetVTable(), wraparound),
                        SetMemory(appendleft_act + 16, Add, 18),
                        SetMemory(jumpleft + 4, Add, 72),
                        SetMemory(iter_init + 348, Add, 18),
                        SetMemory(iter_init + 380, Add, 72),
                        self._length.SubtractNumber(1),
                    ],
                )
                wraparound << c.RawTrigger(
                    conditions=Memory(jumpleft + 4, c.AtLeast, deque + 72 * (capacity - 1)),
                    actions=[
                        SetMemory(appendleft_act + 16, Add, -(18 * capacity)),
                        SetMemory(jumpleft + 4, Add, -(72 * capacity)),
                        SetMemory(iter_init + 348, Add, -(18 * capacity)),
                        SetMemory(iter_init + 380, Add, -(72 * capacity)),
                    ],
                )
                return ret

            self._append = append
            self._appendleft = appendleft
            self._pop = _pop
            self._popleft = popleft
            self._iter = iter

            c.PushTriggerScope()
            append(0)  # prevent 'Cannot evaluate <ConstExpr>...' error
            _pop()  # by always instantiate triggers
            appendleft(0)
            popleft()
            c.PopTriggerScope()

        def __iter__(self):
            return self._iter()

        def append(self, value, **kwargs):
            self._append(value, **kwargs)

        def pop(self, **kwargs):
            return self._pop(**kwargs)

        def appendleft(self, value, **kwargs):
            self._appendleft(value, **kwargs)

        def popleft(self, **kwargs):
            return self._popleft(**kwargs)

        def empty(self):
            return self._length == 0

        @property  # FIXME: eudplib code can mutate length
        def length(self):
            return self._length

        def eqattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length == k
            raise AttributeError

        def neattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length != k
            raise AttributeError

        def leattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length <= k
            raise AttributeError

        def ltattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length < k
            raise AttributeError

        def geattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length >= k
            raise AttributeError

        def gtattr(self, attr, k):
            if isinstance(attr, str) and attr == "length":
                return self._length > k
            raise AttributeError

    return _EUDDeque
