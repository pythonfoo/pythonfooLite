#!/usr/bin/env python3

# Dies ist eine Beispiellösung für die Aufgabe 6.3 (Adressbuch) aus Level 6.

import sqlite3
from pathlib import Path

db_datei = Path("adressbuch.db")
if db_datei.exists():
    db_datei.unlink()  # für einen sauberen Start eine evtl. alte Datei löschen

verbindung = sqlite3.connect(db_datei)
cursor = verbindung.cursor()

# 1. Eine Tabelle anlegen.
cursor.execute("CREATE TABLE kontakte (name TEXT, telefon TEXT)")

# 2. Mehrere Kontakte einfügen.
# WICHTIG: Werte immer über die Platzhalter ? einsetzen, niemals den Befehl
# per f-string oder + zusammenbauen (Stichwort SQL-Injection)!
kontakte = [
    ("Anna", "0151-1111111"),
    ("Ben", "0152-2222222"),
    ("Clara", "0153-3333333"),
]
cursor.executemany("INSERT INTO kontakte VALUES (?, ?)", kontakte)
verbindung.commit()

# 3. Nach einem Kontakt suchen.
gesucht = "Ben"
cursor.execute("SELECT name, telefon FROM kontakte WHERE name = ?", (gesucht,))
for name, telefon in cursor.fetchall():
    print(f"{name}: {telefon}")

verbindung.close()

# Erweiterung (optional): Statt eines festen Namens kannst du mit
#     gesucht = input("Welchen Kontakt suchst du? ")
# den gesuchten Namen interaktiv abfragen.
