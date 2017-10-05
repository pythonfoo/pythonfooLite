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

    
