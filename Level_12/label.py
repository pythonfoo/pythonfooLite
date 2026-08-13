#!/usr/bin/env python3

# Level 9: Ein Label in einem Fenster.

"""
In diesem Level verwenden wir Qt 5 (https://www.qt.io/).
Für eine Anbindung an Python kann man PySide 2 (https://wiki.qt.io/PySide2) oder PyQT 5 verwenden.
PySide 2 ist etwas näher am "normalen" Qt für C++,
aber leider in vielen Distributionen noch nicht in den Paketquellen.
Für die aktuelle Ubuntu LTS (16.04) müsste z.B. das PPA ppa:thopiekar/pyside-git
(https://launchpad.net/~thopiekar/+archive/ubuntu/pyside-git) hinzugefügt und
das Paket "python3-pyside2" installiert werden.
Daher verwenden wir qtpy (https://github.com/spyder-ide/qtpy),
was die jeweils auf dem System installierte Bibliothek lädt.
(Achtung: Dabei kann auch noch das alte Qt 4 herausfallen!)
qtpy kann man z.B. unter Ubuntu mit dem Paket "python3-qtpy"
oder auf allen Systemen mit pip3 installieren.
"""

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

import sys

"""
Am Anfang muss ein QApplication-Objekt erstellt werden.
sys.argv wird durchgeschleift, damit Qt auf einige Parameter reagieren kann
(u.a. diese: https://doc.qt.io/qt-5/qapplication.html#QApplication).

(Die Wayland-Kompatibilität mittels "--platform wayland" bekommen wir geschenkt.)
"""

app = QApplication(sys.argv)

# Das Folgende ist einfaches "Hallo Welt!"-Beispiel.

# Zuerst erstellen wir ein QLabel mit unserem Text.
# Widgets, die kein parent haben, sind ein neues Fenster.
label = QLabel("Hallo Welt!")

# Dann zeigen wir es an.
label.show()

# Und jetzt übergeben wir die Kontrolle an die Qt-Mainloop.
app.exec_()

# für ein fortgeschrittenes Beispiel siehe textbox.py
