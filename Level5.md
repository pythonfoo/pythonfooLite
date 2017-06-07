# Level 5: Funktionen
Mit Hilfe von Funktionen ist es möglich Codeabschnitte bzw. kleinere Programmteile zu speichern und wiederzuverwenden. So wird die Komplexität stark reduziert.
Durch Funktionen muss du dich beim Schreiben eines Hello-World-Programms nicht erst mit der Kommunikation mit dem System Output kümmern oder um die Dekodierung deiner Eingabe. Du kannst einfach die print() Funktion benutzen, die alles wichtige für dich erledit, sodass du nur noch Text eingeben musst.
Python liefert nun eine ganze Menge grundlegender Funktionen mit, was dir die Arbeit unglaublich erleichtert. Viele dieser Funktionen haben wir bereits in den vorherigen Leveln behandelt und sie auch als Funktionen bezeichnet, ohne näher darauf einzugehen.
Beispiele für diese grundlegenden Funktionen sind:

* `print()`
* `len()`
* `input()`

Aber auch viele Funktionen, die zu einem Objekt gehören (solche Funktionen nennen wir "Methoden", dazu mehr im nächsten Level):

* `list.append()`
* `list.count()`
* `list.pop()`

Um aber nicht auf die Menge der mitgelieferten oder aus Drittquellen bezogenen (auch dazu mehr im nächsten Level) Funktionen beschränkt zu sein, bietet Python wie viele andere Programmiersprachen, die Möglichkeit eigene Funktionen zu definieren. Dadurch kann ich kleine Teile des Programms vorhalten und sie genau dann benutzen, wenn ich sie brauche.
Der Name Funktion maf andeuten, dass es sich dabei um etwas ähnliches wie eine mathematische Funktion handelt, das ist jedoch nur zum Teil richtig. Wärend eine mathematische Funktion einen festen Definitionsbereich besitzt, der aus mathematischen Objekten beruht, nimmt eine Funktion in Python beliebige Objekte entgegen und verarbeitet diese. Mit einer Pythonfunktion kann ich beliebiege mathematisch Funktionen definieren, andersherum ist das deutlich schwieriger. Die Analogie des Ablaufs oder der Prozedur ist daher eventuell angebrachter. Wir werden im folgenden trotzdem den Begriff Funktion verwenden.

## Die Funktionsdefinition
Im Folgenden wollen wir eine Funktion definieren, die genau das macht was ein Hello-World-Programm auch macht: "Hello World" ausgeben

``` python
>>> def hello_world():
...     print("hello world")
... 
>>> hello_world()
    hello world
```

`def`ist ein Schlüsselwort, das zu Beginn einer Funktionsdefinition steht. Danach folgt der Funktionsname `hello_world`, für den die gleichen syntaktischen Anforderungen gelten, wie für Variablennamen, da `hello_world`in diesem Fall eine Variable ist. Demnach kann eine Funktion auch überschrieben werden, wie jede andere Variable auch. Darauf folgt eine leere runde Klammer in die Funktionsparameter eingetragen werden könnten. Darauf folgt ein Doppelpunkt und die Funktionssignatur ist abgeschlossen. Der darauf folgende Block ist eingerückt und muss zwangsweise Code enthalten. Nach der Funktionsdefinition wird die Funktion über ihren Namen, bzw. den Namen ihrer Variable, in dem Fall `hello_world`aufgerufen. Die runden Klammern am Ende der des Funktionsnamens stehen dabei für einen Aufruf und können eventuelle Parameter enthalten.
Diese Funktion macht aktuell noch keinen Sinn, da sie nur einen festgelegten String ("hello world") ausgeben kann.

Nun wollen wir unsere Funktion ein wenig aufpeppen, indem wir ihr einen Parameter übergeben, sodass sie beliebige Strings ausgeben kann.
``` python
>>> def new_print(text):
...     print(text)
... 
>>> inp_text = input("Eingabe: ")
    Testeingabe
>>> new_print(inp_text)
    Testeingabe
```
Der Parameter wurde, wie bereits erwähnt in die runden Klammern eingetragen. `text`ist nun eine Variable und steht in der Funktion zur Verfügung. Im Funktionsaufruf haben wir unserer Funktion `new_print`die Variable `inp_text` übergeben, die zu dem Zeitpunkt den String `"Testeingabe"` enthielt. Dieser String wurde nun ausgegeben.

