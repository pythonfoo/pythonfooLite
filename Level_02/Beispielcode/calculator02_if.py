"""
Das folgende Programm ist ein einfacher Taschenrechner.

Nach dem Eingeben zweier Zahlen kann eine Operation ausgewählt werden.
"""

# Für die Berechnung der Quadratwurzel wird die math Bibliothek benötigt,
# des Weiteren wird zum vorzeitigen Beenden die sys Bibliothek benötigt.
import math
import sys

# Zuerst eine Willkommensnachricht
print()
print("Dies ist ein einfacher Taschenrechner.")
print()

print("Bitte zwei Zahlen eingeben: ")
x = input("Erste Zahl: ")
y = input("Zweite Zahl: ")

# Die beiden Eingaben werden in Zahlen umgewandelt, damit das Programm auch mit
# Fließkommazahlen arbeiten kann, wird der Typ float verwendet.
x = float(x)
y = float(y)

# Zuerst wird ein kleines Menü angezeigt:
print("0: Betrag")
print("1: Summe")
print("2: Produkt")
print("3: Differenz")
print("4: Quotient")
print("5: Modulo Division")
print("6: Quadratwurzel")
print("7: Potenz")
print("q: Beenden")

# Nun wird nach der Auswahl gefragt
choice = input("Bitte eine Operation aussuchen: ")

if choice == "0":
    print("|x| =", abs(x))  # Betrag von x
    print("|y| =", abs(y))  # Betrag von y

elif choice == "1":
    print("x + y =", x + y)  # Summe

elif choice == "2":
    print("x * y =", x * y)  # Produkt

elif choice == "3":
    print("x - y =", x - y)  # Differenz
    print("y - x =", y - x)  # Differenz

elif choice == "4":
    print("x / y =", x / y)  # Quotient
    print("y / x =", y / x)  # Quotient

elif choice == "5":
    print("x % y =", x % y)  # Modulo Division
    print("y % x =", y % x)  # Modulo Division

elif choice == "6":
    print("sqrt(x) =", math.sqrt(x))  # Quadratwurzel
    print("sqrt(y) =", math.sqrt(y))  # Quadratwurzel

elif choice == "7":
    print("x ^ y =", pow(x, y))  # Potenz
    print("y ^ x =", pow(y, x))  # Potenz

elif choice == "q" or choice == "Q":
    # Alternativ: choice.upper() == "Q"
    print("Auf Wiedersehen")
    sys.exit(0)

else:
    print("Falsche Eingabe")
    sys.exit(1)
