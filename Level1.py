#!/usr/bin/env python3

# Level 1:

import getpass

# Das ist ein Kommentar.
# Ein Kommentar kann benutzt werden um den Code
# zu dokumentieren.
# Der Kommentar ändert nichts an der Ausführung
# des Programms.


# Eingabe/<input>:
eingabe = input()

# Eingabe mit Inhalt:
eingabe = input("Bitte geben Sie einen Text ein: ")

# Eingabe ohne die Eingabe anzuzeigen:
getpass.getpass()

# <getpass> mit Inhalt:
getpass.getpass("Bitte geben Sie eine Nachricht ein: ")


# Ausgabe:
print("Hello World")

h = "Hello"
w = "World"

print(h + w)


# Der Datentyp <String>:

eine_Zeile = "Dies ist ein einzeiliger String"

mehr_Zeilen = """
Das ist ein Multilinestring.
So kann ich mehrere Zeilen drucken.
	Einrückung beachten.
"""

f = "foo"
b = "bar"
space = " "

print(f + b)
print(5 * f)
print(5 * (f + space))

x = str(5)


# Der Datentyp <int>:
x = 5
y = int("6")
z = -3
basis = 2
exponent = 5

summe = x + y
produkt = x * z
quotient = 9 / 3
differenz = x - z
potenz = pow(basis, exponent)  # Oder: basis ** exponent


# Kommentiere die einzelnen Codeblöcke doch
# nacheinander aus und beobachte, was das
# Programm macht.

"""
Aufgaben:
* Hello_World.py
	Schreibe ein Programm, das "Hello World!" ausgibt

* Eingabe.py
	Schreibe ein Programm, das die Eingabe des Benutzers
	ausgibt.

* Addierer.py
	Schreibe ein Programm, das zwei Zahlen vom User ent-
	gegennimmt und die Summe ausgibt.

* Kreis.py
	Schreibe ein Programm, das den Flächeninhalt eines
	Kreises zu einem Radius ausgibt, den der User ein-
	geben kann.
	Tipp:

	import math
	pi = math.pi

Du solltest die Aufgaben in eigene Codedateien speichern,
weil spätere Level eventuell auf diese zurückgreifen.

"""
