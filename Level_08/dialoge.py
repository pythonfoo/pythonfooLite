#!/usr/bin/env python3

# pythondialog (http://pythondialog.sourceforge.net/doc/) muss vorher installiert.

from dialog import Dialog

d = Dialog()  # für Grafik: Dialog("gdialog", compat="Xdialog")

d.set_background_title("pythonfooLite")

# Messagebox
d.msgbox("Hallo Welt!")

# Auswahl
d.menu(
    "Irgendwelcher Text",
    choices={"id1": "Beschreibung", "id2": "Beschreibung"}.items(),
    title="Schwere Auswahl"
)

# vollständige Doku: http://pythondialog.sourceforge.net/doc/widgets.html
