#!/usr/bin/env python3

# Dies ist eine Beispiellösung für die Aufgabe 9.2 (Klammer-Prüfer) aus Level 9.


class Stack(list):          # Stapel, wie im Notebook
    def is_empty(self):
        return len(self) == 0

    def push(self, element):
        self.append(element)

    def pop(self):
        return super().pop()


def klammern_korrekt(text):
    """Prüft, ob die Klammern in text korrekt geschachtelt sind."""
    # Zu jeder schließenden Klammer die passende öffnende:
    paare = {")": "(", "]": "[", "}": "{"}
    stapel = Stack()
    for zeichen in text:
        if zeichen in "([{":
            # öffnende Klammer merken
            stapel.push(zeichen)
        elif zeichen in ")]}":
            # schließende Klammer: oben muss die passende öffnende liegen
            if stapel.is_empty() or stapel.pop() != paare[zeichen]:
                return False
    # Korrekt, wenn nichts offen geblieben ist:
    return stapel.is_empty()


for beispiel in ["(a[b]c)", "(a[b)c]", "{[()]}", "(((", ""]:
    print(f"{beispiel!r:12} -> {klammern_korrekt(beispiel)}")
