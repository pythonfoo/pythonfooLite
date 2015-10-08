#! /usr/bin/env python3
print ("""Fibonacci-Reihe:
Die Summe zweier Elemente ergibt das naechste.""")

#a, b = 0, 1
a = 0
b = 1
#while b < 50:
for sprechend in range(10):
    print (a)
    #a, b = b, a+b
    n = a
    a = b
    b += n
	   
