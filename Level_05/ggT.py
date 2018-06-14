#!/usr/bin/env python3
"""
Dieses Programm implementiert den euklidischen Algorithmus zur Bestimmung des größten gemeinsamen Teilers zweier Zahlen rekursiv.

(In Level 3 findet sich eine iterative Implementation.)
"""

# Berechnung
def ggT(a: int, b: int) -> int:
    # Beide Zahlen sollten positiv sein.
    # Wir nehmen einfach den Betrag.
    a = abs(a)
    b = abs(b)
    
    # a soll größer sein als b.
    # Falls das nicht bereits der Fall ist,
    # tauschen wir die beiden einfach.
    if b > a:
        return ggT(b, a)
    
    # Wenn b Null ist, sind wir fertig und a ist der ggT.
    # Ansonsten müssen wir (nochmal) rechnen.
    if b == 0:
        return a
    
    # Teile a mit Rest durch b;
    # setze a auf b
    # und b auf den Rest.
    return ggT(b, a%b)

# Eingabe
a = int(input("erste Zahl eingeben: "))
b = int(input("zweite Zahl eingeben: "))

# Ausgabe
print("Der größte gemeinsame Teiler dieser Zahlen ist:", ggT(a, b))
