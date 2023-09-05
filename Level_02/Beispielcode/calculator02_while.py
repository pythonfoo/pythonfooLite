"""
Das folgende Programm ist ein einfacher Taschenrechner.

Nach dem Eingeben zweier Zahlen kann eine Operation ausgewählt werden.
Anschließend wird nach neuen Zahlen gefragt.
"""

# Für die Berechnung der Quadratwurzel wird die math Bibliothek benötigt,
# des Weiteren wird zum vorzeitigen Beenden die sys Bibliothek benötigt.
from math import sqrt
import sys

# Zuerst eine Willkommensnachricht
print()
print("Dies ist ein einfacher Taschenrechner.")
print()

# Das Menü wird angezeigt:
print("0: Betrag")
print("1: Summe")
print("2: Produkt")
print("3: Differenz")
print("4: Quotient")
print("5: Modulo Division")
print("6: Quadratwurzel")
print("7: Potenz")
print("8: Fakultät")
print("q: Beenden")
print()

# Das Programm läuft in einer Endlosschleife und wird durch eine entsprechende
# Nutzereingabe beendet.
while True:
    choice = input("Bitte eine Operation auswählen: ")

    # Falls der Benutzer ein "q" eingibt soll das Programm beendet werden
    if choice.upper() == "Q":
        print("Auf Wiedersehen")
        sys.exit(0)

    x = input("Bitte eine ganze Zahl eingeben: ")
    if choice not in ("0", "6", "8"):
        # Diese Operationen benötigen mehr als einen Wert
        y = input("Bitte eine weitere ganze Zahl eingeben: ")
        y = int(y)

    # Die Eingabe wird in einen Integer umgewandelt
    x = int(x)

    if choice == "0":
        print("Betrag: |x| =", abs(x))  # Betrag von x

    elif choice == "1":
        print("Summe: x + y =", x + y)  # Summe

    elif choice == "2":
        print("Produkt: x * y =", x * y)  # Produkt

    elif choice == "3":
        print("Differenz:")
        print("x - y =", x - y)  # Differenz
        print("y - x =", y - x)  # Differenz

    elif choice == "4":
        print("Quotient:")
        print("x / y =", x / y)  # Quotient
        print("y / x =", y / x)  # Quotient

    elif choice == "5":
        print("Rest:")
        print("x % y =", x % y)  # Modulo Division
        print("y % x =", y % x)  # Modulo Division

    elif choice == "6":
        print("Quadratwurzel: sqrt(x) =", sqrt(x))  # Quadratwurzel

    elif choice == "7":
        print("Potenz:")
        print("x ^ y =", pow(x, y))  # Potenz
        print("y ^ x =", pow(y, x))  # Potenz

    elif choice == "8":
        tmp = 1
        for i in range(2, x + 1):
            tmp = tmp * i
        print("Fakultät: x! =", str(tmp))

    else:
        print("Ungültige Eingabe")
        continue

    print("")
