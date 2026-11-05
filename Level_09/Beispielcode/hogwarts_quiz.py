#!/usr/bin/env python3
"""
Der magische Hut von Hogwarts.

Ein kleines Quiz, das dich - je nach deinen Antworten - einem der vier Häuser
von Hogwarts zuordnet. Das Beispiel zeigt, wie man mit Klassen Daten (die
Fragen und Antworten) und Methoden (das Stellen der Fragen, das Auswerten)
zusammenfasst.

Starte das Programm mit:  python3 hogwarts_quiz.py
"""

# Erlaubt es, die Klasse Frage in den Typangaben von Quiz zu benutzen,
# obwohl Frage erst weiter unten definiert wird.
from __future__ import annotations

import random


class Quiz:
    ergebnisse: list[str] = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    fragen: list[Frage] = []

    def __init__(self, fragen: list[Frage]) -> None:
        self.fragen = fragen

    def durchführen(self, anzahl: int | None = None) -> list[int]:
        if anzahl is None:
            anzahl = len(self.fragen)
        punkte = [0] * len(self.ergebnisse)
        for frage in random.sample(self.fragen, anzahl):
            antwort = frage.frage_nutzer()
            punkte[antwort] += 1
            print()
        return punkte


class Frage:
    frage: str = ""
    antworten: list[str] = []
    zeichen: str = "abcdefgh"

    def __init__(self, frage: str, antworten: list[str]) -> None:
        self.frage = frage
        self.antworten = antworten

    def __str__(self) -> str:
        return self.frage

    def __repr__(self) -> str:
        return "Frage('%s')" % self.frage

    def frage_nutzer(self) -> int:
        print(self.frage)
        antw = random.sample(self.antworten, len(self.antworten))
        for zeichen, antwort in zip(self.zeichen, antw):
            print("   ", zeichen, antwort)
        eingabe = input("Deine Wahl: ")
        while eingabe not in self.zeichen[0:len(self.antworten)]:
            print("Bitte antworte mit einem der Zeichen",
                  ", ".join(self.zeichen[0:len(self.antworten)]))
            eingabe = input("Deine Wahl: ")
        position = self.zeichen.index(eingabe)
        return self.antworten.index(antw[position])


quiz = Quiz([
    Frage("Was machst Du gerne in der Freizeit?",
          ["Klettern", "Kämpfen", "Malen", "Lesen"]),
    Frage("Welchen Sport treibst Du am liebsten?",
          ["Eisschwimmen", "Judo", "Tennis", "Basketball"]),
    Frage("Was magst Du am meisten von den Weasleys?",
          ["verwandelnder Zauberstab", "Finsternispulver",
           "Muff", "Langziehohren"]),
    Frage("Was würdest Du Dir am liebsten in der Winkelgasse kaufen?",
          ["Besen", "Zauberstab", "Hogwartsumhang", "Buch"]),
    Frage("Wen magst Du am liebsten?",
          ["Neville", "Draco", "Cedric", "Luna"]),
    Frage("Welchen Lehrer magst Du am liebsten?",
          ["McGonagall", "Snape", "Sprout", "Flitwick"]),
])

if __name__ == "__main__":
    ergebnis = quiz.durchführen()
    höchstpunkte = max(ergebnis)
    häuser = [quiz.ergebnisse[i] for i in range(len(ergebnis))
              if ergebnis[i] == höchstpunkte]
    if len(häuser) > 1:
        print("Hmm, das ist nicht einfach.")
    print("Du kommst nach", random.choice(häuser), ".")
