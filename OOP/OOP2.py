#siehe auch diese Module
from tier import Tier
from hund import Hund

rex = Hund("Rex")

#<isinstance> prüft, ob ein bestimmtes Objekt von einer bestimmten Klasse stammt
isinstance(rex, Hund) #True
isinstance(rex, Tier) #True

#Methoden mit bestimmten Namen (z.B. "__add__") können Operatoren überladen
str(rex) #"Hallo, ich bin Rex."
