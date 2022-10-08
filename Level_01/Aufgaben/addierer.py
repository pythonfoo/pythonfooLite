#!/usr/bin/env python3

# Dies ist eine Beispiellösung für die Aufgabe 1 aus Level 1:

# 1. Schreibe ein Programm, das die Zahlen 23 und 42 addiert:

print(23 + 42) # Erfüllt die Anforderung komplett.


# 2. Ändere das Programm so ab, dass die Zahlen in zwei Variablen gespeichert werden:

a = 23
b = 42
# Alternativ: a, b = 23, 42
print(a + b)


# 3. Ändere das Programm so ab, dass die Zahlen vom Benutzer eingegeben werden können:

inp_a = input("Bitte geben Sie den ersten Summanden ein: ") # type: str
inp_b = input("Bitte geben Sie den zweiten Summanden ein: ")
# Da input() immer einen String zurückgibt muss dieser in einen Integer umgewandelt werden,
# dabei entsteht eine Fehlerquelle, da ein Fehler auftritt, wenn der Benutzer keine gültige
# Zahl eingibt.
a = int(inp_a)
b = int(inp_b)

print(a + b)
