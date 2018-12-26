from random import randint


def gen_factorial(n):
    print("f")
    if n == 1:
        yield 1
    else:
        print(list(gen_factorial(n - 1)))
        for u in gen_factorial(n - 1):
            yield u
        yield list(gen_factorial(n - 1))[-1] * n

# print(list(gen_factorial(5)))


def factorial(n): yield 1 if n == 0 else n * list(factorial(n - 1))[-1]


def generator():
    for i in range(10):
        yield i
        if i == 5:
            yield "GYUI"


print(list(generator()))
