# kif-letter
###### v0.3.0

Dieses Script parst Namen verschiedener Websites, erstellt den Rahmen für einen Serienbrief und fügt als Text eine Resolution und eventuelle weitere Texte aus TeX-Dateien ein.

#### Currently supported features

 * Parsen alle Namen und Geschlechter einer Tabelle bei Wikipedia
 * Erstellen eines TeX-Datei-Rahmens für den Brief
 * Plugin-Schnittstelle für weitere `NameParser`
 * Offline-Guessing des Geschlechts, soweit nach Parsen der Seite unbekannt
 
#### Future features

 * Mehr vorgefertigte Parser
 * Bessere NameDB
 

### Usage

 ```
 kif_letter.py -o OUTFILE -p PARSERNAME [URL]
 ```
wobei
 * `OUTFILE` der Pfad zur zu erstellenden TeX-Datei ist.
 * `PARSERNAME` die Werte `bundestag` und `wikitable` haben kann.
   * Bei `wikitable` muss zudem eine URL zu einer Namens-Tabelle bei `https://de.wikipedia.org` gegeben und `config.toaddress` definiert sein.


### Dependencies

 * `python3`
 * `setuptools`
 * `urllib`
 
 
### License

The MIT License (MIT)

* Copyright (C) 2015 Sebastian Lau
* Copyright (C) 2015-2016 KIF e.V. (Sebastian Lau)
