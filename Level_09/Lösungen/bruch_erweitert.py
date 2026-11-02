#!/usr/bin/env python3

# Dies ist eine Beispiellösung für die Aufgabe 9.3 (Bruchrechnung vervollständigen)
# aus Level 9. Sie baut auf Beispielcode/bruch.py auf und ergänzt:
#   __rmul__, __rtruediv__ (rechtsseitige Multiplikation / Division)
#   __eq__ (Vergleich zweier Brüche)
#   __float__ (Umwandlung in eine Fließkommazahl)


class Bruch:
    def __init__(self, zähler, nenner):
        if nenner < 0:
            zähler, nenner = -zähler, -nenner
        if nenner == 0:
            raise ZeroDivisionError("Nenner eines Bruchs darf nicht Null sein")
        self.zähler = zähler
        self.nenner = nenner
        self.kürzen()

    def __repr__(self):
        return f"({self.zähler}/{self.nenner})"

    @staticmethod
    def ggt(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def kürzen(self):
        g = Bruch.ggt(self.zähler, self.nenner)
        self.zähler //= g
        self.nenner //= g

    def __add__(self, rechts):
        if isinstance(rechts, int):
            rechts = Bruch(rechts, 1)
        return Bruch(self.zähler * rechts.nenner + self.nenner * rechts.zähler,
                     self.nenner * rechts.nenner)

    def __radd__(self, links):
        return self + links

    def __mul__(self, rechts):
        if isinstance(rechts, int):
            rechts = Bruch(rechts, 1)
        return Bruch(self.zähler * rechts.zähler, self.nenner * rechts.nenner)

    def __truediv__(self, rechts):
        if isinstance(rechts, int):
            rechts = Bruch(rechts, 1)
        return Bruch(self.zähler * rechts.nenner, self.nenner * rechts.zähler)

    # --- Aufgabe 9.3.1: rechtsseitige Operatoren ---

    def __rmul__(self, links):
        # Multiplikation ist vertauschbar, also einfach __mul__ benutzen:
        return self * links

    def __rtruediv__(self, links):
        # links / self, z.B. 6 / Bruch(1, 2)
        return Bruch(links, 1) / self

    # --- Aufgabe 9.3.2: Vergleich ---

    def __eq__(self, anderer):
        if isinstance(anderer, int):
            anderer = Bruch(anderer, 1)
        if not isinstance(anderer, Bruch):
            return NotImplemented
        # Beide Brüche sind immer gekürzt -> es genügt der direkte Vergleich:
        return self.zähler == anderer.zähler and self.nenner == anderer.nenner

    def __hash__(self):
        # Wer __eq__ definiert, sollte auch __hash__ definieren, damit sich
        # Brüche z.B. in einem set verwenden lassen.
        return hash((self.zähler, self.nenner))

    # --- Aufgabe 9.3.3 (freiwillig): Umwandlung in float ---

    def __float__(self):
        return self.zähler / self.nenner


if __name__ == "__main__":
    print("2 * 1/2   =", 2 * Bruch(1, 2))        # __rmul__
    print("6 / (1/2) =", 6 / Bruch(1, 2))        # __rtruediv__
    print("1/2 == 2/4 ?", Bruch(1, 2) == Bruch(2, 4))
    print("1/2 == 1/3 ?", Bruch(1, 2) == Bruch(1, 3))
    print("float(3/4) =", float(Bruch(3, 4)))
