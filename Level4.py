>>> import os

#Existiert eine Datei?

>>> os.path.exists("Beispiele/lorem_ipsum.txt")
False
>>> os.path.exists("Beispiele/loremipsum.txt")
True

#einen Ordner erstellen

>>> os.mkdir("/tmp/nkhsekgs")

#eine Datei auslesen

>>> lorem_ipsum = open("loremipsum.txt", "r")
>>> print(lorem_ipsum.read())

#eine Datei schreiben

>>> test = open("test.txt", "w")
>>> test.write("total toller Text")
17
