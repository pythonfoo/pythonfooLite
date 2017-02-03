# random
Das Modul random ermöglicht einfache aber vielfältige Operationen mit Zufallszahlen. Hierbei sei gesagt, dass der eingebaute Zufallsgenerator bei weitem nicht der Beste ist und schon gar nicht für kryptographische Operationen genutzt werden sollte.
Wir fangen damit an das Modul random zu importieren und uns die Attribute und Methoden anzuschauen:
```python
import random
print(dir(random))
```
Als Ausgabe bekommen wir:
```python
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__',
'__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_ceil', '_cos', '_e', '_exp', '_inst', '_log', '_pi', 
'_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate',
'weibullvariate']
```
Viele dieser Sachen sind allerdings erstmal uninteressant, deshalb wollen wir uns daher erstmal auf folgende Dinge beschränken:

* choice
* gauss
* randint
* random
* randrange
* sample
* seed
* shuffle

### random.seed() 
Wir wollen dabei mit random.seed() anfangen. Mit dieser Methode können wir den Seed für die Zufallsberechnung setzen. Der Seed wird bei der Zufallsberechnung als Ausgang genommen, was bedeutet, das bei dem selben Seed immer derselbe Strom an Zufallszahlen entstehen wird. Daher ist diese Methode auch essentiell wichtig, da sie die anderen der obigen Methoden beeinflusst.
```python
import random
random.seed("foo")
random.random() # 0.45443115919715416 
random.random() # 0.27540896360984124 
```
Um Zufall zufällig zu behalten sollte **niemals** ein statischer Seed oder ein sehr primitiver Seed (wie zum Beispiel Datum oder Uhrzeit) benutzt werden.


### random.random()
Wir haben eben eine weitere Metode benutzt ohne sie einzuführen. Diese Methode liefert einen Fließkommawert zwischen 0 und ausschließend 1 zurück.
```python
import random
random.random()
```

### random.randint()
Diese Methode erwartet zwei Parameter (einen Startwert und einen Endwert) und gibt eine Zufallszahl zwischen diesen beiden Werten zurück, wobei der Endwert ausgenommen ist.
```python
import random
R = random.randint(0,10)
print(R)
```
ist äquivalent zu:
```python
import random
R = int(random.random()*10)
```
