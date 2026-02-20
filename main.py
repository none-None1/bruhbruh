from random import *
import re,sys
def bruh2py(code):
    lines=code.strip().split('\n')
    lines=[i.replace(' ','').replace('\t','')for i in lines]
    res='from bruhlib import *\nimport sys\nsys.setrecursionlimit(2147483647)\n'
    func_id_dicts={}
    for i in 'in inc out outc add sub mul div mod 0 1 2 3 4 5 6 7 8 9 a b c d e f if'.split():
        func_id_dicts[i]=f'builtin_func["{i}"]'
    pattern=re.compile(r'[^(:,)\s]+')
    def func(x):
        t=x.group()
        if t not in func_id_dicts:
            return t
        return f'ID({func_id_dicts[t]})'
    for i in lines:
        x,y=i.split(':')
        func_name=x.split('(')[0]
        func_id=getrandbits(64)
        func_id_dicts[func_name] = func_id
        replaced=re.sub(pattern,func,y)
        res+=f'def func_{func_id}({x.split("(")[-1]}:\n\treturn {replaced}\nfuncs[ID({func_id})]=func_{func_id}\n'
    if 'bruh' in func_id_dicts:
        res+=f'funcs[{func_id_dicts["bruh"]}]()'
    return res
oc=open(sys.argv[1]).read()
print('Original code:')
print(oc)
c=bruh2py(oc)
print('Translated code')
print(c)
input("Press enter to confirm run: ")
exec(c)