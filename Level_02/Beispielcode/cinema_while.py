#!/usr/bin/env python3
fsk_shrek = 6
fsk_avengers = 12

counter: int = 0
while counter < 3:
    age_str: str = input("Wie alt bist du? ")

    if age_str.isdigit():
        age_int: int = int(age_str)
        break

    else:
        print("Bitte gib eine Zahl als Alter ein.")

    counter += 1
else:
    age_int: int = 7
    print("Wenn du uns dein Alter nicht sagen möchtest, müssen wir es schätzen.")
    print(f"Du bist wohl {age_int} Jahre alt.")

print("Folgende Filme könntest du dir ansehen: ")

if age_int >= fsk_avengers:
    print("Marvel: The Avengers")

elif age_int >= fsk_shrek:
    print("Shrek")

else:
    print("Leider haben wir keine Filme für dich im Angebot.")
