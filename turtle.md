# Einstieg in turtle
## Vorwort
Im folgenden wird das `turtle`-Modul aus der Standardbibliothek vorgestellt, die Beispiele sind absichtlich einfach gehalten und sollen einen sanften Einstieg gewährleisten. Um den Codebeispielen folgen zu können, solltest du wissen:

* wie du auf deinem System Pythoncode ausführst
* was eine Variable ist
* was ein Funktionsaufruf ist
* was ein `int`, ein `string` und ein `float`sind
* was eine `if`-Bedingung ist
* was eine Schleife ist

Solltest du bei einem der oben genannten Punkte noch Fragen oder Probleme haben, schau dir doch mal die Level 0 - 2 an.

## Das turtle-Modul
Mit dem `turtle` Modul ist es möglich, mit Hilfe von einfachen Befehlen/Funktionen die namensgebende turtle über ein Fläche zu bewegen.
Die turtle zeichnet dabei standardmäßig eine Spur hinter sich, dies kann benutzt werden um einfache bis komplexe Formen auf der 2D-Ebene zu zeichnen.
Das `turtle`-Modul stellt dafür einfache Funktionen bereit, die miteinander verknüpft werden können um die turtle zu bewegen.

Viele `turtle`-Methoden bieten Aliasse an (z.B. `turtle.fd()` statt `turtle.forward()`). Diese Aliasse vermindern die Schreibarbeit, leider aber auch die Lesbarkeit. Ob du diese Aliasse benutzen willst, um ein paar Zeichen zu sparen, bleibt selbstverständlich dir überlassen. Wir weisen bei den Funktionen auf ihre jeweiligen Aliasse hin.

Im folgenden sollen in kurzen Codeabschnitten, die einzelnen Funktionen vorgestellt werden. Die Codeabschnitte sind so konzipiert, dass sie einfach in den Interpreter oder eine .py-Datei kopiert werden können, ohne auf vorherige Abschnitte angewiesen zu sein. Daher fängt jeder Codeabschnitt auch mit dem `import`-Statement an.

Für den Anfang kannst du die turtle am einfachsten aus dem Interpreter heraus steuern. Öffne dazu den Python-Interpreter deiner Wahl, importiere die `turtle`-Bibliothek und fang an der turtle Befehle zu geben. Dann sollte sich ein Fenster öffnen, in dem du die turtle beobachten kannst. Die Arbeit im Interpreter hat den Vorteil, dass du die Auswirkungen deines Codes direkt sehen kannst. Es bietet sich also an deinen Python-Interpreter und das turtle-Fenster nebeneinander zu öffnen.

## Die turtle bewegen
Die `forward()` und `backward()` Methoden können für die Bewegung benutzt werden. Die turtle läuft dabei die angegebene Strecke ab und zieht eine Spur hinter sich her. Dabei ändert sich nicht ihre Richtung. Beim Start des Programms ist die Richtung `0` was nach rechts entspricht. 

Alternativ zu `turtle.forward(n)` kann auch `turtle.fd(n)` und statt
`turtle.backward(n)` `turtle.bk(n)` benutzt werden.
``` python
import turtle
turtle.forward(50)   # bewegt die turtle um 50 Pixel nach vorne
turtle.backward(25)  # bewegt die turtle um 25 Pixel nach hinten
```

Um die turtle zu drehen und somit ihre Richtung zu ändern, gibt es die `left()` und `right()` Methode, welche die turtle um eine bestimmte Gradzahl in die entsprechende Richtung drehen. Alternativ zu `left()` und `right()` können auch die Alias-Methoden `lt()` bzw. `rt()` benutzt werden.
``` python
import turtle
turtle.forward(50)  # bewegt die turtle um 50px
turtle.left(90)     # dreht die turtle um 90° nach links
turtle.forward(20)  # bewegt die turtle um 20px
turtle.right(180)   # dreht die turtle um 180° nach rechts
turtle.forward(20)  # bewegt die turtle um 20px
```

