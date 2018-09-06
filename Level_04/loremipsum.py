#!/usr/bin/env python3

lorem_ipsum = open("loremipsum.txt", "r")
text = lorem_ipsum.read() # type: str
lorem_ipsum.close()

orig = text
text = text.upper()

if "U" in text:
    text = text.replace("U", "V")

print(orig)
print("****************")
print(text)

lorem_ipsvm = open("loremipsvm.txt", "w")
lorem_ipsvm.write(text)
lorem_ipsvm.close()
