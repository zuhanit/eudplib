## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *
from eudplib.epscript.helper import _RELIMP, _IGVA, _CGFW, _ARR, _VARR, _SRET, _SV, _ATTW, _ARRW, _ARRC, _L2V, _LVAR, _LSH
# (Line 1) import py_random;
import random
# (Line 2) import py_itertools;
import itertools
# (Line 3) function test_write() {
@EUDFunc
def f_test_write():
    # (Line 4) const ret = py_list();
    ret = list()
    # (Line 6) const u32 = py_eval("lambda: random.randint(1, 0xFFFFFFFF)");
    u32 = eval("lambda: random.randint(1, 0xFFFFFFFF)")
    # (Line 7) const shift = py_eval("lambda: random.randint(0, 31)");
    shift = eval("lambda: random.randint(0, 31)")
    # (Line 9) const num = u32(), u32(), u32(), u32(), u32(), u32(),
    # (Line 10) shift(), shift(), u32(), u32(), u32();
    num = u32(), u32(), u32(), u32(), u32(), u32(), shift(), shift(), u32(), u32(), u32()
    # (Line 11) const numV = EUDArray(num);
    numV = EUDArray(num)
    # (Line 12) const numS = num, numV;
    numS = num, numV
    # (Line 13) setcurpl(getuserplayerid());
    f_setcurpl(f_getuserplayerid())
    # (Line 14) const dbg = StringBuffer(3000);
    dbg = StringBuffer(3000)
    # (Line 15) dbg.insert(0);
    dbg.insert(0)
    # (Line 16) foreach(vals : numS) {
    for vals in numS:
        # (Line 17) var expect = vals[0];
        expect = _LVAR([vals[0]])
        # (Line 18) expect += vals[1];
        expect.__iadd__(vals[1])
        # (Line 19) expect -= vals[2];
        expect.__isub__(vals[2])
        # (Line 20) dbg.appendf("\n\x07{:x}\x02 *= {:x}", expect, vals[3]);
        dbg.appendf("\n\x07{:x}\x02 *= {:x}", expect, vals[3])
        # (Line 21) expect *= vals[3];
        expect.__imul__(vals[3])
        # (Line 22) var temp = expect;
        temp = _LVAR([expect])
        # (Line 23) dbg.appendf(" -> \x07{:x}\x02 /= {:x}", expect, vals[4]);
        dbg.appendf(" -> \x07{:x}\x02 /= {:x}", expect, vals[4])
        # (Line 24) expect /= vals[4];
        expect.__ifloordiv__(vals[4])
        # (Line 25) temp += expect;
        temp.__iadd__(expect)
        # (Line 26) dbg.appendf(" -> \x07{}\x02 %= {:x}", expect, vals[5]);
        dbg.appendf(" -> \x07{}\x02 %= {:x}", expect, vals[5])
        # (Line 27) expect %= vals[5];
        expect.__imod__(vals[5])
        # (Line 28) temp += expect;
        temp.__iadd__(expect)
        # (Line 29) dbg.appendf(" -> \x07{}\x02 <<= {}", expect, vals[6]);
        dbg.appendf(" -> \x07{}\x02 <<= {}", expect, vals[6])
        # (Line 30) expect <<= vals[6];
        expect.__ilshift__(vals[6])
        # (Line 31) temp += expect;
        temp.__iadd__(expect)
        # (Line 32) dbg.appendf(" -> \x07{:x}\x02 >>= {}", expect, vals[7]);
        dbg.appendf(" -> \x07{:x}\x02 >>= {}", expect, vals[7])
        # (Line 33) expect >>= vals[7];
        expect.__irshift__(vals[7])
        # (Line 34) temp += expect;
        temp.__iadd__(expect)
        # (Line 37) dbg.appendf(" -> \x07{}\x02 &= {:x}", expect, vals[8]);
        dbg.appendf(" -> \x07{}\x02 &= {:x}", expect, vals[8])
        # (Line 38) expect &= vals[8];
        expect.__iand__(vals[8])
        # (Line 39) temp += expect;
        temp.__iadd__(expect)
        # (Line 40) dbg.appendf(" -> \x07{}\x02 |= {:x}", expect, vals[9]);
        dbg.appendf(" -> \x07{}\x02 |= {:x}", expect, vals[9])
        # (Line 41) expect |= vals[9];
        expect.__ior__(vals[9])
        # (Line 42) temp += expect;
        temp.__iadd__(expect)
        # (Line 43) dbg.appendf(" -> \x07{:x}", expect);
        dbg.appendf(" -> \x07{:x}", expect)
        # (Line 44) expect ^= vals[10];
        expect.__ixor__(vals[10])
        # (Line 45) temp += expect;
        temp.__iadd__(expect)
        # (Line 46) ret.append(temp);
        ret.append(temp)
        # (Line 47) }
        # (Line 48) const pvar, arr = PVariable(), EUDArray(8);

    pvar, arr = List2Assignable([PVariable(), EUDArray(8)])
    # (Line 49) var v1, v2 = pvar, arr;
    v1, v2 = _LVAR([pvar, arr])
    # (Line 50) const pvarV, arrV = PVariable.cast(v1), EUDArray.cast(v2);
    pvarV, arrV = List2Assignable([PVariable.cast(v1), EUDArray.cast(v2)])
    # (Line 52) const index = py_eval("random.randint(0, 7)");
    index = eval("random.randint(0, 7)")
    # (Line 53) var indexV = index;
    indexV = _LVAR([index])
    # (Line 55) foreach(arr, i, vals : py_eval("itertools.product(\
    # (Line 57) )")) {
    for arr_1, i, vals in eval("itertools.product(        (pvar, arr, pvarV, arrV), (index, indexV), (num, numV)    )"):
        # (Line 58) arr[i] = vals[0];
        _ARRW(arr_1, i) << (vals[0])
        # (Line 59) arr[i] += vals[1];
        _ARRW(arr_1, i).__iadd__(vals[1])
        # (Line 60) arr[i] -= vals[2];
        _ARRW(arr_1, i).__isub__(vals[2])
        # (Line 61) arr[i] *= vals[3];
        _ARRW(arr_1, i).__imul__(vals[3])
        # (Line 62) var temp = arr[i];
        temp = _LVAR([arr_1[i]])
        # (Line 63) arr[i] /= vals[4];
        _ARRW(arr_1, i).__ifloordiv__(vals[4])
        # (Line 64) temp += arr[i];
        temp.__iadd__(arr_1[i])
        # (Line 65) arr[i] %= vals[5];
        _ARRW(arr_1, i).__imod__(vals[5])
        # (Line 66) temp += arr[i];
        temp.__iadd__(arr_1[i])
        # (Line 67) arr[i] <<= vals[6];
        _ARRW(arr_1, i).__ilshift__(vals[6])
        # (Line 68) temp += arr[i];
        temp.__iadd__(arr_1[i])
        # (Line 69) arr[i] >>= vals[7];
        _ARRW(arr_1, i).__irshift__(vals[7])
        # (Line 70) temp += arr[i];
        temp.__iadd__(arr_1[i])
        # (Line 73) arr[i] &= vals[8];
        _ARRW(arr_1, i).__iand__(vals[8])
        # (Line 74) temp += arr[i];
        temp.__iadd__(arr_1[i])
        # (Line 75) arr[i] |= vals[9];
        _ARRW(arr_1, i).__ior__(vals[9])
        # (Line 76) temp += arr[i];
        temp.__iadd__(arr_1[i])
        # (Line 77) arr[i] ^= vals[10];
        _ARRW(arr_1, i).__ixor__(vals[10])
        # (Line 78) temp += arr[i];
        temp.__iadd__(arr_1[i])
        # (Line 79) ret.append(temp);
        ret.append(temp)
        # (Line 80) }
        # (Line 81) dbg.Display();

    dbg.Display()
    # (Line 83) return List2Assignable(ret);
    EUDReturn(List2Assignable(ret))
    # (Line 84) }
    # (Line 85) function test_compare() {

