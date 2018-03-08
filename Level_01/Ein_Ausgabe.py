#!/usr/bin/env python3

from getpass import getpass # hilfreich für Passwortabfragen


## Ausgabe

print("Dieser Text wird ausgegeben.")

# Man kann auch mehrere Dinge gleichzeitig ausgeben.
print(1, 2, "Apfel", "Birne")

# Man kann auch Variablen ausgeben:
x = 5  # type: int
print(x) 
text = "Hallo, Welt!" # type: str
print(text)
print(x, text)


## Eingabe

print("Bitte etwas eingeben:")
eingabe = input() # type: str

print("Die Eingabe war: ")
print(eingabe)

# Das geht natürlich auch etwas kürzer:
eingabe = input("Bitte etwas eingeben: ")
print("Die Eingabe war:", eingabe)

## Eingabe ohne die Eingabe anzuzeigen:
passwort = getpass() # type: str # Standardprompt: "Password: "
print("Eingabe:", passwort)

passwort = getpass("Bitte Passwort eingeben: ")
print("Eingabe:", passwort)
