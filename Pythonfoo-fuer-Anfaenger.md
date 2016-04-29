# Anfängerthemen:

Nur Python 3.x

### TODO:
* CrashCourse an den Plan anpassen und dokumentieren
* Plan ergänzen
* Aufgaben für die Level ausdenken
* Folien für die Vorträge machen (Können auch aus gut dokumentierten
Code bestehen)

### Unsortierte Notizen:
* Wir können in jeden Level theoretische und praktische
  Teile einbauen.
* Level 0-2 sollte man locker an einem Abend schaffen
* Wo setzten wir zwischen den Leveln am besten die Pausen?
* Generelle Syntax
 * Einrückung 
* Arbeiten mit Git

### Level 0:
Level 0 ist auf $Menschen ausgerichtet, die zum ersten
Mal programmieren. Deshalb werden zum Anfang ganz rudimentäre
Fragen beantwortet und Dinge geklärt.
* Was ist eine Programmiersprache?
* Was genau ist Python?
* Wie wird Python ausgeführt?
* Wie programmiere ich mit Python?

#### Aufgaben:
* Hello World

### Level 1:
Level 1 bietet den praktischen Einstieg in die Programmierung
mit Python. Dabei ist es auf dieselbe Zielgruppe
ausgerichtet wie Level 0.
* Was ist eine Variable?
* int und unäre und binäre int-Operatoren
* string und einfache string-Manipulation
* Eingabe und Ausgabe
* Kommentare
* Schlüsselwörter

#### Aufgaben:
* Addierer
* Multiplizierer
* Strings konkatinieren
* Strings multiplizieren
* `math`

### Level 2:
Level 2 führt nun in die einfachen Kontrollstrukturen ein.
* Programmablaufdiagramme
* if-Bedingungen
* boolean
* logische Operatoren

#### Aufgaben:
* einfache Passwortabfragen


### Level 3:
Level 3 beschäftigt sich nun mit einer weiteren Kommandostruktur
den Schleifen und führt zu dieser Gelegenheit 
den Datentyp der verschiedenen Listen ein.
* lists, tupel und dictionaries
* for- und while-Schleife
* `getpass`

#### Aufgaben:
* Kennwortabfragen
* Fakultät repitativ
* Potenz repitativ
* Euklid-Algorithmus repitativ
* quersumme repitativ

### Level 4:
* Dateizugriff und Dateimanipulation
* Zugriff und Parsen von Dateien
* Automatisches Generieren von Dateien
* Dateisystemzugriff
* `os`

#### Aufgaben:
* quine
* Dictionaries in .csv Dateien abspeichern

### Level 5:
Level 5 behandelt nun Funktionen und ermöglicht so das
schreiben eigener Funktionen.
* Funktionen
* Gültigkeitsbereiche
* Rekursionen
* mit und ohne Rückgabewert
* `time`

#### Aufgaben:
* Fakultät rekursiv
* Potenz rekursiv
* Euklid-Algorithmus rekursiv
* quersumme rekursiv
* Sortierfunktionen
* Ladebalken

### Level 6.1 (OOP 1):
Level 6 bildet den Abschluss der Beginnerlevel und bietet
einen rudimentären Einblick in die objektorientierte
Programmierung.
* Klassen
* Bibliotheken
* Welche Bibliotheken gibt es?
* Was ist ein `object`?
* Wie benutze ich Klassen?
* Wozu brauche ich Klassen?
* Module
* Imports
* Attribute und Methoden

### Level 6.2 (OOP 2):
* Vererbung
* Überladung
* super()
* isInstance() und is


### Level 7:
Level 7 beschäftigt sich mit Dingen, die thematisch
in andere Level gehören, aber nicht zu deren Kenntnisstand passen.
* format()
* erweiterte Stringmanipulation
* Generatoren und yield
* Decoratoren
* try, except und finally

### Exkurse:
* `turtle`
* `random`

**Folgendes ist eher fortgeschritten.**

### Level 8: Nebenläufigkeit und Alternativen
* Threads
* `multiprocessing`
* `asyncio`

### Level 9: GUI
Es gibt wahnsinnig viele Möglichkeiten,
grafische Benutzeroberflächen mit Python zu realisieren.
Wir beschränken uns hier auf Qt 5 als GUI-Toolkit.
**nur kurz anreißen!**

#### Aufgaben
Ein Hauptfenster soll einen Button und ein Textfeld
enthalten. Beim Klick auf den Button soll der Inhalt des
Textfelds in einem Dialog angezeigt werden.

### Level 10: Web
Webanwendungen sind ein häufiger Einsatzzweck von Python.
* Was ist HTTP und wie funktioniert es?
* CGI
* WSGI
* Werkzeug
* Django (/Flask?) **nur kurz anreißen!**

#### Aufgaben
* *Hallo Welt!* als Webapp
