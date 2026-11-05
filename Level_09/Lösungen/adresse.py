#!/usr/bin/env python3

# Dies ist eine Beispiellösung für die Aufgabe 9.1 (Adresse erweitern) aus Level 9.


class Adresse:
    def __init__(self, name: str, strasse: str, plz: str, ort: str,
                 telefon: str = "", email: str = "") -> None:
        # telefon und email haben einen Standardwert und sind daher optional.
        self.name = name
        self.strasse = strasse
        self.plz = plz
        self.ort = ort
        self.telefon = telefon
        self.email = email

    def visitenkarte(self) -> None:
        """Gibt die Adresse formatiert aus (print)."""
        print(self.name)
        print(self.strasse)
        print(f"{self.plz} {self.ort}")
        # Telefon und E-Mail nur ausgeben, wenn sie gesetzt wurden:
        if self.telefon:
            print("Tel.:  ", self.telefon)
        if self.email:
            print("E-Mail:", self.email)

    def __str__(self) -> str:
        """Gibt die Adresse als eine einzige Zeile zurück (return)."""
        return f"{self.name}, {self.strasse}, {self.plz} {self.ort}"


chaosdorf = Adresse("Chaosdorf", "Hüttenstraße 25", "40215", "Düsseldorf",
                    email="mail@chaosdorf.de")

# visitenkarte() gibt direkt aus:
chaosdorf.visitenkarte()

print()

# __str__ gibt einen String zurück, den wir weiterverwenden können:
einzeiler = str(chaosdorf)
print(einzeiler)
