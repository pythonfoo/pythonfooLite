#!/usr/bin/env python3

# Dies ist eine Beispiellösung für die Aufgabe 2 aus Level 1:

# 1. Schreibe ein Programm, das den String "foo" ausgibt
print("foo") # Sehr ähnlich dem "hello world" Code


# 2. Ändere das Programm so ab, dass es den String "foo" 5 mal ausgibt:
print("foo")
print("foo")
print("foo")
print("foo")
print("foo")


# 3. Ändere das Programm so ab, dass der String 5 mal in der selben Zeile ausgegeben wird.
print(5*"foo")


# 4. Ändere das Programm so ab, dass interaktiv eingegeben werden kann,
#    welcher String 5 mal in der selben Zeile ausgegeben werden soll.
string = input("Welcher String soll ausgegeben werden? ")
print(5*string)


# 5. Ändere das Programm so ab, dass interaktiv eingegeben werden kann,
#    wie oft der angegebene String ausgegeben werden soll.
string = input("Welcher String soll ausgegeben werden? ")
wiederholung = input("Wie oft soll '" + string + "' ausgegeben werden? ")
# Hier wird in dem Aufruf von input() ein String zusammen gebaut

# Wie in Aufgabe 1 muss auch hier der String in einen Integer umgewandelt werden
wiederholung = int(wiederholung)

print(wiederholung*string)
