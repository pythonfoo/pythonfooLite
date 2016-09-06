#!/usr/bin/env python3

# Level 4:

import os

# Existiert eine Datei?

os.path.exists("Beispiele/lorem_ipsum.txt")
# OUT: False
os.path.exists("Beispiele/loremipsum.txt")
# OUT: True

# einen Ordner erstellen

os.mkdir("/tmp/nkhsekgs")

# eine Datei auslesen

lorem_ipsum = open("loremipsum.txt", "r")
print(lorem_ipsum.read())

# eine Datei schreiben

test = open("test.txt", "w")
test.write("total toller Text")
# OUT: 17
