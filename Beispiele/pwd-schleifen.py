#!/usr/bin/env python3

from getpass import getpass

PWD = "123456"

for x in range(3):
	eingabe = getpass()
	
	if eingabe == PWD:
		print("Richtig.")
		break
	elif eingabe in PWD:
		print("Fast.")
	else:
		print("Falsch.")
