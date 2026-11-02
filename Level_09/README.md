# Level 9

Level 9 widmet sich der **objektorientierten Programmierung** (OOP). Du lernst, eigene Typen zu definieren, also Klassen zu schreiben, Objekte zu erzeugen und mit Attributen, Methoden, Vererbung und Operator-Überladung zu arbeiten.

Für dieses Level gibt es zwei Wege - such dir aus, was dir mehr liegt:

* **Zugänglich:** das Notebook [Level_9.ipynb](https://github.com/pythonfoo/pythonfooLite/blob/master/Level_09/Level_9.ipynb) führt dich an Alltagsbeispielen (Adressbuch, Quiz, Stapel und Schlangen, Bruchrechnung) durch die Konzepte. Die vollständigen Programme dazu liegen im Ordner [Beispielcode](Beispielcode).
* **Mathematisch:** die Dateien `OOP1.py`, `OOP2.py` und `Ueberladung.py` behandeln dieselben Konzepte an Beispielen wie komplexen Zahlen und Vektoren.

## Aufgaben

Zur Anwendung des Gelernten findest du hier ein paar Aufgaben. Sie bauen auf den Beispielen aus dem Notebook auf. Wie immer sind sie freiwillig - wir schauen gerne über deine Lösungen.

### 9.1 Adresse erweitern

Nimm die `Adresse`-Klasse mit Konstruktor aus dem Notebook als Ausgangspunkt.

1. Erweitere `__init__` um die Parameter `telefon` und `email`.
2. Erweitere die Methode `visitenkarte()`, sodass auch Telefonnummer und E-Mail ausgegeben werden.
3. Füge eine Methode `__str__` hinzu, die die Adresse als **eine** Zeile zurückgibt (z.B. `"Chaosdorf, Hüttenstraße 25, 40215 Düsseldorf"`). Achte auf den Unterschied: `visitenkarte()` *gibt aus* (`print`), `__str__` *gibt zurück* (`return`).

### 9.2 Klammer-Prüfer mit einem Stapel

Ein Stapel eignet sich gut, um zu prüfen, ob Klammern in einem Text korrekt geschachtelt sind (z.B. `(a[b]c)` ist korrekt, `(a[b)c]` nicht).

1. Lies eine Zeichenkette ein und benutze die `Stack`-Klasse aus dem Notebook.
2. Gehe die Zeichen durch: Bei einer öffnenden Klammer (`(`, `[`, `{`) legst du sie auf den Stapel. Bei einer schließenden nimmst du das oberste Element und prüfst, ob es die passende öffnende Klammer ist.
3. Die Klammerung ist genau dann korrekt, wenn nie eine unpassende Klammer auftaucht **und** der Stapel am Ende leer ist.

### 9.3 Bruchrechnung vervollständigen

Erweitere das Programm [`Beispielcode/bruch.py`](Beispielcode/bruch.py):

1. Ergänze `__rmul__` und `__rtruediv__`, damit auch `2 * Bruch(1, 2)` und `6 / Bruch(1, 2)` funktionieren.
2. Ergänze `__eq__`, um zwei Brüche auf Gleichheit zu vergleichen (`Bruch(1, 2) == Bruch(2, 4)` soll `True` ergeben).
3. **Freiwillig:** Ergänze `__float__`, das den Bruch in eine Fließkommazahl umwandelt.

### 9.4 Das Quiz zu deinem machen (freiwillig)

Passe [`Beispielcode/hogwarts_quiz.py`](Beispielcode/hogwarts_quiz.py) an:

1. Formuliere eigene Fragen und Antworten oder tausche das Thema komplett aus.
2. Lass den Nutzer zu Beginn wählen, wie viele Fragen gestellt werden sollen (Parameter `anzahl` von `durchführen`).
