#!/usr/bin/env python3

# Dies ist eine Beispielslösung für die erste Aufgabe des fünften Levels:

def fakultaet(n):
    # Alternativ: n == 0
    if n == 1:
        return 1
    else: # Der else-Zweig kann auch weggelassen werden
        return n * fakultaet(n-1)

n = input("Bitte geben Sie eine Zahl ein: ")
if n.isdigit():
    n = int(n)
    print(fakultaet(n))
