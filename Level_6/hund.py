#!/usr/bin/env python3
from tier import Tier

class Hund(Tier):

	def __init__(self, name):

		self.name = name
		self.eigenschaften = {}

	def get_name(self):
		return self.name

	def set_name(self, new_name):
		self.name = new_name

	def add_attribut(self, key, value):
		self.eigenschaften[key] = value

	def list_attribute(self):
		for key in self.eigenschaften:
			print(str(key) + ": " + str(self.eigenschaften[key]))

	def __str__(self):
		return "Hallo, ich bin {}.".format(self.name)


if __name__ == "__main__":

	h1 = Hund("Rex")
	h1.add_attribut("Fellfarbe", "braun")
	h1.add_attribut("Rasse", "Dackel")
	h1.add_attribut("Alter", 3)
	h1.add_attribut("Augenfarbe", "Grün")


	h2 = Hund("Bello")
	h2.add_attribut("Fellfarbe", "weiß")
	h2.add_attribut("Rasse", "Rottweiler")
	h2.add_attribut("Alter", 2)

	print( h1.get_name() )
	h1.list_attribute()
	print("")
	print( h2.get_name() )
	h2.list_attribute()
