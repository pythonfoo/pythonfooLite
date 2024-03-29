#!/usr/bin/env python3

# Exceptions
try:
    1 / 0

except ZeroDivisionError as exc:
    print(exc)

finally:
    print("Fertig.")

# OUT:
# division by zero
# Fertig

# Nett ist auch "raise" innerhalb eines except-Blocks.

try:
    x = input()
    x = int(x)
except ValueError:
    print(x, " kann nicht als Integer benutzt werden.")
    raise
else:
    print("Kein Value-Fehler")

# So wird der Fehler bearbeitet, aber der Fehler bleibt nicht unentdeckt

# Man kann auch eigene Fehler definieren, die von Exception erben:
class MeinFehler(Exception):
    pass