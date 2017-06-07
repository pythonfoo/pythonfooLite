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
... 	print("hello world")
... 	
>>> hello_world()
	hello world
```

`def`ist ein Schlüsselwort, das zu Beginn einer Funktionsdefinition steht. Danach folgt der Funktionsname `hello_world`, für den die gleichen syntaktischen Anforderungen gelten, wie für Variablennamen, da `hello_world`in diesem Fall eine Variable ist. Demnach kann eine Funktion auch überschrieben werden, wie jede andere Variable auch. Darauf folgt eine leere runde Klammer in die Funktionsparameter eingetragen werden könnten. Darauf folgt ein Doppelpunkt und die Funktionsdeklaration ist abgeschlossen. Der darauf folgende Block ist eingerückt und muss zwangsweise Code enthalten. Nach der Funktionsdefinition wird die Funktion über ihren Namen, bzw. den Namen ihrer Variable, in dem Fall `hello_world`aufgerufen. Die runden Klammern am Ende der des Funktionsnamens stehen dabei für einen Aufruf und können eventuelle Parameter enthalten.
Diese Funktion macht aktuell noch keinen Sinn, da sie nur einen festgelegten String ("hello world") ausgeben kann.

Nun wollen wir unsere Funktion ein wenig aufpeppen, indem wir ihr einen Parameter übergeben, sodass sie beliebige Strings ausgeben kann.
``` python
>>> def new_print(text):
... 	print(text)
... 	
>>> inp_text = input("Eingabe: ")
	Testeingabe
>>> new_print(inp_text)
	Testeingabe
```
Der Parameter wurde, wie bereits erwähnt in die runden Klammern eingetragen. `text`ist nun eine Variable und steht in der Funktion zur Verfügung. Im Funktionsaufruf haben wir unserer Funktion `new_print`die Variable `inp_text` übergeben, die zu dem Zeitpunkt den String `"Testeingabe"` enthielt. Dieser String wurde nun ausgegeben.