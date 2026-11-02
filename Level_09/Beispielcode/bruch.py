#!/usr/bin/env python3
"""
Bruchrechnung mit einer eigenen Klasse.

Ein Bruch besteht aus zwei ganzen Zahlen: dem Zähler (oben) und dem
Nenner (unten). Den Wert eines Bruchs erhältst Du, wenn Du den Zähler
durch den Nenner teilst.

Wir treffen die Übereinkunft, dass der Nenner immer positiv ist. Ein Bruch
mit negativem Vorzeichen hat also einen negativen Zähler.

Dieses Programm zeigt, wie man mit den "magischen" Methoden (__add__, __mul__,
...) die Rechenoperatoren +, -, *, / und ** für eigene Objekte definiert.
"""


class Bruch:
    zähler = 0
    nenner = 1

    def __init__(self, zähler, nenner):
        # Das Vorzeichen soll immer am Zähler stehen:
        if nenner < 0:
            zähler, nenner = -zähler, -nenner
        if nenner == 0:
            raise ZeroDivisionError("Nenner eines Bruchs darf nicht Null sein")
        self.zähler = zähler
        self.nenner = nenner
        self.kürzen()

    def __repr__(self):
        """Eine für Menschen lesbare Darstellung des Bruchs."""
        if self.zähler < 0:
            return "-({}/{})".format(-self.zähler, self.nenner)
        return "({}/{})".format(self.zähler, self.nenner)

    @staticmethod
    def ggt(a, b):
        """Berechnet den größten gemeinsamen Teiler nach dem Euklid-Algorithmus."""
        while b != 0:
            a, b = b, a % b
        return a

    def kürzen(self):
        """Teilt Zähler und Nenner durch ihren größten gemeinsamen Teiler."""
        ggt = self.ggt(self.zähler, self.nenner)
        self.zähler //= ggt
        self.nenner //= ggt

    def __add__(self, rechts):
        if isinstance(rechts, int):
            rechts = Bruch(rechts, 1)
        return Bruch(self.zähler * rechts.nenner + self.nenner * rechts.zähler,
                     self.nenner * rechts.nenner)

    def __neg__(self):
        return Bruch(-self.zähler, self.nenner)

    def __sub__(self, rechts):
        if isinstance(rechts, int):
            rechts = Bruch(rechts, 1)
        return Bruch(self.zähler * rechts.nenner - self.nenner * rechts.zähler,
                     self.nenner * rechts.nenner)

    def __mul__(self, rechts):
        if isinstance(rechts, int):
            rechts = Bruch(rechts, 1)
        return Bruch(self.zähler * rechts.zähler,
                     self.nenner * rechts.nenner)

    def __truediv__(self, rechts):
        if isinstance(rechts, int):
            rechts = Bruch(rechts, 1)
        return Bruch(self.zähler * rechts.nenner,
                     self.nenner * rechts.zähler)

    def kehrwert(self):
        return Bruch(self.nenner, self.zähler)

    def __radd__(self, links):
        # wird aufgerufen bei z.B. 1 + Bruch(1, 2)
        return self + links

    def __rsub__(self, links):
        return -(self - links)

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise ValueError("Bruch kann nur zu einer ganzen Zahl erhoben werden")
        if exponent == 0:
            # Ein Bruch hoch Null ist immer 1.
            return Bruch(1, 1)
        if exponent < 0:
            # Negativer Exponent: erst den Kehrwert bilden, dann potenzieren.
            return Bruch(self.nenner ** (-exponent),
                         self.zähler ** (-exponent))
        return Bruch(self.zähler ** exponent, self.nenner ** exponent)


if __name__ == "__main__":
    print("1/2 + 1/3 =", Bruch(1, 2) + Bruch(1, 3))
    print("1/2 + 1   =", Bruch(1, 2) + 1)
    print("1 + 1/2   =", 1 + Bruch(1, 2))
    print("3/4 - 1/4 =", Bruch(3, 4) - Bruch(1, 4))
    print("2/3 * 3/4 =", Bruch(2, 3) * Bruch(3, 4))
    print("(1/2) / (3/4) =", Bruch(1, 2) / Bruch(3, 4))
    print("Kehrwert von 2/3 =", Bruch(2, 3).kehrwert())
    print("(2/3) ** 3 =", Bruch(2, 3) ** 3)
    print("(2/3) ** -1 =", Bruch(2, 3) ** -1)
    print("(2/3) ** 0 =", Bruch(2, 3) ** 0)
