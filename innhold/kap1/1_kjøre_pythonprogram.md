Hei på deg Python
=================
**💡 Læringsmål:** _I dette kapitlet skal du lære deg å kjøre Python-programmer i terminalen._

Når man lærer seg et programmeringsspåk, er ofte det første programmet man skrivet et ["Hallo verden"-program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program). Dette er helt enkelt et program som skriver ut teksten "Hallo verden". La oss skrive et sånt program sammen!

Filer og mapper
---------------
Filer bor i mapper, og det kan være nyttig å lage en mappe som inneholder alle filene du skal lage i dette kurset. Vi kommer til å bruke en mappe som heter `kurs/` i denne kursbeskrivelsen. I denne mappen kan du lage en fil som heter `hallo_verden.py`. Når du har gjort det, kan du åpne filen i VS Code, og legge inn koden som er vist under:

```python
print("Hallo verden")
```

Når du har lagt inn koden i filen, lagrer du den og starter en terminal som [Powershell på Windows](https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell), [Terminal på Mac](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac) eller noe tilsvarende på Linux.

I den åpne terminalen, navigerer du ned i `kurs/`-mappen med f.eks. kommandoen `cd`.

```shell
$> cd kurs/
kurs $>
```

_Det kan være du må navigere lenger enn bare rett ned i `kurs/`-mappen på din maskin. Dette er avhengig av hvilken mappe terminalen åpnet seg i. For å gå ut av en mappe kan man bruke kommandoen `cd ..`. Avhengig av hvilket operativsystem du bruker, kan det også være mulig å åpne terminalen direkte i `kurs/`-mappen, fra filutforskeren._

Da skal vi kjøre Pythonkoden! Dette gjør du helt enkelt ved å kjøre kommandoen `python`

```shell
kurs $> python hallo_verden.py
Hallo verden
```

_Hvis du bruker Linux, kan det være at du må kjøre kommandoen `python3` i stedet for `python`. Hvis dette er tilfellet, bruker du bare denne kommandoen alle steder hvor det er referert til `python` i denne kursbeskrivelsen._

Gratulerer! Du har nå kjørt ditt første Pythonprogram.

Sånn printer du til terminalen
------------------------------
I programmet over brukte vi funksjonen `print(...)` til å skrive tekst til terminalen. Dette er ofte den enkleste måten å vise frem data. Man kan skrive tekst til terminalen med `print(...)` stort sett hvor som helst i et program, så denne funksjonen kan være nyttig i mange sammenhenger.

`print(...)` er et eksempel på en innebygget funksjon i Python. Funksjoner skal vi lære mer om senere i kurset, blant annet hvordan du kan lage dine egne funksjoner, men nå i første omgang kan vi notere oss tre ting:
1. Funksjonen har ett navn, `print`, og dette navnet står først, sånn at Python forstår hvilken funksjon vi ønsker å bruke.
2. Parentesene etter funksjonsnavnet, står rundt teksten vi sender inn til funksjonen, sånn at Python vet hvilke tekst vi ønsker å skrive til terminalen.
3. Selve teksten er skrevet med anførselstegn (`"`). Dette forteller Python at det her er snakk om tekst, og ikke mer programkode.

✍️ **Oppgave:** _Kan du utvide `hallo_verden.py`, sånn at den printer ut en tekst til?_
