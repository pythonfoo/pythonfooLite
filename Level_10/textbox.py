#!/usr/bin/env python3

# alles wie gehabt (siehe label.py)

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

import sys

app = QApplication(sys.argv)

"""
Jetzt wird es etwas komplizierter.
Wir haben Buttons und Eingabefelder.
"""

# erstellt ein neues Fenster
window = QWidget()

# vertikales Layout
layout = QVBoxLayout()

# Label
label = QLabel("Bitte Text eingeben und den Button drücken.", window)

# Textfeld
text = QLineEdit(window)

# Button
button = QPushButton("Hier klicken", window)

# alles ins Layout packen
layout.addWidget(label)
layout.addWidget(text)
layout.addWidget(button)

# Layout auf das Fenster anwenden
window.setLayout(layout)

# die Funktion, die beim Klick ausgeführt werden soll


def onClick() -> None:
    # die Eingabe holen
    input = text.text()
    print(f"Eingabe: {input}")
    # MessageBox erstellen
    mb = QMessageBox(QMessageBox.Information, "Titel",
                     f"Der eingegebene Text war: \n{input}", QMessageBox.Ok, window)
    # MessageBox anzeigen
    mb.show()

# Button und Funktion verbinden
button.clicked.connect(onClick)

# Alternative:
#button.clicked.connect(lambda: QMessageBox(QMessageBox.Information, "Titel", "Der eingegebene Text war: \n{}".format(text.text()), QMessageBox.Ok, window).show())

# Fenster anzeigen
window.show()

# main loop
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
