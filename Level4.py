#!/usr/bin/env python3

# Level 4:

import os

# Existiert eine Datei?

os.path.exists("Beispiele/lorem_ipsum.txt")
# OUT: False
os.path.exists("Beispiele/loremipsum.txt")
# OUT: True

# einen Ordner erstellen

os.mkdir("Beispiele/test")

# eine Datei auslesen

lorem_ipsum = open("Beispiele/loremipsum.txt", "r")
print(lorem_ipsum.read())
lorem_ipsum.close()

# eine Datei schreiben

test = open("Beispiele/test/test.txt", "w")
test.write("total toller Text")
test.close()
# OUT: 17

# eine Datei löschen

os.remove("Beispiele/test/test.txt")

# einen Ordner löschen

os.rmdir("Beispiele/test")
