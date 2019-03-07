#!/usr/bin/env python3

# Listentypen:

# 3. Das Dictionary:

# Ein Dictionary ist eine unsortierte Liste, in der
# immer ein <value>/Wert einem <key>/Schlüssel zugeordnet ist.

# Ein Dictionary wird über geschweifte Klammern
# definiert:
dictionary = {"Eins": "one", "Zwei": "two"} # type: dict
dictionary = dict([("Eins", "one"), ("Zwei", "two")])
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