## Auslesen von Position und Richtung
Die Methoden `turtle.position()` und `turtle.heading()` liefern uns die aktuelle Position bzw. Richtung der turtle. Diese Methoden können zum Beispiel dabei helfen, nicht über den Rand zu laufen oder eine Kreislinie entlang zu laufen. 
``` python
import turtle
turtle.forward(100)           # bewegt die turtle um 100px
turtle.left(90)               # dreht die turtle um 90° nach links
turtle.forward(50)            # bewegt die turtle um 50px

position = turtle.position()  # aktuelle Position
print(position)  # Out: (100.00,50.00)

heading = turtle.heading()    # aktuelle Richtung
print(heading)  # Out: 90.0
```
Alternativ zu `turtle.position()` kann `turtle.pos()` verwendet werden.

Zusätzlich zu den Methoden `forward()` und `backward()` welche die turtle relativ zu ihrer aktuellen Position bewegen, kann auch die `setposition()` Methode benutzt werden um die turtle unabhängig von ihrer aktuellen Position und Richtung zu einer bestimmten Position zu bewegen. Dabei wird die Richtung beibehalten.
``` python
import turtle
turtle.setposition((100, 0))  # bewegt die turtle zu angegebenen Position
turtle.setposition((100, 100))
```
Alternativ zur `setposition()`-Methode können auch die Alias-Methoden `setpos()` oder `goto()` benutzt werden.

Analog zur `turtle.setposition()`-Methode kann die `turtle.setheading()`-Methode benutzt werden um die Richtung der turtle unabhängig von ihrer aktuellen Richtung zu verändern. Standardmäßig erwartet die Methode eine Gradzahl als `int` oder `float`. Hierbei entsprechen 0° nach rechts, 90° nach oben, 180° nach links, 270° nach oben. Es ist allerdings auch möglich negative Werte anzugeben (-90° entspricht nach unten).
``` python
import turtle
print(turtle.heading())  # Out: 0.0

turtle.setheading(90)  # setzt die Richtung der turtle auf die angegebene Gradzahl
turtle.forward(50)

print(turtle.heading())  # Out: 90.0
print(turtle.position())  # Out: (0.00, 50.00)
```
Alternativ zur `setheading()`-Methode kann auch die Alias-Methode `seth()` benutzt werden.

Eine praktische Methode im Zusammenhang mit Position und Richtung ist die `turtle.home()`-Methode, welche Position und Richtung auf `(0.00, 0.00)` bzw. `0.0` zurücksetzt.

Mit Hilfe der `distance()`-Methode kann die Entfernung der turtle zum Beispiel zu einer Position berechnet werden.
```python
import turtle
turtle.setposition((100, 100))
distance = turtle.distance((0, 0))  # berechnet die Distanz zur Position
print(distance)  # Out: 141.4213562373095
```

Analog zur `distance()`-Methode kann mit der `towards()`-Methode der Winkel der Linie zwischen der aktuellen Position und der angegebenen Position.
```python
import turtle
turtle.setposition((100, 100))
gradient = turtle.towards((0, 0))
print(gradient)
# Out: 225.0
```

## Manipulation der gezogenen Linie
Standardmäßig zeichnet die turtle eine schwarze Linie, wenn sie sich bewegt. Mit `turtle.penup()` und `turtle.pendown()` ist es möglich den *Stift* zu heben un zu senken und somit das Zeichnen der Linie zu unterbrechen. Dies kann sinnvoll sein um die turtle zu einer Ausgangsposition zu bewegen, ohne dabei eine Linie zu ziehen. Gerade in Verbindung mit der `turtle.setposition()`- und der `turtle.home()`-Methode ergibt es Sinn den *Stift* anzuheben.

