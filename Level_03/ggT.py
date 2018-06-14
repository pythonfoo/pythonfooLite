#!/usr/bin/env python3
"""
Dieses Programm implementiert den euklidischen Algorithmus zur Bestimmung des größten gemeinsamen Teilers zweier Zahlen iterativ.

(In Level 5 findet sich eine rekursive Implementation.)
"""

# Eingabe
a = int(input("erste Zahl eingeben: "))
b = int(input("zweite Zahl eingeben: "))

# Beide Zahlen sollten positiv sein.
# Wir nehmen einfach den Betrag.
a = abs(a)
b = abs(b)

# a soll größer sein als b.
# Falls das nicht bereits der Fall ist,
# tauschen wir die beiden einfach.
if b > a:
    a, b = b, a

# Wenn b Null ist, sind wir fertig und a ist der ggT.
# Ansonsten müssen wir (nochmal) rechnen.
while b != 0:
    # Teile a mit Rest durch b;
    # setze a auf b
    # und b auf den Rest.
    a, b = b, a%b

# Ausgabe
print("Der größte gemeinsame Teiler dieser Zahlen ist:", a)
