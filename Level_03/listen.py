#!/usr/bin/env python3

# Listentypen:

# 1. Die Liste:

# Eine Liste ist eine beliebig lange Folge von beliebigen Objekten

# Eine Liste wird mit Hilfe von eckigen Klammern definiert.
liste = [0, "foo"] # type: list
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
l = len(liste) # type: int
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
liste2.remove(9) # type: None
print(liste2)


# Um festzustellen, wie oft ein Wert in einer Liste vorhanden ist kann
# die count()-Methode verwendet werden.
liste3 = list("aabbbcccc")
print(liste3.count("a"))
print(liste3.count("d"))


# Eine Liste kann mit sort() sortiert werden:
liste2 = [9,6,3,2,7]
liste2.sort() # type: None
print(liste2)


# Auf die einzelnen Zeichen eines Strings kann ebenfalls über den Index
# zugegriffen werden, wie bei einer Liste.
String = "ABCDEFGHIJKLMNOPQRSTUVW"
print(String)
print(String[4])
