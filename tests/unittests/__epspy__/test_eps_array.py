## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *
from eudplib.epscript.helper import _RELIMP, _IGVA, _CGFW, _ARR, _VARR, _SRET, _SV, _ATTW, _ARRW, _ARRC, _L2V, _LVAR, _LSH
# (Line 1) import py_random;
import random
# (Line 2) import tests.unittests.test_eps_randhelper as helper;
from tests.unittests import test_eps_randhelper as helper
# (Line 3) function test_write() {
@EUDFunc
def f_test_write():
    # (Line 4) const ret = py_list();
    ret = list()
    # (Line 6) const num = helper.GetValues();
    num = helper.GetValues()
    # (Line 7) const numV = EUDArray(helper.GetValues());
    numV = EUDArray(helper.GetValues())
    # (Line 8) const numS = num, numV;
    numS = num, numV
    # (Line 9) foreach(vals : numS) {
    for vals in numS:
        # (Line 10) var expect;
        expect = EUDVariable()
        # (Line 11) expect = vals[0];
        expect << (vals[0])
        # (Line 12) expect += vals[1];
        expect.__iadd__(vals[1])
        # (Line 13) expect -= vals[2];
        expect.__isub__(vals[2])
        # (Line 14) expect *= vals[3];
        expect.__imul__(vals[3])
        # (Line 15) expect /= vals[4];
        expect.__ifloordiv__(vals[4])
        # (Line 16) expect %= vals[5];
        expect.__imod__(vals[5])
        # (Line 17) expect <<= vals[6];
        expect.__ilshift__(vals[6])
        # (Line 18) expect >>= vals[7];
        expect.__irshift__(vals[7])
        # (Line 20) expect &= vals[8];
        expect.__iand__(vals[8])
        # (Line 21) expect |= vals[9];
        expect.__ior__(vals[9])
        # (Line 22) expect ^= vals[10];
        expect.__ixor__(vals[10])
        # (Line 23) ret.append(expect);
        ret.append(expect)
        # (Line 24) }
        # (Line 25) const pvar, arr = PVariable(), EUDArray(8);

    pvar, arr = List2Assignable([PVariable(), EUDArray(8)])
    # (Line 26) var v1, v2 = pvar, arr;
    v1, v2 = _LVAR([pvar, arr])
    # (Line 27) const pvarV, arrV = PVariable.cast(v1), EUDArray.cast(v2);
    pvarV, arrV = List2Assignable([PVariable.cast(v1), EUDArray.cast(v2)])
    # (Line 29) const index = py_eval("random.randint(0, 7)");
    index = eval("random.randint(0, 7)")
    # (Line 30) var indexV = index;
    indexV = _LVAR([index])
    # (Line 31) const testmap = py_list();
    testmap = list()
    # (Line 32) foreach(a : list(pvar, arr, pvarV, arrV)) {
    for a in FlattenList([pvar, arr, pvarV, arrV]):
        # (Line 33) foreach(i : list(index, indexV)) {
        for i in FlattenList([index, indexV]):
            # (Line 34) foreach(vlist : numS) {
            for vlist in numS:
                # (Line 35) const pair = a, i, vlist;
                pair = a, i, vlist
                # (Line 36) testmap.append(pair);
                testmap.append(pair)
                # (Line 37) }
                # (Line 38) }

            # (Line 39) }

        # (Line 40) foreach(arr, i, vals : testmap) {

    for arr_1, i, vals in testmap:
        # (Line 41) arr[i] = vals[0];
        _ARRW(arr_1, i) << (vals[0])
        # (Line 42) arr[i] += vals[1];
        _ARRW(arr_1, i).__iadd__(vals[1])
        # (Line 43) arr[i] -= vals[2];
        _ARRW(arr_1, i).__isub__(vals[2])
        # (Line 44) arr[i] *= vals[3];
        _ARRW(arr_1, i).__imul__(vals[3])
        # (Line 45) arr[i] /= vals[4];
        _ARRW(arr_1, i).__ifloordiv__(vals[4])
        # (Line 46) arr[i] %= vals[5];
        _ARRW(arr_1, i).__imod__(vals[5])
        # (Line 47) arr[i] <<= vals[6];
        _ARRW(arr_1, i).__ilshift__(vals[6])
        # (Line 48) arr[i] >>= vals[7];
        _ARRW(arr_1, i).__irshift__(vals[7])
        # (Line 50) arr[i] &= vals[8];
        _ARRW(arr_1, i).__iand__(vals[8])
        # (Line 51) arr[i] |= vals[9];
        _ARRW(arr_1, i).__ior__(vals[9])
        # (Line 52) arr[i] ^= vals[10];
        _ARRW(arr_1, i).__ixor__(vals[10])
        # (Line 53) ret.append(arr[i]);
        ret.append(arr_1[i])
        # (Line 54) }
        # (Line 56) return List2Assignable(ret);

    EUDReturn(List2Assignable(ret))
    # (Line 57) }
