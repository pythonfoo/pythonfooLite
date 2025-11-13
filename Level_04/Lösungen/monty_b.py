#!/usr/bin/env python3

# Dies ist eine Beispiellösung für Aufgabe 2b aus Level 4
# * einen Integer n einliest,
# * die Häufigkeitstabelle der Buchstaben aus der, zuvor erstellten, Datei
#   "chars.txt" einliest und
# * die n häufigsten und die n seltenen Buchstaben ausgibt.

from pathlib import Path

path = Path("chars.txt")

# Eingabe Integer n:
n = input("Bitte eine Zahl eingeben: ")
if n.isdigit():
    n = int(n)
else:
    print("Es wurde keine Zahl eingegeben.")
    exit()

# Einlesen der Datei:
if not path.exists():
    print(f"Die Datei {path} wurde nicht gefunden.")
    exit()

table = {}
file_obj = path.open("r")
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


# Ausgeben der n häufigsten und n seltenen Buchstaben:
common = []
rare = []

for entry in table[0:n]:
    common.append(entry[0])

for entry in table[-(n+1):-1]:
    rare.append(entry[0])

print(f"Die {n} häufigsten Buchstaben sind: ")
print(common)

print(f"Die {n} seltenen Buchstaben sind: ")
print(rare)
