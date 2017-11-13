# Level 3 Aufgaben

Viele Algorithmen in der Mathematik lassen sich als Summen oder Produkte beschreiben. Diese wiederrum können mit Schleifen implementiert werden. Später werden wir allerdings noch einen anderen Weg kennenlernen solche Algorithmen zu implementieren (Rekursion). Im Folgenden soll die Benutzung von Schleifen an klassischen Beispielen geübt werden.

## Aufgabe 1: Die Fakultät
Die Fakultät einer natürlichen Zahl n ist das Produkt aller natürlichen Zahlen von 1 bis einschließlich n.
Wir schreiben:  `n! = n * n-1 * n-2 ... * 3 * 2 * 1`.
**Schreiben Sie ein Programm, das die Fakultät einer eingegebenen Zahl berechnet. Und überprüfen Sie mit Hilfe der vorgegebenen Werte**
```
3! = 6
4! = 24
6! = 720
```
** Hinweis:** Die Fakultät von n entspricht ungefähr 1,6^n, was bedeutet, das sie exponentiell wächst, weshalb aus Zeitgründen, das Programm nur mit niedrigen Zahlen getestet werden sollte.

## Aufgabe 2: Die gaußsche Summe
Die gaußsche Summe von einer natürlichen Zahl n ist die Summe aller natürlicher Zahlen von 1 bis einschließlich n. 
Wie zu sehen ist hat die gaußsche Summe große Ähnlichkeit mit der Fakultät, weshalb Sie Ihren Code nicht so stark ändern müssen. Allerdings hat die gaußsche Summe den Vorteil, dass man sie nicht iterativ berechnen muss. Gauß soll für folgende Berechnungsmethode verantwortlich sein:
`n + n-1 + n-2 ... + 3 + 2 + 1 = n*(n+1)/2 `

**Schreiben Sie ein Programm, dass die gaußsche Summe eine Zahl n iterativ und mit Hilfe der gaußschen Formel berechnet und vergleichen Sie die Ergebnisse (sollten Diskrepanzen auftreten ist Ihnen ein Fehler unterlaufen).**

## Aufgabe 3: Bubblesort
Bubblesort ist ein Sortieralgorithmus, das heißt eine Prozedur um Folgen zu sortieren.
Angenommen wir wollen eine Liste mit n Elementen, die jeweils ganze Zahlen sind, sortieren.
``` python
liste = [7, 4, 6, 2, 8, 1, 3, 5]
```
Nun vergleichen wir jeweils zwei benachbarte Elemente:
```
7 > 4
4 < 6
6 > 2
2 < 8
8 > 1
1 < 3
3 > 5
```
Wenn das vordere Element größer als das hintere Element ist, werden diese vertauscht. Bei jeder Vertauschung merken wir uns, das wir eine Vertauschung gemacht haben. Dies wird solange durchgeführt, bis es in einem Durchgang keine Vertauschung mehr gab. Dann ist die Liste sortiert.
```
0 [7, 4, 6. 2, 8, 1, 3, 5] # Vertauscht = True
1 [4, 6, 2, 7, 1, 3, 5, 8] # Vertauscht = True
2 [4, 2, 6, 1, 3, 5, 7, 8] # Vertauscht = True
3 [2, 4, 1, 3, 5, 6, 7, 8] # Vertauscht = True
4 [2, 1, 3, 4, 5, 6, 7, 8] # Vertauscht = True
5 [1, 2, 3, 4, 5, 6, 7, 8] # Vertauscht = False
```
In dem Coderepository finden Sie im Ordner Level_3 eine Datei "bubblesort.py". Diese erstellt eine Liste mit `n`Elementen und durchmischt diese, das bedeutet, dass kein Element doppelt auftauchen wird.
 **Schreiben Sie ein Programm in diese Datei, dass die Liste `unsortet_list` mit Hilfe von Bubblesort sortiert.** 