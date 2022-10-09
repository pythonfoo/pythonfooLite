#!/usr/bin/env python3

# map

def add_2(x):
    return x + 2

l = range(10)

# Statt:
result = []
for i in l:
    result.append(add_2(i))

# Kann man map() benutzen:
result = list(map(add_2, l))


# oder:
result = [add_2(x) for x in l]

# filter

def even(n):
    return n % 2 == 0

r = range(100)
even_numbers = list(filter(even, r))

even_numbers = [x for x in r if even(x)]
print(even_numbers)

# zip
iter1 = range(10)
iter2 = range(-10,0)
print(list(zip(iter1, iter2)))

# lambda
print(list(filter(lambda x: x % 2 == 0, r)))

print(all(even(x) for x in even_numbers))

# für mehr Spaß mit Generatoren: https://docs.python.org/3/library/itertools.html