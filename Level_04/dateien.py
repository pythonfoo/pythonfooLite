#!/usr/bin/env python3

# Level 4: Dateien

# Pathlib (https://docs.python.org/3/library/pathlib.html) ist die beste Möglichkeit,
# mit Pfaden und Dateien zu hantieren.

from pathlib import Path

# Existiert eine Datei?

Path("lorem_ipsum.txt").exists() # type: bool
# OUT: False
Path("loremipsum.txt").exists()
# OUT: True

# einen Ordner erstellen

test_dir = Path("test")
test_dir.mkdir()

# eine Datei auslesen

# schneller: print(Path("loremipsum.txt").read_text())
lorem_ipsum = Path("loremipsum.txt").open("r")
print(lorem_ipsum.read())
lorem_ipsum.close()

# eine Datei schreiben

test = (test_dir / Path("test.txt")).open("w")
test.write("total toller Text") # type: int
# OUT: 17
test.close()

# eine Datei löschen

(test_dir / Path("test.txt")).unlink()

# einen Ordner löschen

test_dir.rmdir()
