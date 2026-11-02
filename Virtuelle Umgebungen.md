# Virtuelle Umgebungen

## Was ist eine virtuelle Umgebung?
Eine virtuelle Umgebung (englisch: *virtual environment*, kurz *venv*) ist ein abgeschlossener Bereich auf deinem Rechner, in dem eine eigene Python-Installation samt eigener Bibliotheken liegt. Alles, was du dort mit `pip` installierst, landet nur in dieser Umgebung und nicht in deiner systemweiten Python-Installation. Jedes Projekt bekommt so seine eigene, saubere Umgebung, die sich nicht mit anderen Projekten in die Quere kommt.

## Warum möchte ich eine virtuelle Umgebung haben?
Spätestens wenn du Bibliotheken aus dem Internet benutzt (z.B. `requests`, `PySide2` oder `Django`), solltest du mit virtuellen Umgebungen arbeiten. Mit einer virtuellen Umgebung kann ich:

 * für jedes Projekt genau die Bibliotheken (und deren Versionen) installieren, die es braucht
 * verhindern, dass sich zwei Projekte mit unterschiedlichen Versionsanforderungen gegenseitig stören
 * meine systemweite Python-Installation sauber halten (manche Betriebssysteme verlassen sich darauf und verbieten deshalb `pip install` außerhalb einer Umgebung)
 * leicht nachvollziehbar machen, welche Bibliotheken mein Projekt benötigt, damit andere es ebenfalls zum Laufen bekommen
 * eine kaputte Umgebung einfach löschen und neu anlegen, ohne das restliche System anzufassen

Du brauchst dafür nichts zu installieren: Das Modul `venv` ist seit Python 3.3 Teil der Standardbibliothek.

## Wie erstelle ich eine virtuelle Umgebung?
Wechsle zuerst in den Ordner deines Projektes und erzeuge dort die Umgebung. Üblicherweise nennt man den Ordner `.venv`:

```bash
python3 -m venv .venv  # Linux / macOS
```

```powershell
python -m venv .venv  # Windows
```

Der Befehl `python3 -m venv` ruft das Modul `venv` auf und übergibt ihm den Namen des Ordners, der angelegt werden soll (hier `.venv`). In diesem Ordner liegt danach eine eigene Kopie des Python-Interpreters und ein eigener `pip`.

Falls `python3` auf deinem System nicht gefunden wird, versuche es mit `python`, unter Windows ist das meistens der richtige Befehl.

## Wie aktiviere ich die Umgebung?
Damit dein Terminal die Python-Installation aus der Umgebung benutzt (und nicht die des Systems), musst du die Umgebung *aktivieren*:

```bash
source .venv/bin/activate  # Linux / macOS
```

```powershell
.venv\Scripts\Activate.ps1  # Windows (PowerShell)
```

Sobald die Umgebung aktiv ist, stellt dir dein Terminal meistens ihren Namen in Klammern vor den Prompt:

```bash
(.venv) $
```

Ab jetzt beziehen sich `python` und `pip` auf die Umgebung. Du kannst das überprüfen:

```bash
python --version
pip --version
```

> **Hinweis für Windows:** Sollte die Aktivierung mit einer Fehlermeldung zur *Execution Policy* abbrechen, erlaubt der folgende Befehl (einmalig, nur für deinen Benutzer) das Ausführen des Skriptes:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```

## Wie installiere ich Bibliotheken?
Bei aktiver Umgebung installierst du Bibliotheken wie gewohnt mit `pip`. Sie landen dann ausschließlich in der Umgebung:

```bash
pip install requests
```

Welche Bibliotheken gerade installiert sind, zeigt dir:

```bash
pip list
```

## Wie gebe ich mein Projekt an andere weiter?
Damit andere (oder du auf einem anderen Rechner) genau dieselben Bibliotheken installieren können, schreibst du die aktuelle Liste in eine Datei namens `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Diese Datei gehört ins Projekt und sollte eingecheckt werden (siehe `Versionskontrolle.md`). Aus ihr lässt sich die Umgebung an anderer Stelle wiederherstellen:

