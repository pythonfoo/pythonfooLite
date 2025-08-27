#!/usr/bin/env python3
from getpass import getpass
from sys import exit

PWD = "123456"

print("Hallo, bitte gib dein Passwort ein:")

counter = 0
while counter < 3:
    eingabe = getpass("> ")
    if eingabe == PWD:
        print("Richtig.")
        break
    else:
        print("Falsch.")
        counter += 1
else:
    print("leider zu oft falsch :(")
    exit()

print("Herzlich Willkommen")
