# Level 6 Aufgaben

## Aufgabe 1 (Monty Python)

Passe deine Lösung aus Level 4 so an, dass:
 * alle Dateinamen als Parameter auf der Kommandozeile übergeben werden können
 * alle Befehle in einem Programm sind
 * `argparse` dabei verwendet wird

Wenn du keine eigene Lösung hast, kannst du auch unsere Lösung von Level 4 benutzen.
Aufrufbar sein soll das Programm am Ende wie folgt:

```bash
python3 monty.py words --input monty.txt --output words.txt
python3 monty.py chars --input monty.txt --output chars.txt
python3 monty.py analyze --chars chars.txt
python3 monty.py replace --input monty.txt --output MONTY.txt
```
