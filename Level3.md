# Level 3

## Listen
Eine Liste ist eine Folge von beliebigen Objekten mit einer beliebigen Länge.
Eine Liste wird mit `[]` definiert und kann beliebige Objekte enthalten.

``` python
>>> a = [1, "foo", True]
```
    
Auf die Elemente einer Liste wird über deren Index zugegriffen. Das erste Element
hat den Index `0`, das Objekt an der letzten Stelle hat den Index `-1`.

``` python
>>> print(a[2])
	True
```
  
  Viele Objekte, lassen sich mit `list()`in eine Liste umwandeln, dabei wird eine neue
  Liste erstellt.

``` python 
>>> print(list("abcd"))
	['a', 'b', 'c', 'd']
```

Ein Objekt kann wie folgt einer Liste hinzugefügt werden, dabei wird die Liste verändert,
so dass kein Rückgabewert benötigt wird.

``` python
>>> a.append(False)
>>> print(a)
	[1, "foo", True, False]
```

