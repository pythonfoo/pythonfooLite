# Glossar
## Level 0:
### Programmiersprache
Eine Programmiersprache ist eine formalisierte Form um den Computer in menschenlesbarer Form Anweisungen zu geben.
Diese Anweisungen werden bei höheren Programmiersprachen vom Compiler bzw. Interpreter in eine vom Computer lesbare Sprache übersetzt. Höhere Programmiersprachen brauchen dieses Zwischenschritt um vom Computer verstanden werden zu können.
### Interpreter
Ein Interpreter ist ein Programm, dass Anweisungen in einer Programmiersprache entgegennimmt und verarbeitet. Dabei arbeitet es eine Anweisung nach der anderen ab. Somit wird der Programmcode zur Laufzeit geschrieben. Im Interpreter lassen sich sehr leicht kleine Codestücke testen.
### Compiler
Ein Compiler übersetzt Programmcode einer höheren **[Programmiersprache](#programmiersprache)** aus einer Datei in eine, vom Computer lesbare Sprache und speichert diese Übersetzung. Somit wird der Programmcode erst in eine Datei geschrieben, was es ermöglicht komplizierteren Code zu schreiben und zu schreiben. Da der Programmcode in Menschen lesbarer Form gespeichert wird, ist es möglich das Programm auf verschiedenen Systemen und an verschiedenen Zeitpunkten auszuführen.
## Level 1:
### Variable
Eine Variable zeigt auf einen **[Wert](#wert)**. Eine Variable hat immer einen Namen und einen Wert. In Python gibt es, anders als in anderen **[Programmiersprachen](#programmiersprache)**, keine Variablen mit einem festen **[Typ](#typ)**, das heißt einer Variable kann ein beliebiger Wert, mit einem beliebigen Typen zugeordnet werden. Die Arbeit mit Variablen erleichtert das Schreiben von Code stark. Zum Beispiel ist es möglich komplexe Anweisungen in kleinere Anweisungen zu kapseln und das Ergebnis dieser Anweisungen in Variablen zwischen zu speichern, dadurch wird der Code deutlich lesbarer. Durch geschickte Namenswahl einer Variable lässt sich die Lesbarkeit des Codes weiter erhöhen.
### Wert
Ein Wert ist sehr, abstrakt, ein Stück Information und in der Programmierung etwas sehr Grundlegendes. Ein Wert hat in Python immer einen **[Typen](#typ)**, der fest mit dem Wert verankert ist. So ist die `1` immer ein **[Integer](#integer)** und `True` immer ein **[Boolean](#boolean)**.
### Typ
Ein Typ wird definiert durch den Wertebereich und die möglichen Operationen, die mit **[Werten](#wert)** dieses Typs möglich sind. Zum Beispiel spezifiziert der Typ **[Integer](#integer)** den Wertebereich der ganzen Zahlen und als Operationen verschiedene Grundrechenarten und Vergleichsoperationen. Neben den Typen, die von Python mitgeliefert werden, ist es auch möglich eigene Typen zu definieren. Von veränderlichen oder dynamischen Typen spricht man, wenn das Ergebnis eines Ausdrucks den Wert verändert und keinen neuen Wert erzeugt.
### Schlüsselwort
Schlüsselwörter dienen der Strukturierung des Programmcodes und können daher nicht als Namen für **[Variablen](#variable)** verwendet werden.
### Integer
Ein Integer ist ein **[Typ](#typ)**, der von Python mitgeliefert wird und die ganzen Zahlen behandelt. Er bietet als Operationen die Grundrechenarten, sowie die Modulodivision, die Negation und Vergleichsoperationen. Ein Integer wird im Pythoncode durch die entsprechende Zahl ausgedrückt.
### Float
### String
Ein String ist ein **[Typ](#typ)**, der von Python mitgeliefert wird. Die **[Werte](#wert)** eines Strings sind Zeichenketten beliebiger Länge. In Python wird ein String durch eine Zeichenkette in doppelten `""` oder einfach `''` Anführungszeichen ausgedrückt.
### Kommentare
Kommentare dienen der Lesbarkeit des Codes und werden von **[Compiler](#compiler)** und **[Interpreter](#interpreter)** ignoriert. Kommentare können benutzt werden um den Code zu erklären und sollten nicht nur wiederholen, was der Code tut. Im Grunde sollten Kommentare die Frage nach dem "Warum?" und nicht nach dem "Was?" klären. In Python kann ein Kommentar an einer beliebigen Stelle im Code mit einem "#" bis zu Ende der Zeile eingesetzt werden.
## Level 2:
### Boolean
Der Boolean ist ein weiterer **[Typ](#typ)** der von Python mitgeliefert wird. Der Wertebereich besteht aus den beiden Werten `True` und `False`. Dabei erbt Boolean von **[Integer](#integer)**, besitzt also neben den Vergleichsoperatoren auch die Operatoren der Grundrechenarten, wobei `True` als 1 und `False` als 0 interpretiert wird. Der Ausdruck in der Definition einer **[if-Bedingung](#bedingung)** oder einer **[while-Schleife](#while-schleife)** wird in einen Boolean übersetzt und ausgewertet.
### Kommandostruktur
Eine Kommandostruktur ist essentieller Bestandteil von einer **[Programmiersprache](#programmiersprache)**, da für die meisten Programme Kommandostrukturen wie **[Bedingungen](#bedingung)** und **[Schleifen](#schleife)** zwingend benötigt werden. Eine weitere Kommandostruktur sind **[Funktionen](#funktion)**.
### Bedingung
Eine if-Bedingung nimmt einen Ausdruck entgegen, wandelt diesen in einen **[boolschen](#boolean)** **[Wert](#wert)** um und führt daraufhin einen Codeblock aus, wenn der Ausdruck `True`ergibt, andernfalls prüft es eventuelle weitere Bedingungen (`elif`) und oder oder führt den `else` Codeblock aus. Dabei sind alle weitere Bedingungen und der `else` Codeblock optional. Diese **[Kommandostruktur](#kommandostruktur)** dient dazu auf Eingaben oder andere Begebenheiten zu reagieren und ist für viele Algorithmen notwendig.
## Level 3:
### Element
Der Begriff Element wird häufig für **[Werte](#wert)** verwendet, die in einer **[Liste](#liste)** oder einem **[Tupel](#tupel)** gespeichert werden.
### Index
Als Index bezeichnet man die Position, bei 0 beginnend, eines **[Elementes](#element)** in einer **[Liste](#liste)** oder einem **[Tupel](#tupel)**.
### Liste
Eine Liste ist ein **[Typ](#typ)**, der in Python mitgeliefert wird. In einer Liste können beliebig viele **[Werten](#wert)** mit beliebigen **[Typen](#typ)** gespeichert werden. Dabei kann ein Wert beliebig häufig in der selben Liste auftreten. Ebenso können Werte verschiedenen Typs in der selben Liste gespeichert werden. Häufig werden die Werte in einer Liste als **[Elemente](#element)** bezeichnet. Auf die Elemente einer Liste wird über deren Position in der Liste (ihren **[Index](#index)**) zugegriffen. Die Zählung der Indexe beginnt dabei bei `0`, d.h. das erste Element einer Liste mit `n` Elementen hat den Index `0` und das letzte Element den Index `n-1`. Zu beachten ist, das im Gegensatz zu den Typen **[Integer](#integer)**, **[String](#string)**, **[Float](#float)** und **[Boolean](#boolean)** die Liste ein dynamischer Typ ist.
### Tupel
Ein Tupel ist ein **[Typ](#typ)**, der von Python mitgeliefert wird. Er besitzt ähnliche Eigenschaften wie der Typ **Liste**. Der markante Unterschied zwischen diesen
beiden Typen ist, dass ein Tupel unveränderlich ist, sowohl bzgl. der Anzahl der **[Elemente](#element)** als auch bezgl. der Elemente. Der Zugriff geschieht wie bei dervListe über den **[Index](#index)** eines Elements.
### Dictionary
Ein Dictionary ist ein **[Typ](#typ)**, der von Python mitgeliefert wird. Es ist ebenso wie die **[Liste](#liste)** oder das **[Tupel](#tupel)**, ein iterativer Typ. Im Gegensatz zu diesen beiden Typen wird auf ein **[Element](#element)**, dass in einem Dictionary gespeichert wird nicht über einen **[Index](#index)**, sondern über ein Schlüssel zugegriffen.
### Schleife
#### while Schleife

#### for Schleife

### Objekt

## Level 5:
### Funktion

### Rekursion

## Level 6:
### Klasse

### Modul

### Instanz

### Methode

### Attribut

## Level 7:
### Iterator

### Generator

### Decorator

## Unsortiert:
### Exception

### Syntaxfehler
