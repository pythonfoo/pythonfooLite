# Grafische Benutzeroberflächen

Es gibt wahnsinnig viele Toolkits, um grafische Anwendungen zu programmieren (z.B. GTK+ und Tk). Wir haben uns für [Qt](https://www.qt.io/) (in der Version 5) entschieden, weil die API nachvollziehbar ist und es auf sehr vielen Plattformen verfügbar ist.

Für eine Anbindung an Python nehmen wir [PySide 2](https://wiki.qt.io/PySide2).
Dies ist leider in vielen Distributionen noch nicht in den Paketquellen enthalten.
Für die aktuelle Ubuntu LTS (16.04) muss z.B. das [PPA](https://launchpad.net/~thopiekar/+archive/ubuntu/pyside-git) `ppa:thopiekar/pyside-git` hinzugefügt und
das Paket `python3-pyside2` installiert werden.

## Benötigte Module laden:

Qt besteht aus vielen einzelnen Modulen - je nach Verwendung müssen die benötigten Module zuerst geladen werden.
Dies können (je nach Einsatz) mehr oder weniger sein - diese hier sind allerdings üblich:

``` python
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
```

Für den nächsten Schritt benötigen wir zusätzlich noch das Python-Modul `sys`:

``` python
import sys
```

## `QApplication`-Objekt erstellen

Um überhaupt irgendetwas mit Qt machen zu können, brauchen wir eine Instanz von `QApplication`. (Bei reinen Konsolenanwendungen kann man auch `QCoreApplication` verwenden.)

``` python
app = QApplication(sys.argv)
```

Die Befehlszeilenparameter unseres Programms geben wir an Qt weiter, damit es auf bestimmte Parameter darin reagieren kann (u.a. [diese](https://doc.qt.io/qt-5/qapplication.html#QApplication)).

## Ein Widget erstellen:

Alle grafischen Komponenten in Qt sind `QWidgets`.

Der einfachste Fall ist ein `QLabel` - das zeigt einfach einen beliebigen Text an.

``` python
label = QLabel("Dies ist ein Text.")
label.show()
```

Normalerweise würde man dieses Label in einem Fenster mit anderen Elementen unterbringen - in diesem einfachen Fall lassen wir das aber.

## Die main loop:

Jetzt ist alles so eingerichtet, wie wir das wollen.
Wir sehen aber noch nichts.
Wieso?

Der wichtigste Teil fehlt noch:
Wir übergeben die Kontrolle des Programmablaufs an Qt:

``` python
app.exec_()
```
