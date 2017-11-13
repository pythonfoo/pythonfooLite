#!/usr/bin/env python3

# Schreiben Sie ein Programm, das die Fakultät einer eingegebenen Zahl berechnet.
# Und überprüfen Sie mit Hilfe der vorgegebenen Werte 3! = 6, 4! = 24, 6! = 720

n = int(input("Bitte eine Zahl eingeben: "))

result = 1
for i in range(1, n+1):
    result = result * i # Alternativ: result *= i

print(str(n) + "! = " + str(result))


"""
# Alternativ:
counter = 1
result = 1
while counter <= n:
    result = result * counter # Alternativ: result *= counter
    counter = counter + 1 # Alternativ: counter += 1

print(str(n) + "! = " + str(result))
"""
    
