#!/usr/bin/env python3

"""
with ist ein Kontextmanager.

Eine genauere Beschreibung als hier findet sich unter https://docs.python.org/3.6/reference/compound_stmts.html#with und https://docs.python.org/3.6/reference/datamodel.html#context-managers .

Hier folgen nun einige Beispiele.
"""

# Dateien öffnen

with open("../Level_04/loremipsum.txt") as lorem:
    print(lorem.read())

# Exceptions ignorieren

from contextlib import suppress

with suppress(ZeroDivisionError):
    print(1/0)

# temporäre Dateien und Ordner

import tempfile
from os.path import join

with tempfile.TemporaryFile(mode="w") as tmpfile:
    tmpfile.write("Dies ist ein Test.\n")

with tempfile.TemporaryDirectory() as tmpdir:
    with open(join(tmpdir, "test.txt"), "w") as test:
        test.write("Dies ist auch ein Test.\n")

# contextlib bietet Dekoratoren an um eigene Contextmanager zu erstellen:
# https://docs.python.org/3/library/contextlib.html