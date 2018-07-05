#!/usr/bin/env python3
from multiprocessing import Process
from time import sleep
from os import getpid
from sys import argv

"""
multiprocessing ist progammatisch ähnlich zu verwenden wie threading.
Das Modul heißt anders und die Klasse auch (nämlich Process).
"""

class PIDPrinter(Process):
    def __init__(self, wait: float = 0.1) -> None:
        Process.__init__(self)
        self.wait = wait
        self.daemon = True # siehe Threads
    
    def run(self) -> None:
        while True:
            print(getpid())
            sleep(self.wait)

"""
Alternativ kann man auch einfach eine bestimmte Methode
in einem neuen Prozess ausführen ohne eine neue Klasse zu schreiben:

def fun() -> None:
    pass

Process(target=fun).start()
"""

if len(argv) > 1:
    count = int(argv[1])
else:
    count = 2

for x in range(count):
    PIDPrinter().start()

while True:
    sleep(100)

# siehe auch: https://docs.python.org/3.6/library/multiprocessing.html
