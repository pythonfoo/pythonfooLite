#!/usr/bin/env python3
"""
Dies ist ein Beispiel für Vererbung.

Wir implementieren hier die komplexen Zahlen,
indem wir von der abstrakten Klasse numbers.Complex erben
und die relevanten Methoden schreiben.

(Wenn man einfach nur mit komplexen Zahlen rechnen möchte,
ist dieser Aufwand nicht nötig oder sinnvoll.
`complex` ist bereits in der Standardbibliothek enthalten.)

Siehe auch https://docs.python.org/3.7/library/numbers.html.

Abstrakte Klassen kann man auch selber definieren, siehe dazu:
https://docs.python.org/3/library/abc.html

Bei den Rückgabetypen ist `C` in Anführungszeichen gefasst,
weil der Typ zu den Zeitpunkt noch nicht definiert ist.
(Ab Python 3.7 wäre das nicht mehr nötig, siehe dazu PEP 563.)
"""

from numbers import Complex
from math import sqrt

__all__ = ["C"]

class C(Complex):
    """
    Komplexe Zahlen haben einen Real- und einen Imaginärteil.
    
    Sie werden häufig als a + bi geschrieben,
    wobei a der Realteil und b der Imaginärteil ist.
    
    Man kann sie sich auch als zweidimensionalen Vektorraum vorstellen, der 1 + 0i (bzw. (1, 0)) und 0 + 1i (bzw. (0, 1)) als Basisvektoren hat, d.h. eine Dimension ist der Realteil und die andere Dimension ist der Imaginärteil
    """
    real = 0 # type: float
    imag = 0 # type: float
    
    def __init__(self, real: float = 0, imag: float = 0) -> None:
        """
        Erstellt eine neue komplexe Zahl.
        
        Sowohl Real- als auch Imaginärteil können weggelassen werden,
        dann wird einfach 0 angenommen.
        """
        self.real = real
        self.imag = imag
    
    def __abs__(self) -> float:
        """
        Berechnet den Betrag einer komplexen Zahl.abs
        
        Mit der Vektordarstellung (real, imag) sollte das klar sein
         - das ist nur der Satz von Pythagoras.
        """
        return sqrt(self.real**2 + self.imag**2)
    
    def __add__(self, o: Complex) -> "C":
        """
        Addiert zwei komplexe Zahlen.
        
        Mit der Vektordarstellung sollte das klar sein:
        g = (a, b), h = (c, d), g + h = (a + c, b + d)
        """
        assert isinstance(o, Complex)
        return C(self.real + o.real, self.imag + o.imag)
    
    def __radd__(self, o: float) -> "C":
        """
        Addiert eine rationale Zahl zu einer komplexen Zahl.
        
        Hierbei ändert sich einfach nur der Realteil.
        """
        assert isinstance(o, float)
        return C(self.real + o, self.imag)
    
    def __mul__(self, o: Complex) -> "C":
        """
        Multipliziert zwei komplexe Zahlen.
        """
        assert isinstance(o, Complex)
        return C(
            real=self.real * o.real - self.imag * o.imag,
            imag=self.real * o.imag + self.imag * o.real
        )
    
    def __rmul__(self, o: float) -> "C":
        """
        Multipliziert eine rationale Zahl an eine komplexe Zahl.
        
        Hierbei ändert sich nur der Realteil.
        """
        assert isinstance(o, float)
        return C(self.real * o, self.imag)
    
    def __pow__(self, o: int) -> "C":
        """
        Potenziert eine komplexe Zahl.
        """
        assert o >= 0
        value = C(1, 1)
        for i in range(o):
            value *= self
        return value
    
    def __rpow__(self, o: float) -> "C":
        """
        Potenziert nur den Realteil.
        """
        return C(self.real ** o, self.imag)
    
    def __truediv__(self, o: Complex) -> "C":
        """
        Dividiert zwei komplexe Zahlen.
        """
        assert isinstance(o, Complex)
        return C(
            real=(self.real * o.real + self.imag * o.imag) / (o.real ** 2 + o.imag ** 2),
            imag=(self.imag * o.real - self.real * o.imag) / (o.real ** 2 + o.imag ** 2)
        )
    
    def __rtruediv__(self, o: float) -> "C":
        """
        Dividiert eine komplexe Zahl durch eine rationale Zahl.
        
        Hierbei ändert sich nur der Realteil.
        """
        return C(self.real / o, self.imag)
    
    def __eq__(self, o: object) -> bool:
        """
        Vergleicht zwei komplexe Zahlen auf Äquivalenz.
        
        Mit der Vektordarstellung sollte das klar sein:
        g = (a, b), h = (c, d), (g = h) <=> (a = c ^ b = c)
        """
        if not isinstance(o, Complex):
            return False
        return (self.real == o.real) and (self.imag == o.imag)
    
    def conjugate(self) -> "C":
        """
        Berechnet das komplexe Konjugat einer komplexen Zahl.
        """
        return C(self.real, -self.imag)
    
    def __pos__(self) -> "C":
        """
        Berechnet +x (für x eine komplexe Zahl).
        """
        return self
    
    def __neg__(self) -> "C":
        """
        Berechnet -x (für x eine komplexe Zahl).
        """
        return C(-self.real, -self.imag)
    
    def __complex__(self) -> complex:
        """
        Wandelt eine komplexe Zahl in eine complex-Instanz um.
        """
        return complex(self.real, self.imag)
    
    def __hash__(self) -> int:
        """
        Berechnet den Hashwert einer komplexen Zahl.
        
        Wichtig ist: Wenn zwei Zahlen äquivalent sind, sollen sie den gleichen Hash haben.
        
        Wir machen es uns einfach und nehmen einfach die menschenlesbare Darstellung.
        """
        return hash(repr(self))
    
    def __repr__(self) -> str:
        """
        Stellt eine komplexe Zahl menschenlesbar dar.
        
        Dies gibt die Darstellung a + b i,
        nicht die Vektordarstellung (a, b) zurück.
        """
        if self.imag >= 0:
            fstr = "{} + {}i"
        else:
            fstr = "{} - {}i"
        return fstr.format(self.real, self.imag)

if __name__ == "__main__":
    # Hier könnte Code stehen.
    pass
