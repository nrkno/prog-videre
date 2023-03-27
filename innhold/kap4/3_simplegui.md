Simple GUI (Teodor)
==========

installasjon og dokumentasjon

Notater fra evaluering av PySimpleGUI
-------------------------------------
### Installasjon
[Dokumentasjonen](https://www.pysimplegui.org/en/latest/) beskriver følgende installasjon:
```shell
$> pip install pysimplegui
# eller
$> pip3 install pysimplegui
```

På Ubuntu 22.04.2 LTS var ikke dette tilstrekkelig, da forsøket på å kjøre det første eksempelet feilet med `ModuleNotFoundError: No module named 'tkinter'`.

Litt [graving på GitHub](https://github.com/PySimpleGUI/PySimpleGUI/issues/5684) avdekket at man noen steder trenger å installere tkinter manuelt:
```shell
$> sudo apt install python3-tk
```

Etter denne pakken var installert, var det mulig å kjøre eksempelet uten feil.

_Hvis vi velger å bruke PySimpleGUI bør vi nok skrive en installasjonsguide og teste denne på Windows, Mac og Linux._

### Bruk
- Forsøker å lage et enkelt tre-på-rad spill.
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) er spesielt nyttig.
- Det samme er det å ha installert Python-utvidelse til VS Code og huske på at debugging finnes.
- [Eksemplene fra GitHub](https://github.com/PySimpleGUI/PySimpleGUI) og [Kokeboka](https://www.pysimplegui.org/en/latest/cookbook/) er ganske nyttige.
- [Referanse-dokken](https://www.pysimplegui.org/en/latest/call%20reference/) er heller ikke så verst.
- Man får brukbare feilmeldinger hvis noe krasjer i rammeverket.
- `F12` for å inspisere koden i rammeverket er også helt ok.
- Det er litt kjipt at alt baserer seg på å sette opp komponenter, og så mutere de i etterkant.