Der folgende Codeabschnitt bewegt die turtle zu einer Ausgangsposition `(-100, -100)` und zeichnet anschließend ein Quadrat mit einer Seitenlänge von 200 Pixeln, dessen Mitte bei `(0.00, 0.00)` liegt.
```python
import turtle
turtle.penup()                    # Stift heben -> keine Linie
turtle.setposition((-100, -100))  # Ausgangsposition
turtle.pendown()                  # Stift senken -> Linie
for i in range(4):
    turtle.forward(200)
    turtle.left(90)
```
Alternativ zu `turtle.penup()` können auch die Alias-Methoden `turtle.pu()` oder `turtle.up()` benutzt werden. Alternativ zu `turtle.pendown()` können auch die Alias-Methoden `turtle.pd()` oder `turtle.down()` benutzt werden.

Mit Hilfe der `turtle.isdown()`-Methode kann überprüft werden, ob der *Stift* gesenkt ist, also ob gerade eine Linie gezogen wird.
```python
import turtle
turtle.penup()   # Stift heben -> keine Linie
pen_status = turtle.isdown()
print(pen_status)
# Out: False

turtle.pendown()  # Stift senken -> Linie
pen_status = turtle.isdown()
print(pen_status)
# Out: True
```

Die Farbe der Linie, welche von der turtle gezogen wird, lässt sich mit der `turtle.pencolor()` lesen und verändern. Übergeben wir der Methode keine Parameter, wird die aktuelle Farbe zurückgegeben. Übergeben wir der `turtle.pencolor()`-Methode allerdings einen Parameter, der eine entsprechende Farbe enthält, so nimmt der Stift diese Farbe an.
```python
import turtle
color = turtle.pencolor()
print(color)
# Out: 'black'
turtle.pencolor("red")
turtle.forward(100)
```

Es gibt verschiedene Formate der `turtle.pencolor()`-Methode einen Farbparameter zu geben. Im oberen Beispiel wurde ein *color string* benutzt, eine weiteres Format besteht in einem *RGB-tuple* welches die Farbe als Mischung aus **R**ot, **G**rün und **B**lau angibt. 
```python
import turtle
turtle.pencolor((255, 0, 0))  # setzen der Farbe mit einem RGB-tuple
turtle.forward(100)
```

Weitere Informationen zu den verschiedenen Formaten findest du in der Dokumentation zum `turtle`-Modul: https://docs.python.org/3/library/turtle.html#turtle.pencolor.

Neben der Stiftfarbe ist es möglich die Stiftbreite zu ändern. Dafür wird die `turtle.pensize()`-Methode benutzt. Der folgende Codeschnippsel zeichnet das Quadrat von weiter oben, diesmal allerdings mit einer größeren Stiftbreite. Ähnlich zur `turtle.pencolor()`-Methode, liest die `turtle.pensize()` den aktuellen Wert aus, sollten keine Parameter übergeben werden und setzt den Wert der Stiftbreite, sollten Parameter übergeben worden sein.
```python
import turtle
pen_size = turtle.pensize()       # Auslesen der Stiftbreite
print(pen_size)  # Out: 1

turtle.pensize(10)                # Setzen der Stiftbreite
turtle.penup()                    # Stift heben -> keine Linie
turtle.setposition((-100, -100))  # Ausgangsposition
turtle.pendown()                  # Stift senken -> Linie
for i in range(4):
    turtle.forward(200)
    turtle.left(90)
```
Alternativ zur `turtle.pensize()`-Methode kann auch die `turtle.width()`-Methode benutzt werden.

