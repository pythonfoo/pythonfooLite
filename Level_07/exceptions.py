#!/usr/bin/env python3

# Exceptions
>> > try:
...     1 / 0
...
... except ZeroDivisionError as exc:
... print(exc)
...
... finally:
... print("Fertig.")
...
division by zero
Fertig.

# Nett ist auch "raise" innerhalb eines except-Blocks.
