#!/usr/bin/env python3

from getpass import getpass

PWD = "123456" # type: str

eingabe = getpass() # type: str

if eingabe == PWD:
    print("Richtig.")
elif eingabe in PWD:
    print("Fast.")
else:
    print("Falsch.")
