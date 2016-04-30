#!/usr/bin/env python3
#coding: utf-8

"""
In diesem Level verwenden wir Qt 5 (https://www.qt.io/).
Für eine Anbindung an Python nehmen wir PySide 2 (https://wiki.qt.io/PySide2).
Dies ist leider in vielen Distributionen noch in den Paketquellen.
Also für die aktuelle Ubuntu LTS (16.04) muss das PPA ppa:thopiekar/pyside-git
(https://launchpad.net/~thopiekar/+archive/ubuntu/pyside-git) hinzugefügt und
das Paket "python3-pyside2" installiert werden.
"""

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys

"""
Am Anfang muss ein QApplication-Objekt erstellt werden.
sys.argv wird durchgeschleift, damit Qt u.a. auf folgende Parameter reagieren kann:

$ konsole --help-qt
> Qt options:
>  --display <displayname>   Use the X-server display 'displayname'
>  --session <sessionId>     Restore the application for the given 'sessionId'
>  --cmap                    Causes the application to install a private color
>                            map on an 8-bit display
>  --ncols <count>           Limits the number of colors allocated in the color
>                            cube on an 8-bit display, if the application is
>                            using the QApplication::ManyColor color
>                            specification
>  --nograb                  tells Qt to never grab the mouse or the keyboard
>  --dograb                  running under a debugger can cause an implicit
>                            -nograb, use -dograb to override
>  --sync                    switches to synchronous mode for debugging
>  --fn, --font <fontname>   defines the application font
>  --bg, --background <color> sets the default background color and an
>                            application palette (light and dark shades are
>                            calculated)
>  --fg, --foreground <color> sets the default foreground color
>  --btn, --button <color>   sets the default button color
>  --name <name>             sets the application name
>  --title <title>           sets the application title (caption)
>  --testability             load the testability framework
>  --visual TrueColor        forces the application to use a TrueColor visual on
>                            an 8-bit display
>  --inputstyle <inputstyle> sets XIM (X Input Method) input style. Possible
>                            values are onthespot, overthespot, offthespot and
>                            root
>  --im <XIM server>         set XIM server
>  --noxim                   disable XIM
>  --reverse                 mirrors the whole layout of widgets
>  --stylesheet <file.qss>   applies the Qt stylesheet to the application widgets
>  --graphicssystem <system> use a different graphics system instead of the default one, options are raster and opengl (experimental)
>  --qmljsdebugger <port>    QML JS debugger information. Application must be
>                            built with -DQT_DECLARATIVE_DEBUG for the debugger to be
>                            enabled
>  --platform <platform>     The windowing system platform (e.g. xcb or wayland)

(Ja, wir bekommen die Wayland-Kompatibilität geschenkt.)
"""

app = QApplication(sys.argv)

# Das Folgende ist einfaches "Hallo Welt!"-Beispiel.

# Zuerst erstellen wir ein QLabel mit unserem Text.
label = QLabel("Hallo Welt!")

#Dann zeigen wir es an.
label.show()

#Und jetzt übergeben wir die Kontrolle an die Qt-Mainloop.
app.exec_()
