# Level 4


Um eine Datei zu lesen oder bearbeiten, muss diese erst einmal geladen werden.
``` python
filename = "loremipsum.txt"
file_object = open(filename, "r")
```
Der Variablen `file_object` wird nun ein `_io.TextIOWrapper`.
Dieses Objekt bietet mehrere Methoden zum bearbeiten dieser Datei.
Der String `"r"` steht dabei für den Modus, mit dem die Datei geöffnet wurde.

Dieser Modus ist ein Attribut des `_io.TextIOWrapper` und kann auch ausgelesen werden:
``` python
mode = file_object.mode
print(mode)
# Out: "r"
```

Es gibt die Modi `"r"` für Lesen, `"w"` für Schreiben und `"a"` für Anhängen.

Es sollte darauf geachtet werden, die Datei nach dem Lesen oder dem Bearbeiten wieder zu schließen.

``` python
file_object.close()
```

## Datei einlesen
``` python
filename = "loremipsum.txt"
file_object = open(filename, "r")
text = file_object.read()
file_object.close()
```
Die Methode `read()` liefert dabei einen String zurück, der den Inhalt der Datei enthält.
Alternativ kann auch die Methode `readlines()` benutzt werden. Diese gibt eine Liste von Zeilen 
zurück.

Wichtig zu beachten ist, dass die Datei gelesen wird, indem ein Zeiger durch sie durch läuft,
was bedeutet, dass nach dem vollständigen Lesen der Datei der Zeiger zurück gesetzt werden 
muss, da sonst ein leerer String zurückgegeben werden wird. 

``` python
filename = "loremipsum.txt"
file_object = open(filename, "r")
lines = f.readlines()
file_object.close()
```
Gerade für größere Dateien ist es aber auch möglich nur eine einzelne Zeile einzulesen:
``` python
filename = "loremipsum.txt"
file_object = open(filename, "r")
for i in range(10):
	line = f.readline()
	print(line)
file_object.close()
```

## In eine Datei schreiben
Das Schreiben eines Strings in eine Datei funktioniert sehr ähnlich wie das Auslesen. Dazu
muss die Datei allerdings erst mit dem entsprechenden Modus geladen werden.
``` python
content = 100*"spam\n"
filename = "spam.txt"
file_object = open(filename, "w")
file_object.write(content)
file_object.close()
```
Wenn die Datei mit dem Dateinamen nicht vorhanden ist, wird sie in diesem Modus erstellt.
Wichtig ist, dass die Datei dabei überschrieben wird, falls sie schon vorhanden war.

Es ist auch möglich einzelne Zeilen in die Datei zu schreiben, was grade bei größeren Texten 
sinnvoll sein kann.

``` python
content = 10*["spam"]
filename = "spam.txt"
file_object = open(filename, "w")
for line in content:
	file_object.writeline(line)
file_object.close()
```

Ebenso können natürlich auch die Zeilen gesammelt geschrieben werden:

``` python
content = 10*["spam"]
filename = "spam.txt"
file_object = open(filename, "w")
file_object.writelines(line)
file_object.close()
```

## An eine Datei anfügen
Beim Anhängen an eine Datei wird beim Öffnen der Datei der Zeiger auf das Dateiende gelegt,
sodass etwas, das in die Datei geschrieben wird, an das Ende der Datei dran gehangen wird.

``` python
content = 100*"spam\n"
filename = "test.txt"
file_object = open(filename, "a")
file_object.write(content)
file_object.close()
```

Ebenso wie beim Schreiben, wird die Datei erstellt, sollte sie nicht vorhanden sein.
Das Verhalten der Methoden `writeline()`und `writeline()`ist in diesem Modus analog zu ihrem
Verhalten im Schreiben Modus.
