#!/usr/bin/env python3

# Level 2:


# Der Datentyp <boolean>:
boolean = True
boolean2 = False


# Vergleichen von zwei boolean:
bool_result = boolean == boolean2
bool_result2 = boolean and boolean2
bool_result3 = boolean or boolean2

print(bool_result)
print(bool_result2)
print(bool_result3)
print()


# Der not-Operator:

boolean3 = not boolean
print(boolean3)


# Die if-Bedingung:
boolean3 = True

if boolean3 == True:
    print(True)

# Wenn nur geprüft werden soll, ob ein Ausdruck
# <True> ist, kann das '== True' weggelassen werden,
# da der Compiler überprüft, ob der Ausdruck True
# ist.

if boolean3:
    print(True)


# if-Bedingung mit else-Zweig:
summertime = True

if summertime:
    print("Yeah, it's summer!")
else:
    print("Ohh, it's winter!")


# if-Bedingung zum Vergleichen von int-Werten:
a = 5
b = 10
if a > b:
    print(a)
else:
    print(b)

# Wichtig: Auf die Einrückung achten!

# if-Bedingung mit elif- und else-Zweig:

a = 6
b = 7

if a > b:
    print("A")

elif a == b:
    print(" ")

elif a < b:
    print("B")

else:
    print("You broke the math.")


# Verschachtelte if-Bedingungen:

a = 3
b = 4
c = 5

if a < b:
    if b < c:
        print("C ist der Größte!")

    else:
        if b > c:
            print("B ist der Größte!")

        else:
            print("B und C sind die Größten!")

else:
    if a > b:
        if a > c:
            print("A ist der Größte!")

        else:
            if a < c:
                print("C ist der Größte!")

            else:
                print("A und C sind die Größten!")

# Wichtig:
# * Einrückung beibehalten!
# * Gültigkeitsbereiche beachten!

"""
Aufgaben:
* passwort.py:
  Programmiere eine einfache Passwortabfrage.
  Gibt der User das Passwort richtig ein, soll
  ein beliebiger Text angezeigt werden. Gibt er
  es falsch ein, soll ein anderer Text angezeigt
  werden.

* zahlenRaten.py
  Gib dem User 3 Versuche, eine von dir vorgegebene
  Zahl in einem bestimmten Intervall zu erraten.
  Nachdem er geraten hat, gib ihm aus, ob er die Zahl
  getroffen hat oder darüber oder darunter liegt.

Du solltest die Aufgaben in eigene Codedateien speichern,
weil spätere Level eventuell auf diese zurückgreifen.

"""
