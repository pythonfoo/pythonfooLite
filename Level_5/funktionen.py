#!/usr/bin/env python3

# Funktionen:

def funktion():
    print("Hallo!")
funktion()
# OUT: Hallo!


def funktion(text):
    print(text)
funktion("a")
# OUT: a


def funktion(text, wirklich):
    if wirklich:
        print(text)
funktion("Hallo", True)
# OUT: Hallo
funktion(True, "Hallo")
# OUT: True


def funktion(text="Beispiel", wirklich=False):
    if wirklich:
        print(text)
funktion()

funktion(wirklich=True)
# OUT: Beispiel

funktion(wirklich=True, text="Abc")
# OUT: Abc


def ja():
    return "Ja"
ja()
# OUT: 'Ja'


# Rekursion:

def fun():
    print("Fun!")
    fun()

# Quersumme:
def quersumme(zahl):
    qs = 0
    for ziffer in str(zahl):
        qs += int(ziffer)
    return qs
