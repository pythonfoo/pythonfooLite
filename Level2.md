# Level 2

## Der Programmfluss
Bisher hat unser Programm einen Schritt nach den anderen ausgeführt. Man kann also sagen,
dass unsere Programme sehr linear aufgebaut waren. Daher waren die bisherigen Programme
noch sehr primitiv, da sie noch nicht auf verschiedene Eingaben mit verschiedenen Aktionen
reagieren konnten. Um dies zu ändern gibt es in den meisten Programmiersprachen sogenannte
Kontrollstrukturen, die dazu dienen einerseits dem Benutzer das Programmieren zu erleichtern,
andererseits ermöglichen diese Kontrollstrukturen aber auch erst die Formulierung komplexer
Programme, da sie es ermöglichen den Programmablauf nonlinear zu gestalten.

## Boolean
Der Boolean-Typ ist ein Datentyp, der einen Wahrheitswert enthält. Dieser kann entweder `True`
oder `False` sein.

    >>> a = True
    >>> b = False
    >>> print(a, b)
        (True, False)

Die aus der Mathematik bekannten Vergleichsoperatoren geben Booleanwerte zurück:

    >>> print(5 > 6)
        False
    >>> print(3 == 4) # WIchtig "==" entspricht dem mathematischen Operator "="
        False
    >>> print (not True)
        False
    >>> print (True != False) # a != b entspricht not(a == b)
        True

Die Vergleichsoperatoren "==", "!=", "<", ">", sowie die Kombinationen "<=" und ">=" heißen
binäre Operatoren, da sie zwei Elemente bearbeiten. Das `not` ist, ähnlich zu dem `-` in der
Mathematik ein unärer Operator, da es nur ein Element benötigt.
Mit dem Befehl `bool()`kann man Werte in einen Boolean umwandeln lassen, dabei ist zu
beachten, dass dies nur in Ausnahmefällen sinnvoll ist.

    >>> print(bool(0))
        False
    >>> print(bool(""))
        False
    >>> print(bool(1))
        True
    >>> print(bool("a"))
        False

So ist ein String immer als Boolean True, solange er nicht leer ist und ein Integer immer True,
solange er nicht `0` ist.

## Die if-Bedingung
Man stelle sich eine Passwortabfrage vor: Das Programm soll nur weiterlaufen, wenn
der Benutzer ein richtiges Passwort eingegeben hat. Dies war uns aktuell nicht möglich, da wir
noch keine Möglichkeit hatten zwei Werte miteinander zu vergleichen. Die if-Abfrage ist eine
Kontrollstruktur, die einen boolschen Ausdruck entgegen nimmt und einen Block Code nur
ausführt, wenn der boolsche Ausdruck `True` ist.

    >>> x = int(input("'Geben Sie eine Zahl ein: '"))
    >>> if x == 3:
    >>>        print(3)
        'Geben Sie eine Zahl ein:' 3
        3

Allein mit einer if-Bedingung ist schon vieles möglich, allerdings möchte der Programmierer
teilweise mehrere Fälle voneinander unterscheiden und verschieden darauf reagieren.
Dafür gibt es das Schlüsselwort `else`, dass immer am Ende einer if-Bedingung steht und nur
dann ausgeführt wird, wenn alle vorherigen Abfragen gescheitert sind.

    >>> password = input("Bitte das Passwort eingeben: ")
    >>> if password == "Geheim":
    >>>     print("Willkommen")
    >>> else:
    >>>    print("Zutritt verweigert")

Zu beachten sind bei der if-Bedingung und allgemein auch bei anderen Kontrollstrukturen die
Einrückung und die Syntax. Die Definition einer if-Bedingung ist allgemein ausgedrückt:

    if boolscher Ausdruck :
        Anweisungen
    else:
        Anweisungen

Bei der Tiefe der Einrückung liegt eine häufige Fehlerquelle, deshalb hat man sich auf 4
Leerzeichen oder einen Tab derselben Länge geeinigt. PEP8, ein Styleguide für die
Programmierung mit Python, legt 4 Leerzeichen als Einrückungstiefe fest. Egal wie viele
Leerzeichen oder Tabs du benutzt, ist es wichtig im gesamten Programm oder noch besser
in allen deinen Programmen, dabei einheitlich zu bleiben, da dies doofe Fehler vermeidet.
Viele Texteditoren bieten zudem an Tabs in Leerzeichen umzuwandeln, was den Vorteil hat,
dass man sich Schreibarbeit spart aber trotzdem PEP8 kompatibel bleibt. Zu PEP8 kommen
wir in späteren Leveln nochmal. Zusätzlich zu `if` und `else`gibt es noch die Verknüpfung von
beiden, nämlich `elif`, was für `else if ` steht.

    if Bedingung1  :
        Anweisungen1
    elif Bedingung2 :
        Anweisungen2
    else:
        Anweisungen

Eine if-Bedingung kann beliebig viele `elif`Blöcke haben, aber jeweils nur ein `if`und nur ein
`else`. `if`, `elif` und `else`sind Schlüsselwörter, was bedeutet, dass sie für if-Abfragen
reserviert sind, weshalb keine Variable if, elif oder else heißen kann.
