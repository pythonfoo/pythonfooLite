# Level 3

**ToDo:**
* Link zu Operatoren.md, wenn es um .append geht.

## Iterierbare Objekte

### Listen
Eine Liste ist eine Folge von beliebigen Objekten mit einer beliebigen Länge.
Eine Liste wird mit `[]` definiert und kann beliebige Objekte enthalten.
#### Definition:
``` python
>>> a = [1, "foo", True]
```
  Viele Objekte, lassen sich mit `list()`in eine Liste umwandeln, dabei wird eine neue
  Liste erstellt.

``` python 
>>> print(list("abcd"))
	['a', 'b', 'c', 'd']
```

#### Zugriff:

Auf die Elemente einer Liste wird über deren Index zugegriffen. Das erste Element
hat den Index `0`, das Objekt an der letzten Stelle hat den Index `-1`.

``` python
>>> a = [1, "foo", True]
>>> print(a[2])
	True
```
Alternativ kann auch auf Sequenzen einer Liste zugegriffen werden:
``` python
>>> a = [True, "foo", "python", "foo", "spam", 42]
>>> print(a[0:2]) #Zuerst den Startindex, dann den Endindex. Wichtig: Der Endwert ist exklusiv!
	[True, "foo"]
>>> print(a[0:-1:2]) # Zusätzlich kann noch eine Schrittweite angegeben werden
	[True, 'python', 'spam']
>>> print(a[:-2]) # Wenn der Startindex 0 ist, kann er weggelassen werden
	[True, 'foo', 'python', 'foo']
>>> print(a[1:]) # Wenn der Endindex -1 ist, kann er ebenfalls entfallen
	['foo', 'python', 'foo', 'spam', 42]
>>> print(a[:])
	[True, "foo", "python", "foo", "spam", 42]
```

Ob ein Objekt in einer Liste enthalten ist, kann mit dem Schlüsselwort `in`getestet werden:

``` python
>>> a = [True, "foo", "python", "foo", "spam", 42]
>>> print("foo" in a)
	True
>>> print("test" in a)
	False
```

Die Länge einer Liste / bzw. die Anzahl an Elementen bekommt man über die len() Funktion:
``` python
>>> a = [True, "foo", "python", "foo", "spam", 42]
>>> print(len(a))
	6
```


#### Methoden:

##### append()

Ein Objekt kann wie folgt einer Liste hinzugefügt werden, dabei wird die Liste verändert,
so dass kein Rückgabewert benötigt wird. Das Objekt wird dabei immer hinten an die Liste
angehangen.

``` python
>>> a = [1, "foo", True]
>>> a.append(False)
>>> print(a)
	[1, "foo", True, False]
```

##### insert()
Anstatt ein Element in eine Liste einzufügen, indem man es hinten anhängt, kann man
auch bestimmen, an welchem Index ein Objekt eingefügt werden soll.
``` python
>>> a = [True, "foo", "python", "foo", "spam", 42]
>>> a.insert(0, "test")
>>> print(a)
	['test', True, 'foo', 'python', 'foo', 'spam', 42]
```

##### index()
Sobald man weiß, das ein Objekt in der Liste enthalten ist,
liefert `index()` den Index des ersten Auftreten. Allerdings
muss das Element in der Liste enthalten sein.

``` python
>>> a = [True, "foo", "python", "foo", "spam", 42]
>>> print(a.index("foo"))
	1
>>> print(a.index("test"))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a.index("test")
ValueError: 'test' is not in list
```

##### count()

Mit `count()` wird die Anzahl eines Objektes in einer Liste gezählt, sollte das Objekt
nicht in der Liste enthalten sein, wird 0 zurückgeben.
 
``` python

>>> print(a.count("foo"))
	2
>>> print(a.count("test"))
	0
```

##### pop()
Mit der Methode pop() ist es möglich Elemente einer Liste anhand ihres Indexes zu
entfernen. Das entfernte Element wird daei zurückgegeben.
``` python
>>> a = [True, 'foo', 'python', 'foo', 'spam', 42]
>>> print(a.pop(0))
	True
>>> print(a)
	['foo','python','spam',42]
```

##### remove()
Mithilfe von remove() lassen sich Elemente einer Liste anhand ihres Objektes entfernen.
Das entfernte Element wird dabei nicht zurückgegeben.
``` python
>>> a = [True, 'foo', 'python', 'foo', 'spam', 42]
>>> a.remove(True)
>>> print(a)
	['foo', 'python', 'foo', 42]
```
##### sort()
Mithilfe von sort() lassen sich Listen alphanummerisch sortieren. Dabei wird die Liste verändert.
``` python
>>> a = ["foo", "python", "spam", "hamster", "test"]
>>> a.sort()
>>> print(a)
	['foo', 'hamster', 'python', 'spam', 'test']
>>> a = [8, 4, 23, 42, 127]
>>> a.sort()
>>> print(a)
	[4, 8, 23, 42, 127]
```


