#!/usr/bin/env python3
"""
Dieses Programm berechnet die Fibonacci-Reihe (rekursiv).
Dabei gilt: Die Summe zweier Elemente ergibt das Nächste.

(In Level 3 findet sich eine iterative Implementation.)
"""

# Die Fibonacci-Folge ist rekursiv definiert
#  - trotzdem ist die rekursive Berechnung ziemlich ineffizient im Vergleich zur Iterativen;
# siehe dazu https://github.com/pythonfoo/pythonfooLite/wiki/Rekursion_Vs._Iteration.
# Eine wesentlich perfomantere Version findet sich in Level 7.

def fib(n):
    # Die ersten beiden Elemente sind fix:
    if n <= 1:
        return n
    # Ansonsten: f(n) = f(n-1) + f(n-2)
    return fib(n-1) + fib(n-2)

n = int(input("Welches Element soll berechnet werden? "))
print(" =>", fib(n))
