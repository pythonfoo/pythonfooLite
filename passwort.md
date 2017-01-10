# Einfache Passwortabfragen
Passwortabfragen werden häufig benutzt um die Authentizität eines Nutzers zu überprüfen, dabei bildet ein Passwort eine Art Geheimnis, dass ich dem Dienst mitgeteilt habe und das, im Idealfall, nur mir bekannt sein sollte. Somit kann ich dem Dienst zumindestens zeigen, dass ich die Person hinter diesem Account bin. In Zeiten von Zwei-Faktor Authentifizierung geraten einfache Passwortabfragen immer mehr in den Hintergrund, sie dienen hier aber auch nur als anschauliches Beispiel zum Umgang mit if-Bedingungen und generell zur Art, wie man ein Programm schreibt.
Generell sollten wir beim Programmieren immer darauf achten, möglichst einfach anzufangen, dabei ist erstmal wie sehr man den, dabei enstandenen Code, noch verbessern kann. Wir schreiben also erstmal Code, der auf die simpelste Art und Weise den Anforderungen entspricht und verbessern ihn fortlaufend. Dabei kann uns auch Versionskontrolle helfen Änderungen zu widerrufen.
Wenn wir also als Anforderung hätten
**Schreiben SIe ein Programm, das ein Passwort abfragt und etwas ausgibt, falls das Passwort dem vorgegebenen entspricht.**
würde folgendes Programm der Anforderungen komplett entsprechen:

```
password = "12345678"
password_input = input("Bitte geben Sie das Passwort ein: ")
if password == password_input:
	print("Zugang gewährt")
```

Theoretisch könnte man selbst dieses Programm weiter vereinfachen, worauf wir an der Stelle aber verzichten.
Es dürften aber schon einige Schwachstellen aufgefallen sein:

* Es gibt keine Ausgabe bei Eingabe eines falschen Passworts
* Das Programm beendet direkt nach einer falschen Eingabe
* Der Benutzer hat nur eine Möglichkeit das Passwort einzugeben
* Das Passwort kann beim Eingeben gelesen werden
* Das Passwort kann aus dem Quellcode gelesen werden

Um diese Nachteile wollen wir uns jetzt kleinschrittig kümmern, um am Ende ein Programm geschrieben zu haben, dass die selben Anforderungen vom Anfang erfüllt aber noch zusätzlich die Nachteile ausbügelt.
### Es gibt keine Ausgabe bei Eingabe eines falschen Passwort
Dies lässt sich mit wenig Aufwand am vorhandenen Code ändern:

```
password = "12345678"
password_input = input("Bitte geben Sie das Passwort ein: ")
if password == password_input:
	print("Zugang gewährt")
else:
	print("Das Passwort war falsch")
```
Durch den `else`-Zweig wird auch etwas ausgegeben, falls das Passwort nicht richtig war.

### Das Programm beendet direkt nach einer falschen Eingabe
Hier bemerken wir, dass wir ihn schon behoben haben, da jetzt etwas ausgegeben wird.
###Der Benutzer hat nur eine Möglichkeit das Passwort einzugeben
Dies ist tatsächlich ein Problem, da gerade bei langen komplizierten Passwörtern die Möglichkeit größer wird, sich bei einem einzigen Zeichen zu vertun. Wir wollen also nun dem Benutzer 3 Versuche geben das Passwort richtig einzugeben:
```
password = "12345678"
counter = 1
while counter <= 3
	password_input = input("Bitte geben Sie das Passwort ein: ")
	if password == password_input:
		print("Zugang gewährt")
		break
	else:
		print("Das Passwort war falsch")
	counter += 1
```
Durch das benutzen der while-Schleife hat der Benutzer jetzt 3 Versuche das Passwort einzugeben, ohne, dass es neu abgefragt wird, wenn es bereits richtig eingegeben wurde. Hier wurde ein Teil der Optimierung schon implizit übernommen, da eine Schleife nicht notwendig gewesen wäre um ein Password 3 mal abzufragen. So hätte man das Programm auch folgendermaßen schreiben können:
```
password = "12345678"
access = False
if not access:
	password_input = input("Bitte geben Sie das Passwort ein: ")
	if password == password_input:
		print("Zugang gewährt")
		access = True
	else:
		print("Das Passwort war falsch")

if not access:
	password_input = input("Bitte geben Sie das Passwort ein: ")
	if password == password_input:
		print("Zugang gewährt")
		access = True
	else:
		print("Das Passwort war falsch")

if not access:
	password_input = input("Bitte geben Sie das Passwort ein: ")
	if password == password_input:
		print("Zugang gewährt")
		access = True
	else:
		print("Das Passwort war falsch")

```
Spätestens jetzt sollte aber aufgefallen sein, das eine Schleife hier angebracht ist, zumal manchmal das Passwort ja auch 10-mal eingegeben werden kann.