### Tupel
Ein Tupel ist eine unveränderliche Folge an Elementen, die eine feste Länge besitzt.
Ein Tupel kann, genau wie eine Liste verschiedene Elemente enthalten.
Ein Tupel wird über `()` definiert.

#### Definition
Ein Tupel kann direkt definiert werden:
``` python
>>> t = (42, "foo", False)
>>> print(t)
	(42, 'foo', False)
```
Ohne Klammern definiert werden:
``` python
>>> t = 42, "foo", False
>>> print(t)
	(42, 'foo', False)
```
Oder als Umwandlung eines anderen Objektes definiert werden:
``` python
>>> L = [42, "foo", False]
>>> t = tuple(L)
>>> print(t)
	(42, 'foo', False)
```

#### Zugriff
Der Zugriff auf die Elemente eines Tupels erfolgt, wie bei einer Liste über den
Index:
``` python
>>> t = (1, "foo", True)
>>> print(t[2])
	True
```
Alternativ kann auch auf Sequenzen eines Tupels zugegriffen werden:
``` python
>>> t = [True, "foo", "python", "foo", "spam", 42]
>>> print(t[0:2]) #Zuerst den Startindex, dann den Endindex. Wichtig: Der Endwert ist exklusiv!
	[True, "foo"]
>>> print(t[0:-1:2]) # Zusätzlich kann noch eine Schrittweite angegeben werden
	[True, 'python', 'spam']
>>> print(t[:-2]) # Wenn der Startindex 0 ist, kann er weggelassen werden
	[True, 'foo', 'python', 'foo']
>>> print(t[1:]) # Wenn der Endindex -1 ist, kann er ebenfalls entfallen
	['foo', 'python', 'foo', 'spam', 42]
>>> print(a[:])
	[True, "foo", "python", "foo", "spam", 42]
```

Das Schlüsselwort `in` und die Funktion `len()` funktionieren wie bei den Listen:
``` python
>>> t = (True, "foo", "python", "foo", "spam", 42)
>>> print("foo" in t)
	True
>>> print("test" in t)
	False
>>> print(len(t))
	6
```

#### Methoden
Ein Tupel besitzt nur die Methoden `count()` und `index()`, welche analog
zu den Listenmethoden `count()` und `index()` funktionieren.

### Dictionary
Ein Dictionary kann man mit einem Wörterbuch vergleichen werden, einem Schlüssel wird
Wert zugeordnet. Dabei können mehrere Schlüssel auf denselben Wert zeigen, aber ein
Schlüssel muss eindeutig sein, darf also nur einmal vorkommen.
#### Definition
Ein Dictionary kann man mit `{}` definieren:
``` python
>>> d = {"eins":"one", "zwei":"two"}
>>> print(d)
	{'eins':'one', 'zwei':'two'}
```
Es ist allerdings auch möglich ein Dictionary über die Funktion `dict()` zu definieren.
Dabei kann man der `dict()` Funktion eine zweidimensionale Liste der  Form: 
``` python
a = [[key, value], [key2, value2]]
```
oder ein zweidimensionales Tupel der Form:
``` python
t = ((key, value), (key2, value2))
```
übergeben um daraus ein entsprechendes Dictionary zu basteln.

#### Zugriff
Anders als bei Listen und Tupeln, wird auf ein Wert in einem Dictonary nicht über den Index
sondern über den Schlüssel zugegriffen. Praktischerweise ähnelt sich die Syntax dem 
Zugriff auf eine Liste oder ein Tupel.
``` python
>>> d = {"eins":"one", "zwei":"two", "drei":"three"}
>>> print(d["eins"])
	'one'
```
Falls der Key, auf den man zugreifen möchte nicht vorhanden ist, wird ein Fehler geworfen.
``` python
>>> d = {}
>>> d[2]
	Traceback (most recent call last):
 	 File "<input>", line 1, in <module>
    	d[2]
	KeyError: 2
```
Dies kann mit Benutzung der `get()`Methode umgangen werden:
``` python
>>> d = {}
>>> print(d.get(2))
	None
```

## Schleifen
Schleifen sind eine einfache Möglichkeit Code beliebig häufig auszuführen, was grade bei
der Implementierung der meisten Algorithmen sehr häufig benutzt wird. Python liefert nun
zwei Möglichkeiten eine Schleife zu implementieren, die for-Schleife und die while-Schleife.
Grundlegend kann man mit beiden Möglichkeiten dasselbe implementieren, jedoch macht in
verschiedenen Anwendungsfällen die eine Möglichkeit mehr Sinn als die andere.