## Rückgabewerte

In den meisten Anwendungsfällen wollen wir das Ergebnis einer Funktion allerdings nicht ausgeben, sondern zum Beispiel in einer Variabeln speichern können, um es später verwenden zu können. Dafür benötigt unsere Funktion einen Rückgabewert. Mit Hilfe eines Rückgabewertes kann eine Funktion ein Objekt beliebigen Typs zurückgeben, damit es weiter benutzt werden kann. Die folgende Funktion hat nun einen anderen Anwendungsfall verfügt jedoch über einen Übergabeparameter und einen Rückgabewert.

``` python
>>> def square(x):
...     return x**2
...
>>> print( square(5) )
    25
```

Die Funktion `square` nimmt einen Parameter entgegen  (sollte dieser weder `int` noch `float` sein, wird ein Fehler geworfen). Dieser wird nun erst quadriert und danach über das Schlüsselwort `return` zurückgegeben. Wichtig zu beachten ist, dass alles, was nach einem `return` in der selben Einrückungsebene steht, nicht mehr ausgeführt wird. Folglich kann es in einem Einrückungsblock nur ein `return` geben (natürlich kann man mehr hinschreiben, diese werden jedoch nicht ausgeführt werden und sind daher sinnlos). Ein `return`beendet also die Definition einer Funktion. Der Rückgabewert einer Funktion kann nun entweder direkt verwendet werden (wie oben im Beispiel) oder in einer Variable abgespeichert werden um später benutzt zu werden. Ebenfalls wichtig zu beachten ist, dass mit `return`immer nur ein Objekt zurückgegeben werden kann. Falls man mehrere Objekte zurückgeben möchte, sollte man sie in eine Liste, Tupel oder Dictionary packen.

## args und kwargs
Bisher können wir einer Funktion einen Parameter geben und einen Rückgabewert zurückgeben lassen. Allerdings benötigen viele Anwendungsfälle Funktionen, die mehrere Objekte entgegen nehmen können, d.h. die mehrere Parameter haben können. Nun wäre der naive Ansatz, der schon bei Rückgabewerten benutzt wurde, statt mehreren Parametern eine Liste von Parametern zu übergeben. Praktischerweise ist in Python dieser Ansatz implementiert. Zuerst wollen wir aber zwei verschiedene Fälle unterscheiden:

1. Die Menge an Parametern ist fest.
2. Die Menge an Parametern ist variabel

Diese Unterscheidung ist sehr wichtig, da die Verwendung von mehreren Parametern sich danach unterscheidet.

``` python
>>> def diff(a, b):
...     return a - b
... 
>>> print(5, 3)
    2
>>> print(3, 5)
    -2
```
Wenn ich eine feste Anzahl an Parametern benutzen möchte, kann ich diese in der Signatur auflisten. Wichtig ist dabei, dass beim Aufruf die Reihenfolge entscheidend ist. Die obige Funktion subtrahiert das Objekt der Variable `b` von dem Objekt der Variable `a`, daher sind `a` und `b` idealerweise ganze Zahlen oder Fließkommazahlen. Beim Aufruf wird das n-te Element im Aufruf dem n-ten Element der Signatur zugeordnet (hier kann man die Benutzung einer Liste oder eines Tupels erkennen).

Nun möchte ich aber einer Funktion eine beliebige Anzahl an Parametern übergeben, weil ich zum Beispiel nicht weiß, wie viele Parameter zur Laufzeit benötigt werden.

``` python
>>> def string_add(*elemente):
...     result = "" 
...     for e in elemente:
...         result += str(e)	
...     return result
...
>>> print( string_add(0, 1, "test"))
    01test
```