## Flächen füllen
Mit den Methoden `turtle.begin_fill()` und `turtle.end_fill()` ist es möglich, Flächen zu färben, die von der turtle eingeschlossen wurden. Im folgenden Codeschnippsel wird dies (wieder am Beispiel eines Quadrates) demonstriert. Die Methode `turtle.fillcolor()` kann analog zur Methode `turtle.pencolor()` benutzt werden um die entsprechende Farbe festzulegen. Die Methode `turtle.filling()` wird analog zur Methode `turtle.isdown()` benutzt um zu erkennen, ob gerade eine Fläche gefüllt wird.
```python
import turtle
turtle.penup()                    # Stift heben -> keine Linie
turtle.setposition((-100, -100))  # Ausgangsposition
turtle.pendown()                  # Stift senken -> Linie
print("filling? ", turtle.filling())

turtle.fillcolor("blue")          # Setzen der Farbe zum ausfüllen
turtle.begin_fill()               # Ausfüllen starten

for i in range(4):
    turtle.forward(200)
    turtle.left(90)
    print("filling? ", turtle.filling())

turtle.end_fill()                 # Ausfüllen beenden
```

Die Methode `turtle.color()` kann benutzt werden um sowohl die *pencolor* als auch die *fillcolor* festzulegen.
```python
import turtle
turtle.color("red", "blue")
print(turtle.pencolor())  # Out: red
print(turtle.fillcolor())  # Out: blue 
```

## Ändern der Geschwindigkeit
Die Geschwindigkeit der turtle kann mit der `turtle.speed()`-Methode gelesen und geändert werden. Im folgenden Codeschnippsel wird das bereits bekannte Quadrat gezeichnet, jedoch wird beim Zeichnen die Geschwindigkeit von Kante zu Kante variiert.
```python
import turtle
turtle.penup()                    # Stift heben -> keine Linie
turtle.setposition((-100, -100))  # Ausgangsposition
turtle.pendown()                  # Stift senken -> Linie
speed = turtle.speed()            # Auslesen der Geschwindigkeit
print(speed)  # Out: 3

for i in range(4):
    turtle.forward(200)
    turtle.left(90)
    turtle.speed(speed + 3)       # Setzen des speed-Wertes 
```
Die Geschwindigkeit kann auf zwei Arten angegeben werden: als `int` zwischen `0` und `10` oder als *speed string*. Wird ein Wert `<0.5` oder `>10` übergeben, wird der `speed`-Wert auf `0` gesetzt. Folgende *speed strings* sind möglich:
* `“fastest”: 0`
* `“fast”: 10`
* `“normal”: 6`
* `“slow”: 3`
* `“slowest”: 1`

## Weitere Funktionen
Das `turtle`-Modul umfasst noch viele weitere Funktionen, sie alle hier aufzulisten wäre müßig und redundant. Du solltest nun die wichtigsten Methoden kennengelernt haben. Gerüstet mit diesen Methoden kannst du jetzt mit dem Modul experimentieren. In diesem Abschnitt folgen noch ein paar weitere Methoden, falls du noch mehr kennenlernen möchtest. Da wir hier nicht alle Methoden vorstellen solltest du trotzdem dir die Dokumentation zum `turtle`-Modul (du findest sie unter: https://docs.python.org/3/library/turtle.html) ansehen, um rauszufinden, was noch alles möglich ist.

### Sichtbarkeit der turtle
Mit der Methode `turtle.hideturtle()` lässt sich die turtle verstecken, in der Dokumentation wird erwähnt, das dies die Performanz verbessern kann. Um die turtle wieder sichtbar zu machen, kann die Methode `turtle.showturtle()` verwendet werden. Alternativ können auch die Aliasmethoden `turtle.ht()` bzw. `turtle.st()` benutzt werden.

### Bildschirmgröße
Das `turtle`-Modul bietet auch Methoden an auf den Fenster zuzugreifen, in dem sich die turtle bewegt. Beispielsweise kann mit der `turtle.screensize()` die Bildschirmgröße abgerufen und geändert werden.
```python
import turtle
width, height = turtle.screensize()
print(width, height)  # Out: 400 300
turtle.screensize((800, 600))
```
Die genaue größe des Fensters in Pixeln zu kennen, kann hilfreich sein, um zu verhindern, dass die turtle den sichtbaren Bereich verlässt.

### turtle.Turtle