from itertools import permutations, combinations, combinations_with_replacement
# permutations
    # No repetition
    # R epetition

def fact(n): return 1 if n==0 else n*fact(n-1)
"""
for p in permutations(["a","b","c"], 2):
    print(p)
print("----------")
"""
def perm(lst):
    #if lst == []: yield []
    if len(lst) == 1: yield lst
    for i in range(len(lst)):
        for p in perm(lst[:i]+lst[i+1:]):
            yield [lst[i]]+p

#print(list(perm(["a","b","c"]))) # [['a','b','c'],['a','c','b'],['b','a','c'],[...]]

def permut(lst):
    if len(lst)==1: return [lst]
    r = []
    for perm in permut(lst[1:]):
        for i in range(len(perm)+1):
            r.append(perm[:i]+lst[0]+perm[i:])
    return r
#print(list(permut("abc"))) # ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

def lambdaPerm(B):
    if len(B)==1: return B
    r=[];list(map(lambda x: list(map(lambda y: r.append(x[:y]+B[0]+x[y:]), range(len(x)+1))), lambdaPerm(B[1:])));return r
"""
for i in lambdaPerm("ABCDEF"):
    print(i)
"""

def combs2(n, available, used):
    if len(used) == n:
        yield tuple(used)
    elif len(available) <= 0:
        pass
    else:
        for c in combs2(n, available[1:], used[:]+[available[0]]):
            yield c
        for c in combs2(n, available[1:], used[:]):
            yield c
s="ABCDEFGHIJKLMNO"
k=5
mycombs=[c for c in combs2(k,list(s),[])]
#mm=[x for x in combs2(k,list(s)[:-5],[])]
#print(mycombs, "\n",len(mycombs))

def filtr(stri, args):
    for i in args:
        stri = stri.replace(i,"")
    return stri

#print(len(mycombs))#*len(mm))
for i in mycombs:
    print(i,end="")
    s="ABCDEFGHIJKLMNO"
    k=5
    #h=list(map(lambda x: s.replace(x,''),i))
    h=filtr(s,i)
    #print("---------",h)
    mm=[c for c in combs2(k,list(h),[])] 
    for j in mm:
        print("  -->\t",j,end="")
        g=filtr(h,j)#list(map(lambda x: h.replace(x,''),j))
        moo=[tuple(g)]
        for k in moo:
            print("  -->\t",k)
#print(len(mycombs)+len(mm)+len(moo))
