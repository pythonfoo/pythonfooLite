#!/usr/bin/env python3

# huepy muss vorher installiert werden.
import huepy

print(huepy.bold(huepy.red("red and bold")))

print(huepy.run("Starte..."))
print(huepy.info("Info!!"))
print(huepy.bad("Schlecht!"))
print(huepy.good("Gut!"))
input(huepy.que("Frage? "))

# mit Fortschritt:
from tqdm import tqdm

for x in tqdm(range(5000000), desc=huepy.run("Dinge")):
    pass

