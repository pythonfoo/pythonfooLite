#!/usr/bin/env python3
from getpass import getuser
import webbrowser

class Simple:
    """
    Dies ist die einfachst mögliche Klasse.
    Sie hat keine Methoden, keine Attribute
    und erbt (implizit) von `object`.

    Sie ist allerdings relativ langweilig,
    weil man recht wenig mit ihr machen kann.

    Klassennamen sollten laut PEP8 in CamelCase sein
    und mit einem Großbuchstaben beginnen
    (https://www.python.org/dev/peps/pep-0008/#class-names).
    """
    pass

class HelloWorld:
    """ Diese Klasse hat eine (statische) Methode. """
    def hello_world():
        """
        Diese Methode gibt "Hello World!" auf der Konsole aus.

        Funktions- oder Methodennamen sollten laut PEP8 kleingeschrieben
        werden und evtl. mit Unterstrichen getrennt sein
        (https://www.python.org/dev/peps/pep-0008/#function-names).
        """
        print("Hello, World!")

# Die Methode aufrufen:
HelloWorld.hello_world()

class Hello:
    def hello(name: str = "World") -> None:
        """
        Natürlich können Methoden auch Parameter haben.
        Dies funktioniert genau so wie bei Funktionen.
        """
        print(f"Hello, {name}!")

# Die Methode aufrufen:
Hello.hello(getuser())

class SpecialNumbers:
    """
    Diese Klasse hat nur statische Attribute.
    Da dies hier Konstanten sind, sind ihre Namen großschrieben
    (https://www.python.org/dev/peps/pep-0008/#constants).
    """
    PI = 3.14 # type: float
    E = 2.71

# Zugriff
print(SpecialNumbers.PI)

# Problem: Der Zugriff aus statischen Methoden auf statische Attribute ist unschön.
# (`__class__` und so)

class Calculator:
    """
    Diese Klasse hat zusätzlich zu den statischen Attributen
    auch noch zwei statische Methoden.
    """
    PI = 3.14
    E = 2.71

    @classmethod
    def multiply_by_pi(cls, number):
        """
        Dies ist eine statische Methode mit Klassenreferenz.
        Dies lässt sich daran erkennen, dass der erste Parameter `cls` ist
        und an dem Dekorator `@classmethod`.
        Dieses `cls` ist eine Referenz auf die Klasse.
        Da Variablennamen nur innerhalb von Funktionen und Modulen
        aufgelöst werden, ist dies nötig.
        """
        return number * cls.PI

    @classmethod
    def multiply_by_e(cls, number):
        return number * cls.E

print(Calculator.multiply_by_pi(5)) # Aufruf der Methode

class Thing:
    """
    Auch dies ist wieder eine ziemlich nutzlose Klasse.
    Aber sie hat einen Konstruktor!
    """
    def __init__(self) -> None:
        """
        Dies ist ein Konstruktor.
        Bis auf den Namen ähnelt er anderen Instanz-Methoden.
        Er wird aufgerufen, wenn die Klasse instanziert wird.

        Standardmäßig existiert ein leerer Konstruktor ohne Parameter.
        """
        print ("Hallo!")

Thing() # Instanziierung

# Ab Python 3.7 kann man hierfür auch dataclasses benutzen:
# https://docs.python.org/3/library/dataclasses.html
class Contact:
    """ Ein Adressbucheintrag. """
    def __init__(self, name: str, phone: int, email: str) -> None:
        """
        Dies ist ein Konstruktor.
        Aber dieser hat Parameter.

        Diese Parameter werden Instanzvariablen zugewiesen.
        """
        self.name = name
        self.phone = phone
        self.email = email

    def print(self):
        """
        Druckt den Kontakt aus.
        """
        print(f"Name: {self.name}")
        print(f"Telefonnummer: {self.phone}")
        print(f"E-Mail: {self.email}")


c = Contact("Ich", "01234-56789", "mail@example.org")
c.print()

class HTTPURL:
    """ Diese Klasse repräsentiert eine HTTPURL. """
    def __init__(self, url: str) -> None:
        self.url = url

    def open(self) -> None:
        webbrowser.open(self.url)
