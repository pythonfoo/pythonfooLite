#!/usr/bin/env python3
#coding: utf-8

"""
In diesem Level verwenden wir Qt 5 (https://www.qt.io/).
Für eine Anbindung an Python nehmen wir PySide 2 (https://wiki.qt.io/PySide2).
Dies ist leider in vielen Distributionen noch nicht in den Paketquellen.
Für die aktuelle Ubuntu LTS (16.04) muss z.B. das PPA ppa:thopiekar/pyside-git
(https://launchpad.net/~thopiekar/+archive/ubuntu/pyside-git) hinzugefügt und
das Paket "python3-pyside2" installiert werden.
"""

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys

"""
Am Anfang muss ein QApplication-Objekt erstellt werden.
sys.argv wird durchgeschleift, damit Qt auf einige Parameter reagieren kann
(u.a. diese: https://doc.qt.io/qt-5/qapplication.html#QApplication).

(Die Wayland-Kompatibilität mittels "--platform wayland" bekommen wir geschenkt.)
"""

app = QApplication(sys.argv)

#Das Folgende ist einfaches "Hallo Welt!"-Beispiel.

#Zuerst erstellen wir ein QLabel mit unserem Text.
#Widgets, die kein parent haben, sind ein neues Fenster.
label = QLabel("Hallo Welt!")

#Dann zeigen wir es an.
label.show()

#Und jetzt übergeben wir die Kontrolle an die Qt-Mainloop.
app.exec_()

"""
Jetzt wird es etwas komplizierter.
Wir haben Buttons und Eingabefelder.
"""

#erstellt ein neues Fenster
window = QWidget()

#vertikales Layout
layout = QVBoxLayout()

#Label
label = QLabel("Bitte Text eingeben und den Button drücken.", window)

#Textfeld
text = QLineEdit(window)

#Button
button = QPushButton("Hier klicken", window)

#alles ins Layout packen
layout.addWidget(label)
layout.addWidget(text)
layout.addWidget(button)

#Layout auf das Fenster anwenden
window.setLayout(layout)

#die Funktion, die beim Klick ausgeführt werden soll
def onClick():
	# die Eingabe holen
	input = text.text()
	print("Eingabe: {}".format(input))
	#MessageBox erstellen
	mb = QMessageBox(QMessageBox.Information, "Titel", "Der eingegebene Text war: \n{}".format(input), QMessageBox.Ok, window)
	#MessageBox anzeigen
	mb.show()

#Button und Funktion verbinden
button.clicked.connect(onClick)

#Alternative:
#button.clicked.connect(lambda: QMessageBox(QMessageBox.Information, "Titel", "Der eingegebene Text war: \n{}".format(text.text()), QMessageBox.Ok, window).show())

#Fenster anzeigen
window.show()

#main loop
app.exec_()

"""
Für mehr Informationen und komplexere Beispiele siehe die offizielle Qt-Dokumentation:
https://doc.qt.io/qt-5/reference-overview.html
(Ja, die ist auf C++ bezogen, aber das meiste lässt sich auf Python übertragen.)

Diese Anleitung benutzt Qt als QWidgets von Python aus.
In Zukunft™ sollen Qt-Anwendungen allerdings mit Qt Quick
und QML entwickelt werden (siehe https://de.wikipedia.org/wiki/QML,
https://qmlbook.github.io/, https://doc.qt.io/qt-5/qtqml-index.html).
Hierbei kann mittels PyOtherSide (https://thp.io/2011/pyotherside/)
auch Python verwendet werden - von QML aus.
"""
