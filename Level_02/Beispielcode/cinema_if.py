#!/usr/bin/env python3

age_str: str = input("Wie alt bist du? ")

if age_str.isdigit():
    age_int: int = int(age_str)
else:
    print("Bitte gib eine Zahl als Alter ein.")
    exit()

fsk_shrek = 6
fsk_avengers = 12

print("Folgende Filme könntest du dir ansehen: ")

if age_int >= fsk_avengers:
    print("Marvel: The Avengers")

elif age_int >= fsk_shrek:
    print("Shrek")
else:
    print("Leider haben wir keine Filme für dich im Angebot.")
