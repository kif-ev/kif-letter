# kif-letter
###### v0.1.0

Dieses Script parst alle Abgeordneten des Bundestages, erstellt den Rahmen für einen Serienbrief und fügt als Text eine Resolution und eventuelle weitere Texte aus TeX-Dateien ein.

#### Currently supported features

 * Parsen aller Namen aller Abgeordneten des Bundestages (und feststellen des Geschlechts, bis api_limit von genderize.io erreicht ist)
 * Erstellen eines TeX-Datei-Rahmens für den Brief
 * Plugin-Schnittstelle für weitere `NameParser`
 * Offline-Erkennung des Geschlechts, soweit Name bekannt
 
#### Future features

 * Bessere Name-DB
 

### Usage

 ```
 kif_letter.py -o OUTFILE -p PARSERNAME
 ```
wobei
 * `OUTFILE` der Pfad zur zu erstellenden TeX-Datei ist
 * `PARSERNAME` den Wert `bundestag` haben kann


### Dependencies

 * `python3`
 * `codecs`
 * `setuptools`
 * `urllib`
 
 
### License

The MIT License (MIT)

Copyright (c) 2015 Sebastian Lau
Copyright (C) 2015-2016 KIF e.V.
