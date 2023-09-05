"""
Das folgende Programm soll eine einfacher Taschenrechner sein.

Das Programm nimmt zwei Zahlen entgegen und führt daraufhin einige Berechnungen
mit diesen durch.
"""

# Für die Quadratwurzel benötigen wir die math Bibliothek
import math

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

# Jetzt werden einige Operationen mit den beiden Werten durchgeführt:
sum_xy = x + y  # Summe
dif_xy = x - y  # Differenz
dif_yx = y - x  # Differenz
pro_xy = x * y  # Produkt
quo_xy = x / y  # Quotient
quo_yx = y / x  # Quotient
mod_xy = x % y  # Modulo Division
mod_yx = y % x  # Modulo Division
x_sqrt = math.sqrt(x)  # Quadratwurzel
y_sqrt = math.sqrt(y)  # Quadratwurzel

# Nun werden die Ergebnisse der Operationen ausgegeben:
print("x + y =", sum_xy)
print("x - y =", dif_xy)
print("y - x =", dif_yx)
print("x * y =", pro_xy)
print("x / y =", quo_xy)
print("y / x =", quo_yx)
print("x % y =", mod_xy)
print("y % x =", mod_yx)
print("sqrt(x) = ", x_sqrt)
print("sqrt(y) = ", y_sqrt)
