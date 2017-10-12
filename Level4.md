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

## Datei einlesen
``` python
text = file_object.read()
```
Die Methode `read()` liefert dabei einen String zurück, der den Inhalt der Datei enthält.
Alternativ kann auch die Methode `readlines()` benutzt werden. Diese gibt eine Liste von Zeilen 
zurück.

Wichtig zu beachten ist, dass die Datei gelesen wird, indem ein Zeiger durch sie durch läuft,
was bedeutet, dass nach dem vollständigen Lesen der Datei der Zeiger zurück gesetzt werden 
muss, da sonst ein leerer String zurückgegeben werden wird. 

``` python
file_object = open(filename, "r")
lines = f.readlines()
```
Gerade für größere Dateien ist es aber auch möglich nur eine einzelne Zeile einzulesen:
``` python
file_object = open(filename, "r")
for i in range(10):
	line = f.readline()
	print(line)
```

## In eine Datei schreiben
Das Schreiben eines Strings in eine Datei funktioniert sehr ähnlich wie das Auslesen. Dazu
muss die Datei allerdings erst mit dem entsprechenden Modus geladen werden.
``` python
content = 100*"spam\n"
filename = "test.txt"
file_object = open(filename, "w")
file_object.write(content)
```
Wenn die Datei mit dem Dateinamen nicht vorhanden ist, wird sie in diesem Modus erstellt.

## An eine Datei anfügen
