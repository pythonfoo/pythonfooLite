# Level 3

**ToDo:**
* Link zu Operatoren.md, wenn es um .append geht.

## Listen
Eine Liste ist eine Folge von beliebigen Objekten mit einer beliebigen Länge.
Eine Liste wird mit `[]` definiert und kann beliebige Objekte enthalten.
### Definition:
``` python
>>> a = [1, "foo", True]
```
  Viele Objekte, lassen sich mit `list()`in eine Liste umwandeln, dabei wird eine neue
  Liste erstellt.

``` python 
>>> print(list("abcd"))
	['a', 'b', 'c', 'd']
```

### Zugriff:

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


### Methoden:

#### append()

Ein Objekt kann wie folgt einer Liste hinzugefügt werden, dabei wird die Liste verändert,
so dass kein Rückgabewert benötigt wird. Das Objekt wird dabei immer hinten an die Liste
angehangen.

``` python
>>> a = [1, "foo", True]
>>> a.append(False)
>>> print(a)
	[1, "foo", True, False]
```

#### insert()
Anstatt ein Element in eine Liste einzufügen, indem man es hinten anhängt, kann man
auch bestimmen, an welchem Index ein Objekt eingefügt werden soll.
``` python
>>> a = [True, "foo", "python", "foo", "spam", 42]
>>> a.insert(0, "test")
>>> print(a)
	['test', True, 'foo', 'python', 'foo', 'spam', 42]
```

#### index()
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

#### count()

Mit `count()` wird die Anzahl eines Objektes in einer Liste gezählt, sollte das Objekt
nicht in der Liste enthalten sein, wird 0 zurückgeben.
 
``` python

>>> print(a.count("foo"))
	2
>>> print(a.count("test"))
	0
```

#### pop()
Mit der Methode pop() ist es möglich Elemente einer Liste anhand ihres Indexes zu
entfernen. Das entfernte Element wird daei zurückgegeben.
``` python
>>> a = [True, 'foo', 'python', 'foo', 'spam', 42]
>>> print(a.pop(0))
	True
>>> print(a)
	['foo','python','spam',42]
```

#### remove()
Mithilfe von remove() lassen sich Elemente einer Liste anhand ihres Objektes entfernen.
Das entfernte Element wird dabei nicht zurückgegeben.
``` python
>>> a = [True, 'foo', 'python', 'foo', 'spam', 42]
>>> a.remove(True)
>>> print(a)
	['foo', 'python', 'foo', 42]
```
#### sort()
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


## Tupel
Ein Tupel ist eine unveränderliche Folge an Elementen, die eine feste Länge besitzt.
Ein Tupel kann, genau wie eine Liste verschiedene Elemente enthalten.
Ein Tupel wird über `()` definiert.

### Definition
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

### Zugriff
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

### Methoden
Ein Tupel besitzt nur die Methoden `count()` und `index()`, welche analog
zu den Listenmethoden `count()` und `index()` funktionieren.

## Dictionary
Ein Dictionary kann man mit einem Wörterbuch vergleichen werden, einem Schlüssel wird
Wert zugeordnet. Dabei kann ein Schlüssel auf mehrere Werte weisen, aber ein Schlüssel
kann immer nur einmal verwendet werden. Bei einem Wörterbuch von Deutsch nach
Englisch, wäre das deutsche Wort der Schlüssel und die englische Übersetzung(en) die 
Werte.

## for-Schleifen

## while-Schleifen
