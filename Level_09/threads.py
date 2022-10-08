#!/usr/bin/env python3

from threading import Thread
from time import sleep
import string
from sys import argv

"""
Man kann einen Thread erstellen, indem man threading.Thread importiert
und eine neue Klasse erstellt, die davon erbt und run überschreibt.

Man kann diesen Thread dann starten, indem man eine Instanz dieser Klasse anlegt
und start() darauf aufruft.
"""

class PrintThread(Thread):
    def __init__(self, string: str, wait: float = 0.1) -> None:
        Thread.__init__(self)
        self.string = string
        self.wait = wait
        self.daemon = True # Soll dieser Thread beendet werden beim Programmende des Haupt-Threads?

    def run(self) -> None:
        while True:
            print(self.string, end="", flush=True)
            sleep(self.wait)

"""
Alternativ kann man auch einfach eine bestimmte Methode
in einem neuen Thread ausführen ohne eine neue Klasse zu schreiben:

def fun() -> None:
    pass

Thread(target=fun).start()
"""

if len(argv) > 1:
    count = int(argv[1])
else:
    count = 2

for letter in string.ascii_uppercase[0:count]:
    PrintThread(letter).start()

while True:
    sleep(100)

# siehe auch: https://docs.python.org/3.6/library/threading.html
