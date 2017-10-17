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
    def hello(name="World"):
        """
        Natürlich können Methoden auch Parameter haben.
        Dies funktioniert genau so wie bei Funktionen.
        """
        print("Hello, {}!".format(name))

# Die Methode aufrufen:
Hello.hello(getuser())

class SpecialNumbers:
    """
    Diese Klasse hat nur statische Attribute.
    Da dies hier Konstanten sind, sind ihre Namen großschrieben
    (https://www.python.org/dev/peps/pep-0008/#constants).
    """
    PI = 3.14
    E = 2.71

# Zugriff
print(SpecialNumbers.PI)

# Problem: Der Zugriff aus statischen Methoden auf statische Attribute ist unschön.
# (`__class__` und so)

class Calculator:
    """
    Diese Klasse hat zusätzlich zu den statischen Attributen
    auch noch zwei Instanzmethoden.
    """
    PI = 3.14
    E = 2.71

    def multiply_by_pi(self, number):
        """
        Dies ist eine Instanzmethode.
        Dies lässt sich daran erkennen, dass der erste Parameter `self` ist.
        Dieses `self` ist eine Referenz auf das aktuelle Objekt.
        Da Variablennamen nur innerhalb von Funktionen und Modulen
        aufgelöst werden, ist dies nötig.
        """
        return number * self.PI

    def multiply_by_e(self, number):
        return number * self.E

c = Calculator() # Instanziierung
print(c.multiply_by_pi(5)) # Aufruf der Methode
# Achtung: Was nicht funktioniert: Calculator.multiply_by_pi(5)

class Thing:
    """
    Auch dies ist wieder eine ziemlich nutzlose Klasse.
    Aber sie hat einen Konstruktor!
    """
    def __init__(self):
        """
        Dies ist ein Konstruktor.
        Bis auf den Namen ähnelt er anderen Instanzmethoden.
        Er wird aufgerufen, wenn die Klasse instanziert wird.
        
        Standardmäßig existiert ein leerer Konstruktor ohne Parameter.
        """
        print ("Hallo!")

Thing() # Instanziierung

class Contact:
    """ Ein Adressbucheintrag. """
    def __init__(self, name, phone, email):
        """
        Dies ist ein Konstruktor.
        Aber dieser hat Parameter.
        
        Diese Parameter werden Instanzvariablen zugewiesen.
        """
        self.name = name
        self.phone = phone
        self.email = email

c = Contact("Ich", "01234-56789", "mail@example.org")
print("Name: {}".format(c.name))
print("Telefonnummer: {}".format(c.phone))
print("E-Mail: {}".format(c.email))

class HTTPURL:
    """ Diese Klasse repräsentiert eine HTTPURL. """
    def __init__(self, url):
        self.url = url
    
    def open(self):
        webbrowser.open(self.url)
