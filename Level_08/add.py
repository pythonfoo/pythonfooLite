#!/usr/bin/env python3
from sys import argv

if len(argv) != 3:
    print(f"Aufruf: {argv[0]} a b")
    exit(1)

a = int(argv[1])
b = int(argv[2])
c = a + b
print(f"{a} + {b} = {c}")
