"""
Das folgende Programm ist ein einfacher Taschenrechner.

Nach dem Eingeben zweier Zahlen kann eine Operation ausgewählt werden.
Anschließend wird nach neuen Zahlen gefragt.
"""

# Für die Berechnung der Quadratwurzel wird die math Bibliothek benötigt,
# des Weiteren wird zum vorzeitigen Beenden die sys Bibliothek benötigt.
import math
import sys


def menu():
    """Zeigt ein Menü an."""
    # Zuerst eine Willkommensnachricht
    print()
    print("Dies ist ein einfacher Taschenrechner.")

    # Diese Endlosschleife wird durch Aufruf der quit Funktion beendet
    while True:
        print()
        counter = 0
        for fun in operations:
            print(f"{counter} {fun.__name__}")
            counter += 1
        print("Bitte eine Zahl für eine der Operationen angeben")
        choice = input(":")
        choice = int(choice)
        print()
        if choice < 0 or choice >= len(operations):
            print("Die Eingabe war zu groß.")
            continue
        else:
            operations[choice]()


def add():
    """
    Addiert zwei eingegebene Zahlen.

    Die Zahlen können sowohl ganze Zahlen (integer) oder Fließkommazahlen
    (float) sein.
    """
    sum1 = input("Bitte den ersten Summanden eingaben: ")
    sum2 = input("Bitte den zweiten Summanden eingeben: ")
    result = float(sum1) + float(sum2)
    print(f"{sum1} + {sum2} = {result}")


def sum():
    """
    Summiert eine Menge an Zahlen auf.

    Die Summanden können sowohl ganze Zahlen (integer) oder Fließkommazahlen
    (float) sein.
    """
    values = input("Bitte die Summanden mit Leerzeichen getrennt eingeben:\n")
    values = values.split(" ")
    result = 0.0
    for i in values:
        result += float(i)
    print(f"sum({values}) = {result}")


def product():
    """
    Multipliziert eine Menge an Zahlen auf.

    Die Faktoren können sowohl ganze Zahlen (integer) oder Fließkommazahlen
    (float) sein.
    """
    values = input("Bitte die Faktoren mit Leerzeichen getrennt eingeben:\n")
    values = values.split(" ")
    result = 1.0
    for i in values:
        result *= float(i)
    print(f"product({values}) = {result}")


def difference():
    """
    Subtrahiert eine Zahl von einer anderen.

    Minuend und Subtrahend können sowohl ganze Zahlen (integer) oder
    Fließkommazahlen (float) sein.
    """
    minu = input("Bitte den Minuenden eingeben: ")
    subt = input("Bitte den Subtrahenden eingeben: ")
    result = float(minu) - float(subt)
    print(f"{minu} - {subt} = {result}")


def quotient():
    """
    Teilt einen Divisor durch einen Dividenden.

    Dividend und Divisor können sowohl ganze Zahlen (integer), als auch
    Fließkommazahlen (float) sein. 0 oder 0.0 sind als Divisor nicht möglich.
    """
    divid = input("Bitte den Dividenden eingeben: ")
    divis = input("Bitte den Divisor eingeben: ")
    if float(divis) == 0.0:
        print("Ungültige Divisor.")
        return
    result = float(divid) / float(divis)
    print(f"{divid} / {divis} = {result}")


def modulo():
    """
    Gibt das Ergebnis einer Modulo Division zurück.

    Dividend und Divisor müssen ganze Zahlen sein. 0 ist als Divisor nicht
    möglich.
    """
    divid = input("Bitte den Dividenden eingeben: ")
    divis = input("Bitte den Divisor eingeben: ")
    if float(divis) == 0.0:
        print("Ungültige Divisor.")
        return
    result = int(divid) % int(divis)
    print(f"{divid} % {divis} = {result}")


def sqrt():
    """
    Berechnet die Quadratwurzel einer eingegebenen Zahl.

    Die Zahl kann sowohl eine ganze Zahl (integer) als auch eine Fließkommazahl
    (float) sein.
    """
    radiant = input("Bitte eine Zahl eingeben: ")
    result = math.sqrt(float(radiant))
    print(f"sqrt({radiant}) = {result}")


def power():
    """
    Berechnet eine Potenz.

    Basis und Exponent können sowohl ganze Zahlen (integer), als auch
    Fließkommazahlen (float) sein.
    """
    base = input("Bitte die Basis eingeben: ")
    exp = input("Bitte den Exponenten eingeben: ")
    result = pow(float(base), float(exp))
    print(f"{base} ^ {exp} = {result}")


def fak():
    """
    Berechnet die Fakultät einer Zahl.

    Die Zahl sollte eine positive ganze Zahl (natürliche Zahl) sein.
    """
    x = input("Bitte eine Zahl eingeben: ")
    result = 1
    for i in range(2, int(x) + 1):
        result *= i
    print(f"{x}! = {result}")


def help():
    """
    Ruft das Hilfe Menü auf.

    Das Hilfe Menü zeigt die Docstrings der einzelnen Funktionen an.
    """
    for fun in operations:
        print(fun.__name__)
        print(fun.__doc__)


def quit():
    """Beendet das Programm."""
    sys.exit(0)


# Die Funktionen für die Operationen werden in einem Tuple gespeichert
operations = (
    add,
    sum,
    product,
    difference,
    quotient,
    modulo,
    sqrt,
    power,
    fak,
    help,
    quit
)

# Durch diese Bedingung wird das Menü nur aufgerufen, wenn das Programm als
# Hauptprogramm läuft.
if __name__ == "__main__":
    menu()
