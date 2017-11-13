#!/usr/bin/env python3

# Schreiben Sie ein Programm, dass die gaußsche Summe eine Zahl n iterativ und mit Hilfe der
# gaußschen Formel berechnet und vergleichen Sie die Ergebnisse (sollten Diskrepanzen auftreten
# ist Ihnen ein Fehler unterlaufen).

n = int(input("Bitte geben Sie eine Zahl ein: "))

# Iterativ:
result_iter = 0
for i in range(1, n+1):
    result_iter += i

# Gauß
result_gauß = int(n * (n + 1) / 2)

print("Iterativ: " + str(result_iter))
print("Gauß: " + str(result_gauß))
print("Korrekt? " + str(result_iter == result_gauß))

