#!/usr/bin/env python3
import random

def get_random_list(n: int) -> list:
    result = list(range(n))
    random.shuffle(result)
    return result
    
n = int(input("Länge der Liste: "))
unsorted_list = get_random_list(n)

# Bitte die Zeilen 1-12 unverändert lassen

def bubblesort(unsorted_list: list) -> list:
    changed = True
    while changed:
        changed = False
        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                changed = True

print(unsorted_list)
bubblesort(unsorted_list)
print(unsorted_list)