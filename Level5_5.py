#!/usr/bin/env python3

# Mehr Stringmethoden:
# string.format()
print("Das folgende Wort wird ersetzt: '{}' Der Rest nicht.".format("blargh"))
# Auch:
print("Das folgende Wort wird ersetzt: '{0} und {1}' Der Rest nicht.".format("foo", "bar"))

# String.split()
s = "a;b;cd"
s = s.split(";")
# l entspricht nun: ["a", "b", "cd"]
# Geeignet zum Parsen von .csv Dateien zum Beispiel

l = ";".join(s)
# l enspricht nun: 'a;b;cd'

# Wiederholung: 
# string.split(char) Trennt den String bei jedem Auftreten von char
# string.join(list) Trennt die Liste mit String und gibt einen String zurück
