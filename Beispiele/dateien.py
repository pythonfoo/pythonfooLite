#!/usr/bin/env python3

with open("loremipsum.txt", "r") as lorem_ipsum:
	text = lorem_ipsum.read()
orig = text
text = text.upper()
if "U" in text:
	text = text.replace("U", "V")
print(text)
print(orig)
with open("loremipsvm.txt", "w") as lorem_ipsvm:
	lorem_ipsvm.write(text)
