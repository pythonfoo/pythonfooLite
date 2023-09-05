#!/usr/bin/env python3
"""
Dieses Programm implementiert die Cäsar-Chiffre, die schon Gaius Julius Cäsar
benutzt haben soll, um mit seinen Generälen vertraulich zu kommunizieren.
Es handelt sich dabei um eine mono-alphabetische Substitutionschiffre, das
bedeutet, jeder Buchstabe im Klartext wird durch einen anderen Buchstaben aus
dem Alphabet ersetzt, bei der Cäsar-Chiffre wird dieser zweite Buchstaben durch
Verschiebung um einen festen Wert ermittelt. Dieser feste Wert bildet dabei den
Schlüssel. https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung

Dieses Programm kümmert sich um die Verschlüsselung mit Hilfe der
Caesarchiffre, wohingegen sich caesar_encode.py um die Verschlüsselung kümmert.
"""

secret = input("Bitte den Geheimtext eingeben: \n")
key = input("Bitte die Verschiebungszahl eingaben: ")
key = int(key)

secret = secret.upper()

# An dieser Stelle wird das Alphabet durch die ASCII Werte der Buchstaben
# erzeugt
alphabet = []
for i in range(26):
    alphabet += chr(65 + i)

# Später soll in plaintext der Klartext stehen
plaintext = ""

for char in secret:
    # Falls der Buchstabe nicht in dem Alphabet vorhanden ist, wird er auch
    # nicht entschlüsselt
    if char not in alphabet:
        plaintext += char
        continue

    tmp = alphabet.index(char)
    new_char = alphabet[(tmp - key) % len(alphabet)]
    plaintext += new_char

print(plaintext)
