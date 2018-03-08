#!/usr/bin/env python3

x = 5 # type: int
z = -3
basis = 2
exponent = 5

# Daten andere Typen in Integer umwandeln
# Achtung: Dies kann fehlschlagen!
y = int("6")

# Operatoren auf Integer anwenden:
# (für mehr Informationen siehe die Wiki-Seite zu Operatoren)
summe = x + y
produkt = x * z
quotient = 9 / 3 # type: float
differenz = x - z
potenz = pow(basis, exponent) # type: int
# Oder: basis ** exponent, Falsch ist basis ^ exponent
