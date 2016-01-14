def funktion():
    print("Hallo!")
    

funktion()
# OUT: Hallo!
def funktion(text):
    print(text)
    

funktion("a")
# OUT: a
def funktion(text, wirklich):
    if wirklich:
        print(text)
        

funktion("Hallo", True)
# OUT: Hallo
funktion(True, "Hallo")
# OUT: True


>>> def funktion(text="Beispiel" , wirklich=False):
...     if wirklich:
...         print(text)
...         
...     
... 
>>> funktion()

>>> funktion(wirklich=True)
Beispiel

>>> funktion(wirklich=True, text="Abc")
Abc

>>> def ja():
...     return "Ja"
... 
>>> ja()
'Ja'


# Rekursion:

def fun():
	print("Fun!")
	fun()

# Zeit:

>>> import time
>>> time.time()
1444327310.2887266
>>> time.localtime()
time.struct_time(tm_year=2015, tm_mon=10, tm_mday=8, tm_hour=20, tm_min=2, tm_sec=11, tm_wday=3, tm_yday=281, tm_isdst=1)
>>> time.localtime()[0]
2015
>>> list(time.localtime())
[2015, 10, 8, 20, 3, 1, 3, 281, 1]
>>> time.localtime().tm_year
2015

# Ladebalken:

>>> import time
>>> while True:
...     print(".", end="")
...     time.sleep(1)
...     
... 
...........................................

# Quersumme:

>>> def quersumme(zahl):
...     qs = 0
...     for ziffer in str(zahl):
...         qs += int(ziffer)
...         
...     return qs
... 

