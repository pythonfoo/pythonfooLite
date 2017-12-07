#!/usr/bin/env python3
"""
Dieses Programm berechnet die Fibonacci-Reihe (iterativ).
Dabei gilt: Die Summe zweier Elemente ergibt das Nächste.
"""

anzahl = int(input("Wie viele Elemente sollen berechnet werden? "))

# Die ersten beiden Elemente sind fix:
a = 0 # a ist das jeweils aktuelle Element.
b = 1 # b ist das jeweils nächste Element.

for n in range(anzahl):
    # Gebe das aktuelle Element aus:
    print(" * ", a)
    
    # Setze das aktuelle Element eins weiter
    # und das nächste auf die Summe des letzten und des aktuellen Elements.
    a, b = b, a+b