@EUDFunc
def f_test_compare():
    # (Line 86) const ret = py_list();
    ret = list()
    # (Line 87) const u32 = py_eval("lambda: random.randint(1, 0xFFFFFFFF)");
    u32 = eval("lambda: random.randint(1, 0xFFFFFFFF)")
    # (Line 89) const num = u32(), u32(), u32(), u32(), u32(), u32(), u32();
    num = u32(), u32(), u32(), u32(), u32(), u32(), u32()
    # (Line 90) const numV = EUDArray(num);
    numV = EUDArray(num)
    # (Line 92) const pvar, arr = PVariable(), EUDArray(8);
    pvar, arr = List2Assignable([PVariable(), EUDArray(8)])
    # (Line 93) var v1, v2 = pvar, arr;
    v1, v2 = _LVAR([pvar, arr])
    # (Line 94) const pvarV, arrV = PVariable.cast(v1), EUDArray.cast(v2);
    pvarV, arrV = List2Assignable([PVariable.cast(v1), EUDArray.cast(v2)])
    # (Line 96) const index = py_eval("random.randint(0, 7)");
    index = eval("random.randint(0, 7)")
    # (Line 97) var indexV = index;
    indexV = _LVAR([index])
    # (Line 99) foreach(arr, i, vals : py_eval("itertools.product(\
    # (Line 101) )")) {
    for arr_1, i, vals in eval("itertools.product(        (pvar, arr, pvarV, arrV), (index, indexV), (num, numV)    )"):
        # (Line 102) var temp = 0;
        temp = _LVAR([0])
        # (Line 103) arr[i] = vals[0];
        _ARRW(arr_1, i) << (vals[0])
        # (Line 104) if (arr[i] == vals[1]) temp += 1 << 1;
        if EUDIf()(_ARRC(arr_1, i) == vals[1]):
            temp.__iadd__(_LSH(1,1))
            # (Line 105) if (arr[i] != vals[2]) temp += 1 << 2;
        EUDEndIf()
        if EUDIf()(_ARRC(arr_1, i) == vals[2], neg=True):
            temp.__iadd__(_LSH(1,2))
            # (Line 106) if (arr[i] >= vals[3]) temp += 1 << 3;
        EUDEndIf()
        if EUDIf()(_ARRC(arr_1, i) >= vals[3]):
            temp.__iadd__(_LSH(1,3))
            # (Line 107) if (arr[i] <= vals[4]) temp += 1 << 4;
        EUDEndIf()
        if EUDIf()(_ARRC(arr_1, i) <= vals[4]):
            temp.__iadd__(_LSH(1,4))
            # (Line 108) if (arr[i] > vals[5]) temp += 1 << 5;
        EUDEndIf()
        if EUDIf()(_ARRC(arr_1, i) <= vals[5], neg=True):
            temp.__iadd__(_LSH(1,5))
            # (Line 109) if (arr[i] < vals[6]) temp += 1 << 6;
        EUDEndIf()
        if EUDIf()(_ARRC(arr_1, i) >= vals[6], neg=True):
            temp.__iadd__(_LSH(1,6))
            # (Line 110) ret.append(temp);
        EUDEndIf()
        ret.append(temp)
        # (Line 111) }
        # (Line 113) return List2Assignable(ret);

    EUDReturn(List2Assignable(ret))
    # (Line 114) }