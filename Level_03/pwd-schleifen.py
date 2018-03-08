#!/usr/bin/env python3

from getpass import getpass

PWD = "123456"
N_VERSUCHE = 3

for x in range(N_VERSUCHE):
    eingabe = getpass() # type: str

    if eingabe == PWD:
        print("Richtig.")
        break
    elif eingabe in PWD:
        print("Fast.")
    else:
        print("Falsch.")
else:
    print("Passwort", N_VERSUCHE, "mal falsch eingegeben.")
    import sys
    sys.exit(1)

print("...")
