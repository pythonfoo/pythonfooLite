#!/usr/bin/env python3

# Dies ist eine Beispiellösung für die Aufgabe 6.1 (Notenschnitt) aus Level 6.

import csv
from pathlib import Path

noten_datei = Path("noten.csv")

# 1. Eine CSV-Datei mit Schülern und ihren Noten anlegen:
schueler = [
    {"name": "Anna", "note": 2},
    {"name": "Ben", "note": 1},
    {"name": "Clara", "note": 3},
    {"name": "David", "note": 2},
]
with noten_datei.open("w", newline="", encoding="utf-8") as datei:
    writer = csv.DictWriter(datei, fieldnames=["name", "note"])
    writer.writeheader()
    writer.writerows(schueler)

# 2. Die Datei wieder einlesen und jeden Schüler ausgeben:
with noten_datei.open("r", newline="", encoding="utf-8") as datei:
    gelesen = list(csv.DictReader(datei))

for eintrag in gelesen:
    print(eintrag["name"], "hat die Note", eintrag["note"])

# 3. Den Notendurchschnitt berechnen.
# Achtung: Aus der CSV kommen alle Werte als String zurück -
# zum Rechnen müssen wir sie erst mit int() umwandeln!
summe = 0
for eintrag in gelesen:
    summe += int(eintrag["note"])

durchschnitt = summe / len(gelesen)  # int / int -> float
print(f"Notendurchschnitt: {durchschnitt:.2f}")
