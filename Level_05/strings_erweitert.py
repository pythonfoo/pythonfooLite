#!/usr/bin/env python3

# Character escaping:
# escaping ist eine Möglichkeit Zeichen und Steuerzeichen (z.B. \n und \t) in einen
# String einzubauen
print("Tab:\t#")

# Zeichen über ihren Namen einbinden:
print("Wal: \N{WHALE}")

# Das Zeichen hinter einem \ wird entweder Steuerzeichen interpretiert oder ignoriert
print("\aabc")

# Folglich kann ein \ nicht trivial in einen String gepackt werden:
# Nicht so:
print("\0/")
# Sondern so:
print("\\0/")

# Rawstrings können kein escaping:
print(r"\n")
print(r"\0/")


# string.format()
print("Das folgende Wort wird ersetzt: '{}' Der Rest nicht.".format("blargh"))
# Auch:
print("Das folgende Wort wird ersetzt: '{} und {}' Der Rest nicht.".format("foo", "bar"))

# Zum Weiterlesen und erweitern: https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3

# String.split()
s = "a;b;cd"
l = s.split(";") # type: list
print(repr(l))
# l entspricht nun: ["a", "b", "cd"]
# Geeignet zum Parsen von .csv Dateien zum Beispiel

s = ";".join(l) # type: str
# l entspricht nun: 'a;b;cd'

# Wiederholung:
# string.split(char) Trennt den String bei jedem Auftreten von char
# string.join(list) Trennt die Liste mit String und gibt einen String zurück
