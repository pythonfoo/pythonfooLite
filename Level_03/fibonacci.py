#!/usr/bin/env python3
"""
Dieses Programm berechnet die Fibonacci-Reihe (iterativ).
Dabei gilt: Die Summe zweier Elemente ergibt das Nächste.

(In Level 5 findet sich eine rekursive Implementation.)
"""

anzahl = int(input("Wie viele Elemente sollen berechnet werden? "))

# Die ersten beiden Elemente sind fix:
current = 0  # current ist das jeweils aktuelle Element.
next = 1  # next ist das jeweils nächste Element.

for n in range(anzahl):  # type: int
    # Gebe das aktuelle Element aus:
    print(" * ", current)
    
    # Setze das aktuelle Element eins weiter
    # und das nächste auf die Summe des letzten und des aktuellen Elements.
    current, next = next, current + next