### for-Schleifen
Die for-Schleife ist eine der beiden Schleifenarten. Bei der for-Schleife gibt es eine
Durchlaufvariable die durch ein iterierbares Objekt läuft. Die Syntax für eine for-Schleife ist
wie folgt:
``` python
>>> a = [1,2,3,4,5]
>>> for i in a:
... 	print(i)
	1
	2
	3
```
Hier bei ist `i`die Durchlaufvariable und die Liste `a` das iterierbare Objekt. 
Mit einer for-Schleife kann über folgende Objekte beispielwwiese iteriert werden:

* string
* Listen
* Tupel
* dictionary

Allerdings ist bei Dictionaries zu beachten, dass die Durchlaufvariable nur den Wert des
Keys annimmt.
``` python
>>> dictionary = {"eins":"one", "zwei":"two", "drei":"three", "vier":"four"}
>>> for german in dictionary:
 ...	print("Deutsch:", german)
 ...	print("Englisch:", dictionary[german])
	'Deutsch: eins'
	'Englisch: one'
	'Deutsch: zwei'
	'Englisch: two'
	'Deutsch: drei'
	'Englisch: three'
	'Deutsch: vier'
	'Englisch: four'	
```

#### range()
Ein häufoger Anwendungsfall für die for-Schleife sind, gerade am Anfang, Zählschleifen,
das heißt, dass ein Integer hochgezählt wird. Mit der `range()` Funktion ist es sehr einfach
möglich solche Zählschleifen zu erstellen. Die Funktion erstellt ein iterierbares Objekt, mit
dem dann über die Integer iteriert wird.
``` python
>>> r = range(5)
>>> for i in r:
...		print(i)
	0
	1
 	2
 	3
 	4
```
 
Wie zu sehen ist, ist der Endwert exklusive
Es ist allerdings auch möglich einen Startwert und eine Schrittweite anzugeben

``` python
>>> for i in range(2,11,2):
...		print(i, end="")
	2 4 6 8 10
```
Natürlich kann man auch der Startwert auch größer sein als der Endwert, dann muss aber
auch die negative Schrittweite zwingend angegeben werden.

#### break und continue
Bei for-Schleifen ist zu beachten, dass die Anzahl an Durchläufen durch die Länge des iterierbaren
Objektes bestimmt wird. Es gibt keine Möglichkeit mehr Durchläufe durchzuführen.
Falls man jedoch aus einer Schleife ausbrechen möchte, d.h. sie frühzeitig beenden kann
man das Schlüsselwort `break` benutzen. Dabei ist zu beachten, dass mit `break` nur aus
der aktuellen Schleife ausgebrochen wird. Sollte diese Schleife in einer weiteren enthalten
sein, läuft diese weiter. 
``` python
l = range(10)
>>> for i in l:
...		if i == 4:
...			break
...		print(i)
>>> print("Fertig")
	0
	1
	2
	3
	Fertig
``` 

Mit dem Schlüsselwort `continue` ist es möglich den aktuellen Durchlauf abzubrechen, um
mit dem nächsten fortzufahren.
``` python
l = range(10)
>>> for i in l:
...		if i == 4:
...			continue
...		elif i == 6:
...			continue
...		print(i)
>>> print("Fertig")
	0
	1
	2
	3
	5
	7
	8
	9
	Fertig
```

### while-Schleifen
Die while-Schleife ist die zweite Art von Schleifen in Python. Statt einer Durchlaufavariable wird
bei der while-Schleife ein boolscher Ausdruck, d.h. ein Ausdruck, der entweder `True`oder `False`
zurückgibt. Die Syntax ist die folgende:
``` python
>>> running = True
>>> while running == True:
...		print("foo")
```
Dies ist eine Endlosschleife, die unter normalen Umständen immer weiter laufen wird.
Was hinter dem `while` steht wird intern in einen boolschen Ausdruck umgewandelt, daher ist
das Vergleichen mit `True` im oberen Fall überflüssig.
Im Allgemeinen wird eine variable als boolscher Ausdruck benutzt, die dann wärend der Laufzeit
der Schleife geändert werden kann um die Laufzeit er Schleife zu beeinflussen. Bei der 
while-Schleife ist es somit, im Gegensatz zur for-Schleife, möglich die Laufzeit zu verlängern
oder zu verkürzen.
Zum Beispiel kann mit der while-Schleife sehr viel flexiblere for-Schleifen implementieren.
``` python
>>> counter = 0
>>> while counter < 3:
... 	inp = input("Eingabe: ")
... 	if inp == "exit":
... 		break
... 		print("foo")
...		counter += 1
...	print("Fertig")
	Eingabe: 3
	foo
	Eingabe: exit
	Fertig
```