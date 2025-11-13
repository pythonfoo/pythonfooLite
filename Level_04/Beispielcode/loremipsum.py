#!/usr/bin/env python3

from pathlib import Path

lorem_ipsum = Path("loremipsum.txt")
text = lorem_ipsum.read_text() # type: str

orig = text
text = text.upper()

if "U" in text:
    text = text.replace("U", "V")

print(orig)
print("****************")
print(text)

lorem_ipsvm = Path("loremipsvm.txt")
lorem_ipsvm.write_text(text)
