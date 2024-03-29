# cm-price-checker

## Disclaimer:
Evt. verstößt dieses Skript gegen die Richtlinien einer Seite. Eventuelle Sperren sind möglich, wenn zuviele Anfragen hintereinander gesendet werden. Verwendung auf eigene Gefahr.

Aufpassen, dass ältere .xlsx Dateien nicht überschrieben werden! Noch nicht ausgiebig genug getestet.

Möglicherweise funktioniert es, wenn ein 'generierter Output' wieder als Input verwendet wird, sodass das Ergebnis eine erweiterte Liste ist. Bitte testen, ansonsten [Issue](https://github.com/IsolatedSys/cm-price-checker/issues/new/choose) erstellen.
Bis jetzt werden nur die neuen links als hyperlinks gespeichert. Wenn `--concat` (Python only) mitgegeben wird, werden durch funktionen generierte Texte zu Texten umgewandelt und vorhandene Hyperlinks zu Text.


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
- `--create`: Erstellt eine neue XLSX-Datei mit Standardspalten und macht keine weiteren Schritte. Diese Vorlage kann man mit den URLs von Cardmarket füllen.
- `--pause`: Unterbricht die Ausführung nach jeweils 15 Karten, um die Erkennung durch Cardmarket zu verhindern (Standard: True). [evt. verbugged, wenn flag gesetzt wird, wird es wieder auf True gesetzt ^^]

### Erster Aufruf:
Erster Aufruf zeigt die Hilfe an und bricht danach ab. Ein file `.cache` wird erstellt (auf Linux versteckt), was nur zeigt ob das Program einmal ausgefuehrt wurde und sonst (noch) keinen Zweck hat.
Das ist kein Bug, das ist ein Feature ;)

### Beispielaufruf 1:
```bash
python cm-scraper.py --path input.xlsx --output output.xlsx --jump_over_filled --sleep 5
```
Das Program oeffnet `input.xlsx`, springt über schon befuellte Zellen und pausiert zw. 5.5 und 6.5 Sekunden (addiert die gegebene Zahl hinzu) zwischen jeder Karte. Anschließend wird das Ergebnis in `output.xlsx` ausgegeben.

### Beispielaufruf 2:
Befehl um eine Vorlage mit Standardspalten zu generieren. Erstellt im `xlsx` Ordner das File `Vorlage.xlsx`.
```bash
python cm-scraper --create
```
Das erstellte File kann mit URLs zu den Karten befüllt werden und mit
```bash
python cm-scraper.py
```
sofort ohne weitere Argumente verwendet werden. Das Ergebnis befindet sich dann in `xlsx/Ergebnis.xlsx`. 

