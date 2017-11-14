#!/usr/bin/env python3

# Dies ist eine Beispielslösung für Aufgabe 2c aus Level 4
# Schreiben Sie ein Programm, dass:
# * die Datei `monty.txt` öffnet und den Inhalt einliest,
# * im eingelesenen Inhalt jedes Auftauchen des Wortes `Python` durch `PYTHON`
#   ersetzt,
# * und den entstandenen Text in einer Datei `MONTY.txt`
#   (auf Windows unter `monty_upper.txt`) speichert

# Wir benötigen die Bibliotheken os und sys für einige Funktionen:
import os
import sys

filename_text = "monty.txt"
filename_new = "MONTY.py"

# 1. Einlesen des Textes:
if os.path.exists(filename_text):
    file_obj = open("monty.txt", "r")
    text = file_obj.read()
    file_obj.close()
else:
    print("Die Datei {} existiert nicht.".format(filename_text))
    sys.exit()

# 2. "Python" ersetzen:
new_text = text.replace("Python", "PYTHON")

# 3. Neuen Text in neue Datei schreiben:
file_obj = open(filename_new, "w")
file_obj.write(new_text)
file_obj.close()
