#!/usr/bin/env python3

# Listentypen:

# 2. Das Tuple:

# Ein Tuple ist eine unveränderliche und unsortierte
# Folge von Elementen.

# Ein Tuple wird über runde Klammern definiert:
Tuple = ("foo", "bar") # type: tuple
print(Tuple)

# man kann auch vorhandene Werte in Tupel umwandeln
print(tuple('foo'))

# Mit einem Index kann auf ein Element zugegriffen
# werden:
print(Tuple[0])

# Mit dem len()-Befehl lässt sich die Länge aus-
# geben:
print(len(Tuple))
