#!/usr/bin/env python3

# Generatoren und yield
def gen(s):
    for char in s:
        yield char


for x in gen("abcdef"):
    print(x)

# Dekoratoren
def f(x):
    return x**2


# IN: f(2)
# OUT: 4
# IN: f(3)
# OUT: 9

def dec(func):
    def inner_func(*args):
        print(args)
        r = func(*args)
        print("Return: {}".format(r))
        return r
    return inner_func

@dec
def f(x):
    return x**2


# IN: f(2)
# OUT: (2,)
# OUT: Return:
# OUT:    4
# OUT:4
