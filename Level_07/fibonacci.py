#!/usr/bin/env python3
"""
Dieses Programm berechnet die Fibonacci-Reihe rekursiv (siehe Level 5).
Dabei werden aber die Zwischenergebnisse gecachet.
"""

def cache(func):
    """
    Dies ist ein Dekorator der Funktionsaufrufe cachet.
    Er funktioniert natürlich nur sinnvoll für mathematische Funktionen,
    also Funktionen, die beim Aufruf mit den gleichen Parametern immer das gleiche Ergebnis zurückliefern und sonst keine Seiteneffekte haben.
    
    Dieser Cache hat keinerlei Ersetzungs- oder Löschstrategien, wird also mit der Zeit immer größer.
    Das ist nicht ideal, reicht aber für dieses Beispiel.
    """
    # ein Dict erzeugen für die zwischengespeicherten Werte
    values = dict()
    
    # die neue Funktion
    # hier der Einfachheit halber nur positionale Parameter
    def new_func(*args):
        # Ist der Wert schon berechnet worden?
        if args in values.keys():
            # dann gebe das Ergebnis zurück
            return values[args]
        # Ansonsten müssen wir die Funktion aufrufen und das Ergebnis speichern.
        result = func(*args)
        values[args] = result
        return result
    
    return new_func

# die gleiche unpeformante Version von Fibonacci wie in Level 5
@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Welches Element soll berechnet werden? "))
print(" =>", fib(n))
