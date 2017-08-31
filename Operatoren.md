# Operatoren

Python kennt diverse Operatoren (z.B. `+`, `-`, `*` und `/`).
Diese sind allerdings nicht in der Sprache festgelegt,
sondern sie hängen von den verwendeten Datentypen ab und werden dort definiert.
Es ist sogar möglich (und erwünscht!), sie mit eigenen Datentypen zu verwenden.

## int

Auf `int`-Werte angewandt, verhalten sich die Operatoren wie normale Rechenoperatoren.

 * `<int> + <int> -> <int>`: Die Summe der beiden Zahlen.
 * `<int> - <int> -> <int>`: Die Differenz der beiden Zahlen.
 * `<int> * <int> -> <int>`: Das Produkt der beiden Zahlen.
 * `<int> / <int> -> <float>`: Der (exakte) Quotient der beiden Zahlen.
 * `<int> // <int> -> <int>`: Der abgerundete Quotient der beiden Zahlen.
 * `<int> ** <int> -> <int>`: Die Potenz der beiden Zahlen.
 * `<int> << <int> -> <int>`: Bitshift nach links (äquivalent zu `<int> * (2 ** <int>)`)
 * `<int> >> <int> -> <int>`: Bitshift nach rechts (äquivalent zu `<int> // (2 ** <int>)`)
 * `<int> ^ <int> -> <int>`: bitweises XOR

## float

Bei `float`-Werten funktioniert das fast alles genau so wie bei `int` mit der Besonderheit,
dass alle Rückgabewerte auch `float` sind. (Dies gilt auch, wenn `int` und `float` gemischt werden.)
Außerdem funktionieren die Bitoperatoren `<<`, `>>` und `^` nicht auf floats.

## bool

Die oben beschriebenen `int`-Operationen lassen sich auch auf `bool`-Werte anwenden. Dabei gilt:

 * `True == 1`
 * `False == 0`

Außerdem gibt es auch noch weitere boolesche Operatoren:

 * `<bool> and <bool> -> <bool>`: logisches Und
 * `<bool> or <bool> -> <bool>`: logisches Oder
 * `not <bool> -> <bool>`: logisches Nicht

## str

Bei Strings ist das Verhalten auch sinnvoll, aber auf den ersten Blick evtl. anders als erwartet:

 * `<str> + <str> -> <str>`: Verkettet die beiden Strings.
 * `<str> * <int> -> <str>`: Hängt den String n-mal hintereinander. (äquivalent zu n-mal `+`)

## list

Bei Listen funktioniert das auch:

 * `<list> + <list> -> <list>`: Verkettet die beiden Listen.
 * `<list> * <int> -> <list>`: Hängt die Liste n-mal hintereinander. (äquivalent zu n-mal `+`)

## tuple

Bei Tupeln funktioniert alles genau wie bei Listen mit der Besonderheit, dass alle Rückgabewerte auch `tuple` sind.
