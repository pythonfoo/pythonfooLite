# Python 2.7

Wir stellen nur aktuelle Versionen von Python vor.
Es kann allerdings sein, dass man für manche (sehr speziellen) Einsatzzwecke Python 2.7 verwenden muss.

Mit dem Erscheinen von Python 3.0 wurden einige größere Änderungen eingebracht - und die fehlen dann natürlich in 2.7. Außerdem hat die Standardbibliothek im Laufe der Zeit einige neue Module erhalten.

## Aktivieren des bereits unterstützten neuen Verhaltens

Python 2.7 unterstützt viele Änderungen in Python 3.0 schon - sie müssen nur noch aktiviert werden. Dazu müssen die folgenden zwei Zeilen an den Anfang (!) jeder Datei gepackt werden:


```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from io import open
```

(Warum unbedingt an den Anfang der Datei?
Syntaktisch ist das ein Kommentar und ein `import`-Statement, semantisch sind dies allerdings Anweisungen an den Compiler.)

Die erste Zeile sorgt dafür, dass der Quellcode als [UTF-8](http://utf8everywhere.org/) gelesen wird.
Die zweite Zeile aktiviert die neue Import-Reihenfolge, die neue Division (`/` gibt `float` zurück), die `print`-Funktion (statt einem Statement) und Unicode-Strings als Standard.
Die dritte Zeile ersetzt `open` durch das aus Python 3 bekannte.

## Dinge, die anders sind

 * `input` heißt `raw_input`
 * viele Funktionen geben Listen oder Tupel zurück statt Iteratoren (z.B. `xrange` statt `range` verwenden)
 * viele Funktionen verwenden Bytestrings statt Unicodestrings
 * Klassen müssen explizit von `object` erben
 * `int`s, `list`s und `dict`s haben eine maximale Länge (evtl. statt `int` `long` verwenden)
 * einige Dinge in der Standardlibrary wurden verschoben (siehe z.B. [diese Tabelle](https://six.readthedocs.io/#module-six.moves))
 * ...


## neue Module aus der Standardlibrary, die sich nachinstallieren lassen

 * [ipaddress](https://pypi.org/project/ipaddress/)
 * [enum34](https://pypi.org/project/enum34/)
 * ...
