from itertools import permutations, combinations, combinations_with_replacement
# permutations
# No repetition
# R epetition


def fact(n): return 1 if n == 0 else n * fact(n - 1)


def factorial(n): yield 1 if n == 0 else n * list(factorial(n - 1))[-1]

"""
for p in permutations(["a","b","c"], 2):
    print(p)
print("----------")
"""


def perm(lst):
    # if lst == []: yield []
    if len(lst) == 1:
        yield lst
    for i in range(len(lst)):
        for p in perm(lst[:i] + lst[i + 1:]):
            yield [lst[i]] + p

# print(list(perm(["a","b","c"]))) # [['a','b','c'],['a','c','b'],['b','a','c'],[...]]


def permut(lst):
    if len(lst) == 1:
        return [lst]
    r = []
    for perm in permut(lst[1:]):
        for i in range(len(perm) + 1):
            r.append(perm[:i] + lst[0] + perm[i:])
            print(r, perm, lst)
    return r
print(permut("abc")) # ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']


def lambdaPerm(B):
    if len(B) == 1:
        return B
    r = []; list(map(lambda x: list(map(lambda y: r.append(x[:y] + B[0] + x[y:]), range(len(x) + 1))), lambdaPerm(B[1:]))); return r


#rint(lambdaPerm("abc"))
