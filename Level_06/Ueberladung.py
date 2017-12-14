""" Diese Datei zeigt Operatorüberladung. """

import math

class Punkt:
    """
    Ein Punkt in einem dreidimensionalen Koordinatensystem.
    
    Man kann ihn z.B. ausgeben lassen, vergleichen oder addieren.
    """
    
    def __init__(self, x, y, z):
        """ Ein Punkt wird erzeugt unter Angabe von drei Koordinaten: x, y und z. """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __repr__(self):
        """ die menschenlesbare Darstellung -- str und repr """
        return "({}|{}|{})".format(self.x, self.y, self.z)
    
    def __eq__(self, p):
        """ prüft auf Äquivalenz -- == """
        if hasattr(p, "x") and hasattr(p, "y") and hasattr(p, "z"):
            return self.x == p.x and self.y == p.y and self.z == p.z
        else:
            return False
    
    def __add__(self, p):
        """ addiert p und erzeugt einen neuen Punkt -- + """
        assert isinstance(p, Punkt)
        return Punkt(self.x + p.x, self.y + p.y, self.z + p.z)
    
    def __sub__(self, p):
        """ subtrahiert p und erzeugt einen neuen Punkt -- - """
        assert isinstance(p, Punkt)
        return self + -p
    
    def __neg__(self):
        """ negiert dieses Objekt -- - """
        return Punkt(-self.x, -self.y, -self.z)

class Strecke:
    """
    Eine Strecke ist eine Linie zwischen zwei Punkten.
    Sie hat keine Richtung.
    """
    
    def __init__(self, p1, p2):
        """ Eine Strecke wird erzeugt unter Angabe zweier Punkte. """
        assert isinstance(p1, Punkt)
        assert isinstance(p2, Punkt)
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        """ die menschenlesbare Darstellung -- str und repr """
        return "{} - {}".format(self.p1, self.p2)
    
    def __eq__(self, l):
        """
        prüft auf Äquivalenz -- ==
        
        Strecken haben keine Reihenfolge.
        """
        if not isinstance(l, Strecke):
            return False
        if self.p1 == l.p1 and self.p2 == l.p2:
            return True
        if self.p1 == l.p2 and self.p2 == l.p1:
            return True
        return False
    
    def __abs__(self):
        """ berechnet den Betrag -- abs """
        x = self.p1.x - self.p2.x
        y = self.p1.y - self.p2.y
        z = self.p1.z - self.p2.z
        return math.sqrt(x**2 + y**2 + z**2)
    
    def __len__(self):
        """ Berechnet die Länge. Dies muss ein int sein. -- len """
        return int(abs(self))
    
    def __gt__(self, l):
        """
        prüft auf echtes größer -- >
        
        Dies muss ein bool zurückgeben.
        
        kleiner muss nicht manuell implementiert werden.
        """
        return abs(self) > abs(l)
    
    def __ge__(self, l):
        """
        prüft auf größer oder gleich -- >=
        
        Dies muss ein bool zurückgeben.
        
        kleiner gleich muss nicht manuell implementiert werden.
        """
        return self == l or self > l

class Vektor:
    """ Ein Vektor hat eine Richtung. """
    
    def __init__(self, *args):
        if len(args) == 3: # x, y, z
            self.x = float(args[0])
            self.y = float(args[1])
            self.z = float(args[2])
        elif len(args) == 2: # p1, p2
            self.x = args[1].x - args[0].x
            self.y = args[1].y - args[0].y
            self.z = args[1].z - args[0].z
        else:
            raise NotImplementedError
    
    def __repr__(self):
        """ die menschenlesbare Darstellung -- str und repr """
        return "({}|{}|{})".format(self.x, self.y, self.z)
    
    def __eq__(self, l):
        """ Äquivalenz: Vektoren haben eine Richtung. """
        if not isinstance(l, Vektor):
            return False
        return self.x == l.x and self.y == l.y and self.z == l.z
    
    def __abs__(self):
        """ berechnet den Betrag -- abs """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __len__(self):
        return int(abs(self))
    
    def __gt__(self, l):
        return abs(self) > abs(l)
    
    def __ge__(self, l):
        return self == l or self > l
    
    def __add__(self, l):
        """ Addition """
        assert isinstance(l, Vektor)
        return Vektor(self.x + l.x, self.y + l.y, self.z + l.z)
    
    def __sub__(self, l):
        """ Subtraktion """
        assert isinstance(l, Vektor)
        return self + -l
    
    def __neg__(self):
        """ Negation """
        return Vektor(-self.x, -self.y, -self.z)
    
    def __mul__(self, faktor):
        """ Multiplikation """
        if isinstance(faktor, float) or isinstance(faktor, int):
            # Multiplikation mit einem Skalar ergibt einen neuen Vektor.
            x = self.x * faktor
            y = self.y * faktor
            z = self.z * faktor
            return Vektor(x, y, z)
        if isinstance(faktor, Vektor):
            # Multiplikation mit einem Vektor ergibt einen Skalar.
            x = self.x * faktor.x
            y = self.y * faktor.y
            z = self.z * faktor.z
            return x + y + z
        return None
    
    def __pow__(self, exp):
        """ Potenzieren - ** """
        assert isinstance(exp, int)
        assert exp > 0
        r = self
        for i in range(0, exp):
            r *= r
        return r
    
    def __iter__(self):
        """ Iterator - siehe nächstes Kapitel """
        yield self.x
        yield self.y
        yield self.z
    
    def __getitem__(self, item):
        """ Zugriff via Index """
        return tuple(self)[item]
    
