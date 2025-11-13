#!/usr/bin/env python3

# Dies ist eine Beispiellösung für Aufgabe 2c aus Level 4
# Schreiben Sie ein Programm, dass:
# * die Datei `monty.txt` öffnet und den Inhalt einliest,
# * im eingelesenen Inhalt jedes Auftauchen des Wortes `Python` durch `PYTHON`
#   ersetzt,
# * und den entstandenen Text in einer Datei `MONTY.txt`
#   (auf Windows unter `monty_upper.txt`) speichert

# Wir benötigen die Bibliothek pathlib für einige Funktionen:
from pathlib import Path

path_text = Path("monty.txt")
path_new = Path("MONTY.txt")

# 1. Einlesen des Textes:
if path_text.exists():
    file_obj = path_text.open("r")
    text = file_obj.read()
    file_obj.close()
else:
    print(f"Die Datei {path_text} existiert nicht.")
    exit()

# 2. "Python" ersetzen:
new_text = text.replace("Python", "PYTHON")

# 3. Neuen Text in neue Datei schreiben:
file_obj = path_new.open("w")
file_obj.write(new_text)
file_obj.close()
