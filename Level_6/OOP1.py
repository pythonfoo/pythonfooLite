'''
Objektorientierte Programmierung mit Python:

1. Was ist eine Klasse?
Eine Klasse ist ein Objekt. Sie besitzt Eigenschaften (Attribute) und
Funktionen (Methoden). Wenn wir uns den Hund als Klasse vorstellen hätte er
beispielsweise...

Die Attribute:
* Fellfarbe
* Augenfarbe
* Name
* Schulterhöhe
* Alter
* Rasse
* Hunger
* Müdigkeit
* usw.

und die Methoden:
* bellen
* Frisbee fangen
* futtern
* schlafen
* laufen
* rennen
* springen
* usw.

Wie man sieht, beschreiben Attribute Zustände oder Eigenschaften.
Methoden beschreiben stattdessen Abläufe oder Vorgänge.

Bei einer Klasse können Methoden auf Attribute zugreifen und diese verändern.
Zum Beispiel senkt die Methode <essen> das Attribut <Hunger> des Hundes und
die Methode <schlafen> das Attribut <Müdigkeit>.

Ein Attribut hat immer einen Typ. Dieser muss natürlich nicht beibehalten
werden, aber es ist schon sinnvoll die Typen der Attribute kohärent zu
lassen, um sie besser verarbeiten zu können. So ist es beispielsweise
wenig sinnvoll, dem Attribut <Schulterhöhe> eine Liste zuzuordnen.

'''




# Definition einer Klasse:

class foo():

	pass

f = foo()


# Definition einer Klasse mit Initialisierungsmethode:

class foo():

	def __init__(self):

		pass

f = foo()

# Funktion innerhalb einer Klasse: "Methode"
# Funktion außerhalb einer Klasse: "Funktion"



# Übergabeparameter der __init__() Methode:

class foo():

	def __init__(self, x):

		print(x)

x = input(":")
f = foo(x)


# Definition eines Attributes:

class foo():

	def __init__(self, x):

		self.x  = x
		print(self.x)

x = input(":")
foo(x)



# get- und set-Methoden:

class foo():

	def __init__(self, x):

		self.x = x


	def set_x(self, tmp_x):
		self.x = tmp_x


	def get_x(self):
		return self.x

x = input(":")
f = foo(x)

"""
Da Python keine privaten Variablen hat, ist es theoretisch möglich,
auf eingebaute Methoden und Attribute eingebauter Klassen zuzugreifen.
Es hat sich als Standard entwickelt, dass Methoden, die nur für den
internen Gebrauch in der Klasse bestimmt sind, mit zwei "_" vor und
hinter dem Namen deklariert werden z.B. "__privat__()"
"""

# Aufruf einer Methode:

class foo():

	def __init__(self, x):

		self.x = x


	def set_x(self, tmp_x):
		self.x = tmp_x


	def get_x(self):
		return self.x

x = input(":")
f = foo(x)

print(f.get_x())

new_x = input(":")
f.set_x(new_x)

print(f.get_x())



# Auflisten von Attributen und Methoden einer Klasse:

beispiel = ""
print( dir( beispiel ) )

beispiel2 = 2
print( dir( beispiel2 ) )

beispiel3 = []
print( dir( beispiel3 ) )
