# Level 3:


# Typen von Listen:

# 1. Die Liste:

# Eine Liste ist eine veränderbare und unsortierte
# Menge von Elementen, welche alles mögliche sein
# können. Unsortiert heißt in dem Fall, das die
# Reihenfolge der Elemente eine Rolle spielt.

# Eine Liste wird mit Hilfe von eckigen Klammern definiert.
liste = [0, "foo"]
print(liste)

# Auf ein Element in einer Liste wird über dessen Index
# zugegriffen, das ist die Stelle an der das element
# steht.
# Wichtig: Die Zählung des Index beginnt mit 0,
# daher ist der Index des ersten Elements 0.
element = liste[0]
print(element)

# Mit len() kann man sich die Anzahl an Elementen einer
# Liste ausgeben lassen:
l = len(liste)
print(l)

# Die append() Methode fügt einer Liste ein beliebiges
# Element hinzu:
liste.append("bar")
print(liste)

# Der Datentyp String hat große Ähnlichkeit mit dem
# Datentyp Liste. So funktioniert der Zugriff über den
# Index auch bei einem String.

String = "ABCDEFGHIJKLMNOPQRSTUVW"
print(String)
print(String[4])

# Anstatt append() hat der String das +=:
String += "XYZ"
print(String)
# Dabei ist 'String += "XYZ"' eine Abkürzung für
# String = String + "XYZ", was bedeutet, dass ein
# String neudefiniert wird und nicht verändert wird.

# Mit list() lässt sich ein String in einen Liste verwandeln:
print(list(String))


# 2. Das Tuple:

# Ein Tuple ist eine unveränderliche und unsortierte
# Menge von Elementen.

# Ein Tuple wird über runde Klammern definiert:
Tuple = ("foo", "bar")
print(Tuple)

# Mit einem Index kann auf ein Element zugegriffen
# werden:
print(Tuple[0])

# Mit dem len() Befehl lässt sich die Länge aus-
# geben:
print(len(Tuple))


# 3. Das Dictionary:

# Ein Dictionary ist eine unsortierte Liste, in der
# immer einem key ein value zugeordnet ist.

# Ein Dictionary wird über geschweifte Klammern
# definiert:
dictionary = {"Eins":"one", "Zwei":"two"}
print(dictionary)

# Auf einen value wird mit Hilfe des keys zu-
# gegriffen:
print(dictionary["Eins"])

# Ein neues Key-Value-Paar wird erstellt,
# indem auf ein nicht existirenden Value zu-
# gegriffen wird und dieser definiert wird:
dictionary["Wasser"] = "water"
print(dictionary)

# Mit len() lässt sich die Länge ausgeben:
print(len(dictionary))



# Schleifen:

# 1. Die while-Schleife:

# Im Kopf der while-Schleife steht eine Bedingung.
# Sie prüft ob, die Bedingung True ist und durch-
# läuft ihren Bauch. Danach prüft sie erneut die
# Bedingung. Und das immer so weiter.
counter = 0

while counter < 10:
	counter += 1

# Endloswhile:
"""
while True:
	print("foo")
"""


# 2. Die for-Schleife:

# Die for-Schleife durchläuft ein iterierbares
# Objekt. Alle oben genannten Listen sind solche
# iterierbaren Objekte.
String = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in String:
	print(char)

# Beim Durchlaufen eines Dictonary wird jedoch nur
# der key zurückgegeben:
Dictonary = {"one":"Eins", "two":"Zwei", "three":"drei"}
for key in Dictonary:
	print(key)
	print(Dictonary[key])

# Mit dem Befehl range() erschafft man ein iterierbares
# Objekt, das mit Zahlen gefüllt ist:
R = range(10)
print(list(R))

# Dabei kann man auch den Startwert und die Schrittweite
# angeben:
R = range(0,101,2)
print(list(R))

# Somit kann man eine Zählschleife implementieren:
R = range(10)
for i in R:
	print(i)

# oder:

for i in range(10):
	print(i)

"""
Aufgaben:
* fakultaet.py:
  Schreibe ein Programm, das die Fakultaet einer Zahl 
  ausgibt, die der User eingibt.
  Fakultaet(n) = Fakultaet(n-1) * n
  Fakultaet(0) = 1

* potenz.py:
  Schreibe ein Programm, das dem User eine Basis und
  einen Exponenten eingeben lässt und ihm dann die
  Potenz ausrechnet.

* passwort.py:
  Ändere deine Passwort so ab, dass die Anzahl an Ver-
  suchen, die der Benutzer hat als int-Variable im Code
  hinterlegt werden kann.

* zahlenRaten.py:
  Ändere dein Programm so ab, dass der User den Bereich
  mit zwei Integern festlegen kann und die Anzahl an Ver-
  suchen, die er hat von der Größe des Intervalls abhängt.

Du solltest die Aufgaben in eigene Codedateien speichern,
weil spätere Level eventuell auf diese zurückgreifen.

"""
