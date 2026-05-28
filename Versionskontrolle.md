# Einstieg in Git

## Was ist Versionskontrolle?
Mit einer Versionskontrolle ist es möglich, die verschiedenen Versionen eines Programms, welche beim Programmieren natürlich entstehen, zu dokumentieren. So ist es möglich, Änderungen rückgängig zu machen, verschiedene Entwicklungszweige zusammen zu führen oder die Arbeit mehrerer Leute miteinander zu verknüpfen.

## Warum möchte ich Versionskontrolle haben?
Mit einer funktionierenden Versionskontrolle kann ich:

 * Mit vielen Leuten an einem Projekt arbeiten, ohne sich im Weg zu stehen
 * Schnell die Version finden, bei der alles kaputt ging
 * Auf einfache Weise nachvollziehen wie sich mein Projekt entwickelt hat
 * Den Fortschritt meines Projektes im Auge behalten

Versionsverwaltung hat zwar nur indirekt mit Programmierung zu tun, ist aber ein sehr praktisches Hilfsmittel, gerade wenn es um größere Projekte geht, an denen eventuell auch mehrere Leute arbeiten. Durch die Möglichkeit, zu einer bestimmten Version zurückspringen zu können, wird es einfacher Fehler zu finden. Sobald die Verwaltung der Versionskontrolle in den Workflow eines Projektes übergegangen ist, wird die Entwicklung

## Was ist git?
Nachdem jetzt (hoffentlich) klar wurde, warum Versionskontrolle beim Programmieren eine gute Idee ist, ist es natürlich wichtig zu wissen, wie man das denn umsetzt, dazu gibt es glücklicherweise eine einfache Möglichkeit: Git. Git ist, sehr vereinfacht, eine Möglichkeit Versionskontrolle durchzuführen, die sich bewährt hat.

## Wie installiere ich git?

Am besten mit dem Paketmanager deines Systems:

```bash
sudo apt install git # Debian / Ubuntu
```

```powershell
winget install Git.Git # Windows
```

```bash
git  # macOS
```

## Wie verwende ich git?

Git lässt sich unter UNIX als Konsolen-Programm ausführen, unter Windows ist das Arbeiten mit Git etwas komplexer durch die Git-Bash.

### Ich will aber nicht in der Konsole arbeiten
Es gibt sowohl unter Windows als auch unter Linux, Programme mit einer graphischen Oberfläche, welche git dann im Hintergrund aufrufen, falls einem die Arbeit mit der Konsole zu kompliziert erscheint. Allerdings lassen sich gerade die komplexeren Operationen in der Konsole komfortabler lösen lassen und die Hilfestellungen im Internet™ häufig zu den Konsolen-Befehlen ausführlicher sind.

## Wie kann ich Git lernen?

Mit [Oh My Git!](https://ohmygit.org/) gibt es eine schöne interaktive Einführung.
Deutlich vollständiger, aber auch wesentlich trockener ist [das Buch "Pro Git"](https://git-scm.com/book).
