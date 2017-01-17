#!/usr/bin/env python3

# Level 3:


# Listentypen:

# 1. Die Liste:

# Eine Liste ist eine beliebig lange Folge von beliebigen Objekten

# Eine Liste wird mit Hilfe von eckigen Klammern definiert.
liste = [0, "foo"]
print(liste)


# Mit list() lässt sich bspw. ein String in einen Liste verwandeln:
print(list(String))


# Auf ein Element in einer Liste wird über dessen Index
# zugegriffen. Der Index ist die Stelle, an der das Element
# steht.
# Wichtig: Die Zählung des Index beginnt mit 0,
# daher ist der Index des ersten Elements 0.
# Liste: [0, "foo"]
# Index:  0    1

element = liste[0]
print(element)

# Die Funktion liefert für viele Objekte die Länge zurück.
# Bei einer Liste enspricht die Länge der Anzahl an Elementen.
l = len(liste)
print(l)


# Die append()-Methode fügt einer Liste ein beliebiges
# Element hinzu:
liste.append("bar")
print(liste)


# Statt ein Objekt am Ende einer Liste anzufügen, ist es auch möglich,
# es an einem Index einzusetzen. Dabei wird das Objekt vor dem Index
# eingesetzt.
liste.insert(0, "test")
print(liste)


# Die pop()-Methode löscht das Objekt an dem Index in der Liste.
# Ist kein Index angegeben lösht pop() das letzte Element
liste.pop()
print(liste)


# Ein Element kann aber nicht nur über den Index gelöscht werden, sondern
# auch über das Objekt, es wird allerdings nur das erste Auftreten des
# Objektes gelöscht. Dabei wird ein Fehler geworfen, falls das Objekt
# nicht in der Liste vorhanden ist.
liste2.remove(9)
print(liste2)


# Um festzustellen, wie oft ein Wert in einer Liste vorhanden ist kann
# die count()-Methode verwendet werden.
liste3 = list("aabbbcccc")
print(liste3.count("a"))
print(liste3.count("d"))


# Eine Liste kann mit sort() sortiert werden:
liste2 = [9,6,3,2,7]
liste2.sort()
print(liste2)


# Auf die einzelnen Zeichen eines Strings kann ebenfalls über den Index
# zugegriffen werden, wie bei einer Liste.
String = "ABCDEFGHIJKLMNOPQRSTUVW"
print(String)
print(String[4])




# 2. Das Tuple:

# Ein Tuple ist eine unveränderliche und unsortierte
# Folge von Elementen.

# Ein Tuple wird über runde Klammern definiert:
Tuple = ("foo", "bar")
print(Tuple)

# Mit einem Index kann auf ein Element zugegriffen
# werden:
print(Tuple[0])

# Mit dem len()-Befehl lässt sich die Länge aus-
# geben:
print(len(Tuple))




# 3. Das Dictionary:

# Ein Dictionary ist eine unsortierte Liste, in der
# immer ein <value>/Wert einem <key>/Schlüssel zugeordnet ist.

# Ein Dictionary wird über geschweifte Klammern
# definiert:
dictionary = {"Eins": "one", "Zwei": "two"}
print(dictionary)

# Auf einen value wird mit Hilfe des keys zu-
# gegriffen:
print(dictionary["Eins"])

# Ein neues Key-Value-Paar wird erstellt,
# indem auf ein nicht-existierenden value zu-
# gegriffen wird und dieser definiert wird:
dictionary["Wasser"] = "water"
print(dictionary)
# Als keys geeignet sind zum Beispiel: Integer, Strings, Tupel, Boolean


# Mit len() lässt sich die Länge ausgeben:
print(len(dictionary))


# Die Schlüssel eines Dictionarys können als Liste zurückgegeben werden:
print(dictionary.keys())


# ebenso wie die Values:
print(dictionary.items())




# Schleifen:

# 1. Die while-Schleife:

# Im Kopf der while-Schleife steht eine Bedingung.
# Wenn die Begindung erfüllt ist, durchläuft die while-Schleife ihren Bauch.
# Danach prüft sie erneut die Bedingung. Und das immer so weiter.
counter = 0

while counter < 10:
    counter += 1

# Endlosschleife:
"""
while True:
	print("foo")
"""


# 2. Die for-Schleife:

# Die for-Schleife durchläuft ein iterierbares
# Objekt. Alle oben genannten Listen sind solche
# iterierbaren Objekte.
String = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in String:
    print(char)

# Beim Durchlaufen eines Dictionary wird jedoch nur
# der key zurückgegeben:
Dictionary = {"one": "Eins", "two": "Zwei", "three": "drei"}
for key in Dictionary:
    print(key)
    print(Dictionary[key])

# Mit dem Befehl range() erschafft man ein iterierbares
# Objekt, das mit Zahlen gefüllt ist:
R = range(10)
print(list(R))

# Dabei kann man auch den Startwert und die Schrittweite
# angeben:
R = range(0, 101, 2)
print(list(R))

# Somit kann man eine Zählschleife implementieren:
R = range(10)
for i in R:
    print(i)

# oder:

for i in range(10):
    print(i)

"""
Aufgaben:
* fakultaet.py:
  Schreibe ein Programm, das die Fakultaet einer Zahl
  ausgibt, die der User eingibt.
  Fakultaet(n) = Fakultaet(n-1) * n
  Fakultaet(0) = 1

* potenz.py:
  Schreibe ein Programm, das dem User eine Basis und
  einen Exponenten eingeben lässt und ihm dann die
  Potenz ausrechnet.

* passwort.py:
  Ändere dein Passwortprogramm so ab, dass die Anzahl an Ver-
  suchen, die der Benutzer hat, als int-Variable im Code
  hinterlegt werden kann.

* zahlenRaten.py:
  Ändere dein Programm so ab, dass der User den Bereich
  mit zwei Integern festlegen kann und die Anzahl an Ver-
  suchen, die er hat, von der Größe des Intervalls abhängt.

Du solltest die Aufgaben in eigene Codedateien speichern,
weil spätere Level eventuell auf diese zurückgreifen.

"""
