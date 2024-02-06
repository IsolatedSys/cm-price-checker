# cm-price-checker

## Windows Executable
1. Downloade die .exe Datei in [Releases](https://github.com/IsolatedSys/cm-price-checker/releases/tag/v1.1.0)
2. Commandline (cmd) öffnen und mit `.\cm-scraper.exe` ausführen. Weitere Argumente siehe Abschnitt [CLI Arguments](./README.md#cli-argumente)

## Python

### Windows Installation:
1. Gehe zur offiziellen Python-Website: https://www.python.org/downloads/
2. Lade die neueste Version von Python herunter und folge den Installationsanweisungen.
3. Stelle sicher, dass du während der Installation die Option "Add Python to PATH" aktivierst.

### Mac Installation:
1. Öffne ein Terminal.
2. Installiere Homebrew, falls noch nicht installiert: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. Installiere Python 3 mit Homebrew: `brew install python`

### Linux Installation:
1. Öffne ein Terminal.
2. Führe den Befehl aus, um Python 3 zu installieren:
   - Ubuntu/Debian: `sudo apt-get install python3`
   - Fedora: `sudo dnf install python3`
   - Arch Linux: `sudo pacman -S python`

## Requirements
- Chrome oder eine Chromium-Derivat

### Dependencies:
- cfscrape
- BeautifulSoup
- fake_useragent
- pandas

#### Evtl.:
- setuptools

### Installation von Requirements:
1. Öffne ein Terminal.
2. Navigiere zum Verzeichnis deines Projekts.
3. Führe den Befehl aus: `pip install -r requirements.txt`


## CLI-Argumente

Das Skript akzeptiert verschiedene CLI-Argumente für die Steuerung seines Verhaltens. Hier sind die verfügbaren Optionen:

- `--path <PATH>`: Pfad zur Eingabedatei im XLSX-Format. (Default: xlsx/Vorlage.xlsx)
- `--output <PATH>`: Pfad zur Ausgabedatei im XLSX-Format. (Default: xlsx/Ergebnis.xlsx)
- `--jump_over_filled`: Überspringt gefüllte Einträge und ruft nur neue URLs ab (Standard: False).
- `--sleep <SECONDS>`: Minimale Wartezeit zwischen Anfragen (Standard: 3). Je höher die Zahl, desto besser die Chance, nicht von Cardmarket erkannt zu werden und weniger Wiederholungen sind erforderlich.
- `--create`: Erstellt eine neue CSV-Datei mit Standardspalten und macht keine weiteren Schritte. Diese Vorlage kann man mit den URLs von Cardmarket füllen.
- `--pause`: Unterbricht die Ausführung nach jeweils 15 Karten, um die Erkennung durch Cardmarket zu verhindern (Standard: True).

### Beispielaufruf:
```bash
python cm-scraper.py --path input.xlsx --output output.xlsx --jump_over_filled --sleep 5
```
Das Program oeffnet `input.xlsx`, springt über schon befuellte Zellen und pausiert zw. 5.5 und 6.5 Sekunden zwischen jeder Karte. Anschließend wird das Ergebnis in `output.xlsx` ausgegeben.

### Beispiel um eine Vorlage zu generieren. Erstellt im `xlsx` Ordner das File `Vorlage.xlsx`.
```bash
python cm-scraper --create
```
Das erstellte File kann mit URLs zu den Karten befüllt werden und mit
```bash
python cm-scraper.py
```
sofort ohne weitere Argumente verwendet werden. Das Ergebnis befindet sich dann in `xlsx/Ergebnis.xlsx`. 

