# Level 3 Aufgaben

Viele Algorithmen in der Mathematik lassen sich als Summen oder Produkte beschreiben. Diese wiederrum können mit Schleifen implementiert werden. Später werden wir allerdings noch einen anderen Weg kennenlernen solche Algorithmen zu implementieren (Rekursion).

## Aufgabe 1: Die Fakultät
Die Fakultät einer natürlichen Zahl n ist das Prodiukt aller natürlichen Zahlen von 1 bis einschließlich n. Wir schreiben:** n! = n * n-1 * n-2 ... * 3 * 2 * 1 **.
**Schreiben Sie ein Programm, das die Fakultät einer eingegebenen Zahl berechnet. Und überprüfen Sie mit Hilfe der vorgegebenen Werte**
3! = 6
4! = 24
6! = 720
** Hinweis:** Die Fakultät von n entspricht ungefähr 1,6^n, was bedeutet, das sie ziemlich schnell wächst, weshalb aus Zeitgründen, das Programm nur mit niedrigen Zahlen getestet werden sollte.

## Aufgabe 2: Die gaußsche Summe
Die gaußsche Summe von einer natürlichen Zahl n ist die Summe aller natürlicher Zahlen von 1 bis einschließlich n. Wie zu sehen ist hat die gaußsche Summe große Ähnlichkeit mit der Fakultät, weshalb Sie Ihren Code nicht so stark ändern müssen. Allerdings hat die gaußsche Summe den immensen Vorteil, dass man sie nicht iterativ berechnen muss. Gauß soll für folgende Berechnungsmethode verantwortlich sein:
**n + n-1 + n-2 ... + 3 + 2 + 1 = n*(n-1)/2 **
**Schreiben Sie ein Programm, dass die gaußsche Summe eine Zahl n iterativ und mit Hilfe der gaußschen Formel berechnet und vergleichen Sie die Ergebnisse (sollten Diskrepanzen auftreten ist Ihnen ein Fehler unterlaufen).**