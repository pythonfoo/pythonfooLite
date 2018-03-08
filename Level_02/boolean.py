#!/usr/bin/env python3

# Der Datentyp <boolean>:
boolean = True # type: bool
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