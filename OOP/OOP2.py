#siehe auch diese Module
from tier import Tier
from hund import Hund

rex = Hund("Rex")

#isinstance prüft, ob ein bestimmtes Objekt einer bestimmten Klasse entstammt
isinstance(rex, Hund) #True
isinstance(rex, Tier) #True

#mit Methoden mit bestimmten Namen (z.B. "__add__") können Operatoren überladen werden
str(rex) #"Hallo, ich bin Rex."
