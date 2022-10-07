# Level 1

In Level 0 hast du Python installiert und mit `hello_world.py` dein erstes Python Programm geschrieben.
In Level 1 geht es unter anderem darum zwei grundlegende Funktionen für die Ein- und Ausgabe kennenzulernen, die Funktionen `input()` und `print()`.
Ebenso wirst du in diesem Level die einfachen Datentypen `int`, `float` und `str` kennenlernen.
Du wirst lernen Werte in Variablen zu speichern und auf diese Variablen später zuzugreifen.

Um mit diesem Level zu starten navigiere zur [Level1.ipynb](https://github.com/pythonfoo/pythonfooLite/blob/master/Level_01/Level_1.ipynb) Datei im Code Repository.
<<<<<<< HEAD
=======

## Wie gebe ich mit Python etwas aus?
Zur trivialen Ausgabe in der Konsole bietet Python die `print()`-Funktion. Diese gibt Dinge, die ihr
übergeben werden in der Konsole aus. Wie genau das funktioniert ist in dem aktuellen Lernfortschritt
noch nicht relevant. Wichtig jedoch ist, das die `print()`-Funktion in der Lage eine Vielzahl an Dingen
zu drucken. Wenn einfach nur ein Text ausgegeben werden soll, muss dieser allerdings in `""` gesetzt
werden, z.B.

    >>> print("Test")
        Test

## Wie lese ich eine Eingabe ein?
Auch für die Eingabe bietet Python eine Funktion, die `input()` Funktion. Wichtig hierbei ist: da ich die Eingabe erhalten
und speichern möchte, muss ich die Eingabe einer Variablen übergeben.

    >>> eingabe = input()
        Testeingabe
    >>> print(eingabe)
        Testeingabe
    >>> eingabe2 = input("Bitte geben Sie etwas ein: ")
        Bitte geben Sie etwas ein: Hallo
    >>> print(eingabe2)
        Hallo

## Was ist eine Variable?
Eine Variable ist eine Art Container für einen beliebigen Wert, dabei ist in Python - im Gegensatz zu vielen
anderen Programmiersprachen - egal welcher Art dieser Wert ist. Dabei kann in Python sowohl der Wert im
Container, als auch der Typ des Wertes geändert werden. Typen sind beispielsweise Zahlen, Wörter, Wahrheitswerte.
Der Wert einer Variable kann entweder im Quellcode definiert werden oder aus externen Quellen wie beispielsweise
der Konsoleneingabe, lokalen Dateien, dem Netzwerk oder einer grafischen Oberfläche kommen. Die Verwendung von
Variablen macht ein Programm flexibel, da Werte zur Laufzeit verändert werden können und Ergebnisse im Programm
für weitere Berechnungen weiterverwendet werden können.

## Was ist denn jetzt eine Funktion?
Eine Funktion ist eine Abfolge grundlegender Befehle, die eine Aufgabe ausführt. In Level 5 werden wir beleuchten, wie
man in Python eigene Funktionen schreiben kann, bis dahin werden wir uns mit den mitgelieferten Funktionen und
Methoden begnügen (wo der genaue Unterschied zwischen Funktion und Methode besteht wird ebenfalls später geklärt).
Eine Funktion kann:

* eine Eingabe entgegennehmen
* einen Rückgabewert ausliefern
* weitere Funktionen aufrufen (wird später vertieft, Stichwort Rekursion)
* Variablen manipulieren

Eine Funktion kann zum Beispiel benutzt werden, um Code mit verschiedenen Werten auszuführen. Später wird noch
genauer darauf eingegangen, wie eine Funktion funktioniert.

## Was ist ein Integer?
Eine Integer ist eine ganze Zahl, d.h. eine Zahl ohne Nachkommastellen mit beliebigen Vorzeichen. Die simplen
Rechenoperationen aus der Mathemaik sind in Python eingebaut. Es folgen ein paar Beispiele:

<<<<<<< HEAD
* Schreibe ein Programm, das den String "foo" ausgibt
* Ändere das Programm so ab, dass der String "foo" 5 mal ausgegeben wird.
* Ändere das Programm so ab, dass der String 5 mal in der selben Zeile ausgegeben wird.
* Ändere das Programm so ab, dass der Benutzer eingeben kann welcher String 5 mal in der selben
  Zeile ausgegeben werden soll.
* Ändere das Programm so ab, dass der Benutzer angeben kann, wie oft der angegebene String aus-
  gegeben werden soll.
>>>>>>> a4dd4fa (Level1.md: Mergen von Level1.md und Aufgaben)
=======
    >>> 1 + 1
	    2
	>>> 2 - 5
		-3
	>>> 3 * 4
		12
	>>> 20 / 5
		4
	>>> 2 ** 5 # 2 hoch 5
		32
	>>> 12 % 10 # 12 modulo 10
		2

Weiterhin gibt es noch Vergleichsoperatoren, die auch für andere Typen gelten:

	>>> 5 > 3
		True
	>>> 3 == 9 / 3
		True
	>>> 4 <= 2 ** 3
		False

Diese Rechenoperatoren können auch mit Variablen benutzt werden.

[weitergehende Informationen zum Thema "Operatoren"](https://github.com/pythonfoo/pythonfooLite/wiki/Operatoren)

## Was bedeutet das `#`?
Mit dem Nummernzeichen `#` kann man einen Kommentar einfügen. Nach einem `#` wird der Kompiler oder Interpreter
bis zum Ende der Zeile alles ignorieren, was es ermöglicht hier sinnvolle Kommentare hin zu schreiben. Ein
Kommentar dient dazu den Code lesbarer zu machen, damit man auch später noch nachvollziehen kann, was der Code
machen sollte. Kommentare sind somit ein Werkzeug der Dokumentation, welches das Ziel hat den Code nachvollziehbar
zu machen, damit auch andere ihn verstehen können.

    >>> sum = 1 + 2   # Zwei Zahlen werden addiert
    >>> print(sum)
        3


## Was ist ein String?
Ein String ist eine Zeichenkette. Diese Zeichenkette kann ein Wort, einen Satz, einen Text, eine Seite oder sogar
ein Buch enthalten, wichtig ist nur, dass in einem String Text enthalten ist. Dies macht den String zu eine sehr
variablen Typen. Python 3.x unterstützt Unicode, was bedeutet, dass auch Sonderzeichen und Umlaute in einem String
benutzt werden können, dies war in Python 2.x nicht der Fall. Ein String wird mit Gänsefüßschen oder Hochkommata definiert:

    >>> a = "Hallo"
    >>> b = 'Welt!'
    >>> print (a, b)
        Hallo Welt

## Schlüsselwörter
In Python gibt es Schlüsselwörter, die eine feste Bedeutung haben und daher nicht als Variablennamen verwendet werden
können. In den meisten Texteditoren, die Syntax Highligthing unterstützen werden diese Schlüsselwörter farblich
markiert.

    >>> import keyword
    >>> print(keyword.kwlist)

Gibt eine Liste von Schlüsselwörtern aus. Diese sind recht eindeutig und spezifisch. Im Allgemeinen sollte man daher auf
keine Kollisionen stoßen, wenn man seine Variablennamen so gestaltet, dass der Name aussagt, wofür die Variable verwendet wird.
>>>>>>> 798ecd1 (Revert "Level1.md: Mergen von Level1.md und Aufgaben")
