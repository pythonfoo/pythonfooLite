# Dieses Programm enthält verschiedene Fehler,
# die Aufgabe besteht darin die Fahler zu finden
# und zu beheben.
import getpass, sys

pass = "Geheim"

eingabe = getpass.getpass("Bitte geben Sie das Passwort ein: \n")

if eingabe == pass:
	print("Das Passwort war richtig.")
    print("Bitte fahren Sie fort.")

else:
	print("Das Passwort war falsch.')
	sys.exit()
