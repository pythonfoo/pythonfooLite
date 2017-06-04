#!/usr/bin/env python3
import asyncio
import string
from sys import argv

# alternativ (ab Python 3.5): async def
@asyncio.coroutine
def print_string(mystring, wait=0.1):
    while True:
        print(mystring, end="", flush=True)
        yield from asyncio.sleep(wait) # alternativ (ab Python 3.5): await

"""
Die Event-Loop ist bei asyncio sehr wichtig.
Sie kontrolliert die Ausführung innerhalb des aktuellen (und meistens einzigen) Threads.
"""
loop = asyncio.get_event_loop()

if len(argv) > 1:
    count = int(argv[1])
else:
    count = 2

for letter in string.ascii_uppercase[0:count]:
    # create_task erstellt einen Task aus einer Coroutine und führt ihn aus.
    loop.create_task(print_string(letter))

try:
    # Übergibt die Kontrolle des Ablaufs an die Loop.
    loop.run_forever()
except KeyboardInterrupt: # bei Drücken von Strg+C
    loop.stop() # beende die Loop
    loop.close() # schließe die Loop

# siehe auch: https://docs.python.org/3.6/library/asyncio.html
