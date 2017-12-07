# Rekursion Vs. Iteration
## Einleitung
Zum Anfang betrachten wir, was genau Rekursion ist. Im Grunde ist Rekursion
nämlich nur ein Sprachfeature, dass eine Funktion sich selber aufrufen kann.
Jedoch ist eine Programmiersprache auch ohne Rekursion Turing komplett, d.h. ich
kann jedes Programm auch ohne Rekursion implementieren. Das wird unter anderem
dadurch deutlich, dass eine rekursive Funktion beim Übersetzen in Maschinencode
als Schleife ausgeführt wird. Zusammenfassend kann man also sagen:

> Alles was sich iterativ implementieren lässt, lässt sich auch rekursiv
> implementieren und anders herum.

Rekursion bietet sich an, da viele Algorithmen rekursiv definiert sind und daher
rekursiv leichter zu implementieren sind als iterativ. Damit ist jedoch nicht
gesagt, dass die rekursive Implementierung die effizientere ist.
Ein einfaches Beispiel dafür sind die Fibonacci-Zahlen.

## Die Fibonacci-Zahlen
Die Fibonacci-Zahlen tauchen in der Natur auf und sind eine relativ schnell
wachsende Zahlenfolge, die folgendermaßen definiert ist:
```
fib(0) = 1
fib(1) = 1
fib(n) = fib(n-2) + fib(n-1)
```
### Einfache rekursive Implementierung

Die Definition ist eindeutig rekursiv, folglich wäre der simpelste Ansatz diese
Zahlenfolge zu implementieren die folgende:
``` python
def fibR(n): # Fibonacci Rekursiv
	if n == 0 or n == 1:
		return 1
	return fibR(n-2) + fibR(n-1)
```

### Probleme

Dieser Code funktioniert, ist leicht zu lesen hat aber einige Nachteile:
#### Rekursionslimit
Der Rekursion ist ein Limit gesetzt, weshalb der Code bei größeren Zahlen in
einen `RecursionError`laufen wird. In diesem Fall passiert dies schon sehr früh,
weil es zwei rekursive Aufrufe in der Funktion gibt.
#### Laufzeit
Das weitaus größere Problem ist die Laufzeit, denn dadurch, dass fibR(n-2) und
fibR(n-1) aufgerufen werden, wird fibR() immer häufiger aufgerufen:
```
n = 5
fibR(5) wird 1 mal aufgerufen
fibR(4) wird 1 aufgerufen
fibR(3) wird 2 mal aufgerufen
fibR(2) wird 3 mal aufgerufen
fibR(1) wird 5 mal aufgerufen
fibR(0) wird 8 mal aufgerufen
```
Wenn man sich die Anzahl der Aufrufe genau anschaut, stellt man fest dass es
sich um die Fibonaccifolge handelt. Die rekursive Implementation berechnet also
ihre eigene Laufzeit. Da die Fibonaccifolge aber relativ schnell wächst, wächst
auch die Laufzeit relativ schnell.

### Lösung
Da jeder Algorithmus sowohl rekursiv, als auch iterativ implementiert werden
kann und die rekursive Implementation Probleme aufwieß, versuchen wir jetzt die
Fibonacci Folge iterativ zu implementieren:
```
def fibI(n): # Fibonacci Iterativ
	last = 1
	current = 1
	for i in range(0,n):
		current, last = current + last, current
	return current
```
Diese Funktion implementiert die Folge iterativ, läuft daher nicht in einen
`RecursionError` benötigt `n` Durchläufe der Schleife, ist also deutlich
schneller als die rekursive Implementierung.

### Fazit
Die beiden gezeigten Implementierungen eines einfachen Problems, waren ungefähr
gleich komplex, haben sich aber in der Laufzeit stark unterschieden.
Beide Möglichkeiten der Implementation haben jedoch ihre Vorzüge, weshalb im
Einzelfall entschieden werden muss, mit welcher Methode ein Algorithmus
implementiert wird.
