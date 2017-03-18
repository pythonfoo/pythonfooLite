#!/usr/bin/env python3

from getpass import getpass

PWD = "123456"

eingabe = getpass()

if eingabe == PWD:
    print("Richtig.")
elif eingabe in PWD:
    print("Fast.")
else:
    print("Falsch.")
