from random import getrandbits
import sys
builtin_func={}
funcs={}
class ID(int):
    def __call__(self,*args,**kwargs):
        return funcs[self](*args,**kwargs)
for i in 'in inc out outc add sub mul div mod 0 1 2 3 4 5 6 7 8 9 a b c d e f if'.split():
    builtin_func[i]=ID(getrandbits(64))
def _0():return ID(0)
funcs[builtin_func["0"]]=_0
def _1():return ID(1)
funcs[builtin_func["1"]]=_1
def _2():return ID(2)
funcs[builtin_func["2"]]=_2
def _3():return ID(3)
funcs[builtin_func["3"]]=_3
def _4():return ID(4)
funcs[builtin_func["4"]]=_4
def _5():return ID(5)
funcs[builtin_func["5"]]=_5
def _6():return ID(6)
funcs[builtin_func["6"]]=_6
def _7():return ID(7)
funcs[builtin_func["7"]]=_7
def _8():return ID(8)
funcs[builtin_func["8"]]=_8
def _9():return ID(9)
funcs[builtin_func["9"]]=_9
def _0():return ID(0)
funcs[builtin_func["0"]]=_0
def _a():return ID(10)
funcs[builtin_func["a"]]=_a
def _b():return ID(11)
funcs[builtin_func["b"]]=_b
def _c():return ID(12)
funcs[builtin_func["c"]]=_c
def _d():return ID(13)
funcs[builtin_func["d"]]=_d
def _e():return ID(14)
funcs[builtin_func["e"]]=_e
def _f():return ID(15)
funcs[builtin_func["f"]]=_f
def _in():
    try:
        return ID(input())
    except:
        return ID(0)
funcs[builtin_func["in"]]=_in
def _inc():
    try:
        return ID(ord(sys.stdin.read(1)))
    except:
        return ID(0)
funcs[builtin_func["inc"]]=_inc
def _out(x):
    print(x)
    return x
funcs[builtin_func["out"]]=_out
def _outc(x):
    print(chr(x), end='')
    return x
funcs[builtin_func["outc"]]=_outc
funcs[builtin_func["add"]]=ID.__add__
funcs[builtin_func["mul"]]=ID.__mul__
funcs[builtin_func["div"]]=ID.__floordiv__
funcs[builtin_func["mod"]]=ID.__mod__
funcs[builtin_func["sub"]]=lambda x,y:ID(0 if x<y else x-y)
def _if(x,y,z,*args):
    if x:
        return y(*args)
    else:
        return z(*args)
funcs[builtin_func["if"]]=_if