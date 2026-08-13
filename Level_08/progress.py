#!/usr/bin/env python3
from time import sleep

# tqdm muss erst installiert werden.
from tqdm import tqdm, tqdm_gui

print("feste Länge:")
for x in tqdm(range(25000000)):
    pass

print("unbekannte Länge:")
for x in tqdm(x for x in range(25000000)):
    pass

print("grafisch:")
for x in tqdm_gui(range(25000000)):
    pass

print("manuell:")
progress = tqdm(total=20)
for x in range(20):
    sleep(1)
    progress.update()  # Standard-Schrittweite: 1
progress.close()

print("manuell mit with:")
with tqdm(total=10) as progress:  # with wird später erklärt.
    for x in range(20):
        sleep(0.5)
        progress.update(n=0.5)

print("geschachtelt:")
for x in tqdm(range(50)):
    for y in tqdm(range(1000)):
        sleep(0.001)
