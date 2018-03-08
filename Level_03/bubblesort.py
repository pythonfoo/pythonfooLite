#!/usr/bin/env python3
import random

def get_random_list(n: int) -> list:
    result = list(range(n))
    random.shuffle(result)
    return result
    
n = int(input("Länge der Liste: "))
unsortet_list = get_random_list(n)

# Bitte die Zeilen 1-12 unverändert lassen
