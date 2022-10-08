# Bugs und Fehlerbehebung
Grundsätzlich müssen drei Arten von Fehlern unterschieden werden: Syntaxfehler, Laufzeitfehler und Semantikfehler.

## Syntaxfehler
Syntaxfehler sind ähnlich zu verstehen wie Rechtschreibfehler. Ein Befehl wurde nicht richtig geschrieben, eine Zeile nicht richtig eingerückt, eine Klammer nicht geschlossen. Syntaxfehler werden dabei gemeldet, bevor das eigentliche Programm ausgeführt wird.
```
  File "bug.py", line 1
    print("Test)
               ^
SyntaxError: EOL while scanning string literal

```
Hier wurde ein String nicht beendet. Die Fehlermeldung zeigt die Datei und die Zeile an, in der der Fehler aufgetreten ist, sowie eine Meldung um was für einen Fehler es sich handelt.

```
  File "bug.py", line 2
    print("True")
        ^
IndentationError: expected an indented block
```
Hier wurde die Einrückung weggelassen, was die Fehlermeldung auch mitteilt ("IndentationError"). Zudem wird wieder die Datei und die Zeile angezeigt.


Syntaxfehler sind einfach zu beheben, da sie schnell gefunden sind und die Fehlermeldung sehr genaue Auskunft darüber gibt, was passiert ist. Viele Texteditoren bieten zudem die Funktion an offene Klammern hervorzuheben, um schon die Entstehung von leicht vermeidbaren Fehlern zu vermeiden.

## Laufzeitfehler
Laufzeitfehler finden, dem Namen nach, zur Laufzeit statt. Dabei gibt es verschiedene Fehlerquellen. Um die Fehlermeldung verständlicher zu machen werden die verschiedenen Arten von Laufzeitfehlern klassifiziert.

### ValueError

```
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    int("a")
ValueError: invalid literal for int() with base 10: 'a'

```

Hier wurde versucht den String "a" in einen Integer umzuwandeln. Spezifischer in einen Integer mit der Basis 10, welches die Standardbasis für die Umwandlung in einen integer ist. Dies ist ein Beispiel für einen `ValueError`. Diese Fehler können auftreten, wenn zum Beispiel die Nutzereingaben nicht überprüft wurden.

Laufzeitfehler zu finden ist weiterhin sehr einfach, da die Fehlermeldung sehr genau angibt, wo man zu suchen hat, weitaus schwieriger kann es allerdings werden einen Laufzeitfehler zu beheben, da dabei geklärt werden muss, ab wann das Programm den gewollten Zustand verlassen hat.

### RecursionError

```
File "<input>", line 2, in recursion
    return recursion(x+1)
RecursionError: maximum recursion depth exceeded
```

Hier wurde eine rekursive Funktion ohne Abbruchbedingung gestartet. Die wird bis zu einem Limit an Durchläufen durchlaufen und wirft dann einen `RecursionError`. Dieser ist zweifelsohne ein sehr spezieller Fehler.

## Semantikfehler
Semantikfehler sind von den beschriebenen drei Fehlerarten die weitaus schwierigste Kategorie, da sie vom Compiler oder Interpreter nicht angezeigt werden. Bei semantische Fehler, macht der Quellcode alles richtig, leider macht er nicht das, was er tun soll. Dabei sind Semantische Fehler sehr leicht zu erreichen. Wenn ich zum Beispiel in einer verschachtelten Schleife eine Anweisung in der falschen Einrückungsebene platziere, wird der Code wahrscheinlich noch funktionieren, allerdings nicht mehr das tun, was er soll. Somit ist beim Finden von Semantischen Fehlern sehr wichtig den erwarteten Output mit dem tatsächlichen Output zu vergleichen.