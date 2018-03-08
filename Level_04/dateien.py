#!/usr/bin/env python3

# Level 4: Dateien

import os

# Existiert eine Datei?

os.path.exists("lorem_ipsum.txt") # type: bool
# OUT: False
os.path.exists("loremipsum.txt")
# OUT: True

# einen Ordner erstellen

os.mkdir("test")

# eine Datei auslesen

lorem_ipsum = open("loremipsum.txt", "r")
print(lorem_ipsum.read())
lorem_ipsum.close()

# eine Datei schreiben

test = open("test/test.txt", "w")
test.write("total toller Text") # type: int
# OUT: 17
test.close()

# eine Datei löschen

os.remove("test/test.txt")

# einen Ordner löschen

os.rmdir("test")
