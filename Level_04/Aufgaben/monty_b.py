#!/usr/bin/env python3

# Dies ist eine Beispielslösung für Aufgabe 2b aus Level 4
# * einen Integer n einliest,
# * die Häufigkeitstabelle der Buchstaben aus der, zuvor erstellten, Datei
#   "chars.txt" einliest und
# * die n häufigsten und die n seltesten Buchstaben ausgibt.

import os
import sys

filename = "chars.txt"

# Eingabe Integer n:
n = input("Bitte eine Zahl eingeben: ")
if n.isdigit():
    n = int(n)
else:
    print("Es wurde keine Zahl eingegeben.")
    sys.exit()

# Einlesen der Datei:
if not os.path.exists(filename):
    print("Die Datei {} wurde nicht gefunden.".format(filename))
    sys.exit()

table = {}
file_obj = open(filename, "r")
for line in file_obj:
    key = line.split(";")[0]
    value = int(line.split(";")[1])
    table[key] = value
file_obj.close()

# Sortieren
tmp = list(table.items())
table = []
for i in range(len(tmp)):
    max_key = 0
    max_value = 0
    for index in range(len(tmp)):
        entry = tmp[index]
        if entry[1] > max_value:
            max_key = index
            max_value = entry[1]
    max_entry = tmp[max_key]
    table.append(max_entry)
    tmp.remove(max_entry)


# Ausgeben der n häufigsten und n seltesten Buchstaben:
common = []
rare = []

for entry in table[0:n]:
    common.append(entry[0])

for entry in table[-(n+1):-1]:
    rare.append(entry[0])

print("Die {} häufigsten Buchstaben sind: ".format(n))
print(common)

print("Die {} seltesten Buchstaben sind: ".format(n))
print(rare)
