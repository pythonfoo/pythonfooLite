#!/usr/bin/env python3
"""
Der magische Hut von Hogwarts.

Ein kleines Quiz, das dich - je nach deinen Antworten - einem der vier Häuser
von Hogwarts zuordnet. Das Beispiel zeigt, wie man mit Klassen Daten (die
Fragen und Antworten) und Methoden (das Stellen der Fragen, das Auswerten)
zusammenfasst.

Starte das Programm mit:  python3 hogwarts_quiz.py
"""

import random


class Quiz:
    ergebnisse = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    fragen = []

    def __init__(self, fragen):
        super().__init__()
        self.fragen = fragen

    def durchführen(self, anzahl=None):
        if anzahl is None:
            anzahl = len(self.fragen)
        punkte = [0] * len(self.ergebnisse)
        for frage in random.sample(self.fragen, anzahl):
            antwort = frage.frage_nutzer()
            punkte[antwort] += 1
            print()
        return punkte


class Frage:
    frage = ""
    antworten = []
    zeichen = "abcdefgh"

    def __init__(self, frage, antworten):
        super().__init__()
        self.frage = frage
        self.antworten = antworten

    def __str__(self):
        return self.frage

    def __repr__(self):
        return "Frage('%s')" % self.frage

    def frage_nutzer(self):
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
