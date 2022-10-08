#!/usr/bin/env python3

# Schleifen:

# 1. Die while-Schleife:

# Im Kopf der while-Schleife steht eine Bedingung.
# Wenn die Bedingung erfüllt ist, durchläuft die while-Schleife ihren Bauch.
# Danach prüft sie erneut die Bedingung. Und das immer so weiter.
counter = 0

while counter < 10:
    counter += 1

# Endlosschleife:
"""
while True:
	print("foo")
"""

# Schleifen vorzeitig beenden

counter = 0
while counter < 4:
    counter += 1
    print(counter)
    if counter == 5:
        break
else:
    print("Die Schleife ist bis zum Ende durchgelaufen.")

# Schleifendurchläufe überspringen
counter = 0
while counter < 10:
    counter += 1
    if counter == 5:
        continue
    print(counter)
