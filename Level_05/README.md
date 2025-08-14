# Level 5 Aufgaben
Wie bereits in den Aufgaben zu Level 3 angekündigt bieten Funktionen eine weitere Möglichkeit Abläufe zu wiederholen. Im Gegensatz zu den Schleifen sind die Einsatzmöglichkeiten von Funktionen weitaus vielfältiger.

## Aufgabe 1: Fakultät rekursiv
Die Fakultät ist als rekursive Funktion definiert, weshalb es intuitiv sein sollte, sie als rekursive Funktion zu implementieren. In dieser Aufgabe geht es genau um diese Implementation. Schreibe eine Funktion `factorial(n: int) -> int` die eine Zahl `n` entgegen nimmt und rekursiv deren Fakultät berechnet.
Zur Erinnerung: Die Fakultät einer Zahl `n` ist gegeben durch:
```
n! = n * (n-1) mit 0! = 1
```

**Hinweis:**
Während es bei der while-Schleife keine Begrenzung gibt, was die maximale Anzahl an Durchläufen angeht, existiert für die Tiefe einer Rekursion ein Limit.
