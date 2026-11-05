# Level 6

In Level 6 geht es um **Persistenz** und **Datenformate**: wie du strukturierte Daten dauerhaft speicherst und wieder einliest. Du lernst die drei Formate `CSV`, `JSON` und `SQLite` kennen.

Um mit diesem Level zu starten, navigiere zur [Level_6.ipynb](https://github.com/pythonfoo/pythonfooLite/blob/master/Level_06/Level_6.ipynb) Datei.

## Aufgaben

Wie in den vorherigen Leveln gibt es auch hier ein paar Aufgaben zum Üben. Zu jeder Aufgabe findest du im Ordner [Lösungen](Lösungen) eine Beispiellösung - versuche dich aber erst selbst daran. Jede Aufgabe ist in Teilaufgaben gegliedert, die das bestehende Programm Schritt für Schritt erweitern.

### 6.1 noten.py (CSV)

In dieser Aufgabe speicherst du Noten in einer CSV-Datei und wertest sie aus.

1. Lege eine Liste von Schülern an (jeweils ein Dictionary mit `name` und `note`) und schreibe sie mit `csv.DictWriter` in die Datei `noten.csv`.
2. Lies die Datei mit `csv.DictReader` wieder ein und gib für jeden Schüler eine Zeile wie `Anna hat die Note 2` aus.
3. Berechne den Notendurchschnitt und gib ihn aus. **Tipp:** Aus einer CSV-Datei kommen alle Werte als `string` zurück - zum Rechnen musst du sie erst mit `int()` umwandeln.

### 6.2 einstellungen.py (JSON)

Diese Aufgabe nutzt JSON, um auch verschachtelte Daten zu speichern.

1. Erstelle ein Dictionary mit Programm- oder Spieleinstellungen. Mindestens ein Wert soll selbst wieder ein Dictionary sein (z.B. eine Tastenbelegung unter dem Schlüssel `tasten`).
2. Speichere das Dictionary mit `json.dump` in die Datei `einstellungen.json`. Sorge dafür, dass die Datei lesbar eingerückt ist und Umlaute als Umlaute erhalten bleiben.
3. Lies die Datei mit `json.load` wieder ein und gib einen Wert aus dem **inneren** Dictionary aus (z.B. die Taste zum Springen).

### 6.3 adressbuch.py (SQLite)

Hier legst du ein kleines Adressbuch in einer SQLite-Datenbank an.

1. Öffne eine Verbindung zur Datei `adressbuch.db` und lege eine Tabelle `kontakte` mit den Spalten `name` und `telefon` an.
2. Füge mehrere Kontakte ein. Benutze dafür **unbedingt** die Platzhalter `?` und baue den Befehl nicht anders zusammen (Stichwort SQL-Injection). Vergiss das `commit()` nicht.
3. Suche mit einem `SELECT ... WHERE name = ?` nach einem bestimmten Kontakt und gib das Ergebnis aus.

**Erweiterung (freiwillig):** Frage den gesuchten Namen mit `input()` interaktiv ab.
