#!/usr/bin/env python3

# Dies ist eine Beispiellösung für Aufgabe 2a aus Level 4
# Schreibe ein Programm, dass:
# die Datei `monty.txt` aus dem Code-Repository einliest,
# * eine Worthäufigkeitstabelle erstellt,
# * eine Buchstabenhäufigkeitstabelle erstellt,
# * die Worthäufigkeiten lesbar formatiert in "words.txt" abspeichert,
# * und die Buchstabenhäufigkeiten lesbar formatiert in "chars.txt" speichert.

# Wir benötigen die Bibliothek pathlib für einige Funktionen:
from pathlib import Path

path_text = Path("monty.txt")
path_words = Path("words.txt")
path_chars = Path("chars.txt")

# 1. Einlesen des Textes:

if path_text.exists():
    file_obj = path_text.open("r")  # Öffnen der Datei
    text = file_obj.read()  # Einlesen des Textes
    file_obj.close()  # Schließen des Dateiobjekts
else:
    print("Die Datei {} existiert nicht.".format(path_text))
    exit()

# Alternativ:
# with path_text.open("r") as file_obj:
#     text = file_obj.read()

# 2. Worthäufigkeitstabelle
text = text.replace("\n"," ")  # entfernen der Return-Steuerzeichen
text = text.lower()  # der ganze Text in Kleinbuchstaben
words = text.split(" ")  # Aufteilen am Leerzeichen

word_count = {}
for element in words:
    if element.isalpha():  # handelt es sich um ein Wort
        if element in word_count:
            word_count[element] += 1
        else:
            word_count[element] = 1


# 3. Buchstabenhäufigkeitstabelle:
char_count = {}
for char in text:
    if char.isalpha():  # handelt es sich um einen Buchstaben
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1


# 4. Abspeichern der Tabellen:
# Worthäufigkeiten:
file_obj = path_words.open("w")
for word, count in word_count.items():
    line = f"{word};{count}\n"
    file_obj.writelines([line])
file_obj.close()

# Buchstabenhäufigkeiten:
file_obj = path_chars.open("w")
for char, count in char_count.items():
    line = f"{char};{count}\n"
    file_obj.writelines([line])
file_obj.close()