```bash
pip install -r requirements.txt
```

## Wie verlasse ich die Umgebung wieder?
Um die Umgebung zu deaktivieren und wieder das System-Python zu benutzen, genügt:

```bash
deactivate
```

## Wie lösche ich eine Umgebung?
Eine virtuelle Umgebung ist nur ein Ordner. Du kannst sie bedenkenlos löschen und bei Bedarf neu erzeugen:

```bash
rm -r .venv  # Linux / macOS
```

```powershell
Remove-Item -Recurse .venv  # Windows (PowerShell)
```

## Schneller geht es mit `uv`
[uv](https://docs.astral.sh/uv/) ist ein modernes, sehr schnelles Werkzeug, das die obigen Schritte - Umgebung anlegen und Pakete installieren - in wenigen Befehlen zusammenfasst. Es ist in der Programmiersprache Rust geschrieben und installiert Pakete um ein Vielfaches schneller als `pip`. Anders als `venv` gehört `uv` jedoch nicht zu Python und muss erst installiert werden.

### uv installieren
Am einfachsten über das offizielle Installations-Skript:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux / macOS
```

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows (PowerShell)
```

Es gibt noch weitere Wege (z.B. über den Paketmanager deines Systems oder `pip install uv`); eine Übersicht findest du in der [Installationsanleitung](https://docs.astral.sh/uv/getting-started/installation/).

### Umgebung anlegen und benutzen
Mit `uv` sieht der Ablauf von oben so aus:

```bash
uv venv                      # legt eine Umgebung im Ordner .venv an
source .venv/bin/activate    # aktivieren wie gewohnt (Windows: .venv\Scripts\Activate.ps1)
uv pip install requests      # Pakete installieren - wie pip, nur schneller
```

Praktisch: Fehlt eine passende Python-Version auf deinem Rechner, lädt `uv` sie bei Bedarf automatisch herunter.

### Noch bequemer: uv das Projekt verwalten lassen
`uv` kann auch das ganze Projekt verwalten. Statt einer `requirements.txt` benutzt es dann die Datei `pyproject.toml`:

```bash
uv init mein-projekt   # legt ein neues Projekt an
cd mein-projekt
uv add requests        # Paket hinzufügen (wird in pyproject.toml vermerkt)
uv run python main.py  # im Projekt ausführen - die Umgebung wird automatisch benutzt
```

In diesem Fall kümmert sich `uv` selbst um die virtuelle Umgebung - du musst sie nicht von Hand aktivieren. Für den Anfang reicht `python -m venv` aber völlig; `uv` lohnt sich, sobald dich die Geschwindigkeit oder die Projektverwaltung reizt.

## Was sollte ich noch beachten?
 * Der Ordner `.venv` gehört **nicht** in die Versionskontrolle – er ist groß, rechnerspezifisch und jederzeit aus der `requirements.txt` wiederherstellbar. Trage ihn in deine `.gitignore` ein:
   ```
   .venv/
   ```
 * Lege für jedes Projekt eine eigene Umgebung an.
 * Die Umgebung muss in jedem neuen Terminal erneut aktiviert werden.
 * Es gibt neben `venv` noch weitere Werkzeuge: das oben beschriebene [uv](https://docs.astral.sh/uv/) sowie z.B. [virtualenv](https://virtualenv.pypa.io/) oder [Poetry](https://python-poetry.org/). Für den Anfang reicht das mitgelieferte `venv` aber vollkommen aus.

## Wo erfahre ich mehr?
 * [Die offizielle Dokumentation zu `venv`](https://docs.python.org/3/library/venv.html)
 * [Das offizielle Tutorial zu virtuellen Umgebungen und `pip`](https://docs.python.org/3/tutorial/venv.html)
