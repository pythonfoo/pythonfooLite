#!/usr/bin/env python3

from getpass import getpass

PWD = "123456"
N_VERSUCHE = 3

for x in range(N_VERSUCHE):
    eingabe = getpass()

    if eingabe == PWD:
        print("Richtig.")
        break
    elif eingabe in PWD:
        print("Fast.")
    else:
        print("Falsch.")
else:
    print("Passwort {} mal falsch eingegeben.".format(N_VERSUCHE))
    import sys
    sys.exit(1)

print("...")