### Das Passwort kann beim Eingeben gelesen werden
Um diesen Issue zu beheben müssen wir uns von der `input()` Funktion trennen, da bei ihrer Benutzung immer die Eingabe angezeigt wird. Daher benutzen wir nun die `getpass` Methode aus dem Modul `getpass`:
```
from getpass import getpass as passinput
password = "12345678"
counter = 1
while counter <= 3
	password_input = passinput("Bitte geben Sie das Passwort ein: ")
	if password == password_input:
		print("Zugang gewährt")
		break
	else:
		print("Das Passwort war falsch")
	counter += 1
```
Zum Glück funktioniert `getpass.getpass()`fast genauso wie `input()` weshalb wir  nur minimale Änderungen vornehmen mussten. Was aber auffällt ist, das wir gerade etwas geändert haben, was seit der ersten Version des Programms schon da war und somit sehr relevant war. Das sollte uns daran erinnern, das wir kein Code in Stein meißeln sondern so agil sein müssen, auch altbewährtes neu zu schreiben.
### Das Passwort kann aus dem Quellcode gelesen werden
Dieser Issue ist gewissermaßen ein wenig widersinning, denn wenn ich den Quellcode lesen kann, habe ich prinzipiell auch die Möglichkeit die Passwortabfrage einfach raus zu programmieren, aber wir wollen uns trotzdem anschauen, wie wir diesen Issue schließen können. Dafür müssen wir uns kurz mit Hashwerten befassen. Das Prinzip hinter einem Hashwert ist, dass ich aus einer Eingabe einen Wert erzeuge, wobei die Eingabe immer zu diesem Hashwert führen wird aber auch andere Eingaben zu diesem Hashwert führen können, weshalb man aus dem Hashwert nicht auf die Eingabe schließen kann. Beim Hashen der Eingabe gehen Informationen verloren, die nicht wiederhergestellt werden können. Genau diesen Effekt nutzen wir im Folgenden aus.
In Python kann man einen Hashwert aus einem Objekt mit der hash() Funktion erzeugen:
```
print(hash("Test")
print(hash("test"))
```
Doch wie nutzen wir den jetzt konkret Hashwerte für unsere Passwortabfrage? Nun im folgenden werden wir nicht mehr Passworteingabe und Passwort vergleichen, sondern die Passworteingabe hashen und mit dem Hash vom Passwort vergleichen, sodass das Passwort selber nicht im Quellcode steht. Dafür müssen wir aber erstmal an den Hashwert unseres Passwortes kommen:
```
>>> hash("12345678")
   -3267442341694311876
```
Nun können wir unser Programm umändern:
```
from getpass import getpass as passinput
passwordHash = -3267442341694311876
counter = 1
while counter <= 3
	password_input = passinput("Bitte geben Sie das Passwort ein: ")
	input_hash = hash(password_input)
	if passwordHash == inputHash:
		print("Zugang gewährt")
		break
	else:
		print("Das Passwort war falsch")
	counter += 1
```
Es liegt aber noch ein Problem vor:
Hashfunktionen verlieren Informationen, das heißt, dass mehrere Eingaben den selben Hashwert liefern können, weshalb der Benutzer nicht **das** Passwort eingeben muss, dass den Hashwert ergibt, sondern nur **eins** von denen, die diesen Hashwert ergeben. An dieser Stelle vertrauen wir darauf, dass die Wahrscheinlichkeit für so eine Kollision niedrig genug ist um sie zu tolerieren, zumal wir ja die Eingabe auf 3 Versuche beschränkt haben.

**Achtung**: *Für den praktischen Einsatz ist diese Hashfunktion ziemlich ungeeignet!*

## Fazit:
Wir haben mit einem Programm angefangen, das genau den gestellten Anforderungen entsprach. Anschließend haben wir Probleme mit unseren Programm ausgemacht und diese Issues in 5 Schritten behoben. Dabei haben wir zuerst nur Funktionalität hinzugefügt und in den letzten beiden Schritten auch bestehenden Code verändert. Wir haben aber die Funktionalität der ersten Version erhalten gelassen. Diesen Vorgang nennt man Refactoring. Bei dem Optimieren des Codes kann Versionskontrolle eine sehr wichtige Rolle spielen, denn es kann sein, dass man den Code überoptimiert und er auf ein mal nicht mehr tut was er soll. Vorrausgesetzt man hat eine ordentliche Versionskontrolle durchgeführt, kann man nun von dem letzten funktionierenden Stand aus vorwärts gehen und so die Änderung ausfindig machen, die das Programm zerschossen hat.
Sowohl zu Refactoring als auch zu Versionskontrolle haben wir eigene Folien (geplant).
