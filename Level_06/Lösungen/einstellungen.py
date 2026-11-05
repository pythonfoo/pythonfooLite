#!/usr/bin/env python3

# Dies ist eine Beispiellösung für die Aufgabe 6.2 (Einstellungen) aus Level 6.

import json
from pathlib import Path

einstellungen_datei = Path("einstellungen.json")

# 1. Ein verschachteltes dict mit Einstellungen erstellen.
# ("tasten" ist selbst wieder ein dict - das kann CSV nicht, JSON aber schon.)
einstellungen = {
    "spielername": "Löwenherz",
    "lautstärke": 80,
    "vollbild": True,
    "tasten": {
        "springen": "Leertaste",
        "ducken": "Strg",
    },
}

# 2. Als JSON-Datei speichern.
# indent=2 macht die Datei lesbar, ensure_ascii=False erhält die Umlaute.
with einstellungen_datei.open("w", encoding="utf-8") as datei:
    json.dump(einstellungen, datei, indent=2, ensure_ascii=False)

# 3. Die Datei wieder einlesen und auf einen verschachtelten Wert zugreifen.
with einstellungen_datei.open("r", encoding="utf-8") as datei:
    geladen = json.load(datei)

print("Spieler:", geladen["spielername"])
print("Lautstärke:", geladen["lautstärke"])
# Zugriff auf einen Wert im inneren dict:
print("Taste zum Springen:", geladen["tasten"]["springen"])
