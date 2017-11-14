#!/usr/bin/env python3

# Dies ist eine Beispielslösung für Aufgabe 2a aus Level 4
# Schreibe ein Programm, dass:
# die Datei `monty.txt` aus dem Coderepository einliest,
# * eine Worthäufigkeitstabelle erstellt,
# * eine Buchstabenhäufigkeitstabelle erstellt,
# * die Worthäufigkeiten lesbar formatiert in "words.txt" abspeichert,
# * und die Buchstabenhäufigkeiten lesbar formatiert in "chars.txt" speichert.

# Wir benötigen die Bibliotheken os und sys für einige Funktionen:
import os
import sys

filename_text = "monty.txt"
filename_words = "words.txt"
filename_chars = "chars.txt"

# 1. Einlesen des Textes:

if os.path.exists(filename_text):
    file_obj = open("monty.txt", "r")
    text = file_obj.read()
    file_obj.close()
else:
    print("Die Datei {} existiert nicht.".format(filename_text))
    sys.exit()


# 2. Worthäufigkeitstabelle
text = text.replace("\n"," ")
text = text.lower()
words = text.split(" ")

word_count = {}
for element in words:
    if element.isalpha():
        if element in word_count:
            word_count[element] += 1
        else:
            word_count[element] = 1


# 3. Buchstabenhäufigkeitstabelle:
char_count = {}
for char in text:
    if char.isalpha():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1


# 4. Abspeichern der Tabellen:
# Worthäufigkeiten:
file_obj = open(filename_words, "w")
for key in word_count:
    line = "{};{}\n".format(key, word_count[key])
    file_obj.writelines([line])
file_obj.close()

# Buchstabenhäufigkeiten:
file_obj = open(filename_chars, "w")
for key in char_count:
    line = "{};{}\n".format(key, char_count[key])
    file_obj.writelines([line])
file_obj.close()
