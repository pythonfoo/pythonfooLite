#!/usr/bin/env python3

# Generatoren und yield
def gen(s):
    for char in s:
        yield char


# iterieren mit einer for-Schleife:
for x in gen("abcdef"):
    print(x)

# oder manuell mit next:
g = gen("foobar")
print(next(g))
print(next(g))

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
