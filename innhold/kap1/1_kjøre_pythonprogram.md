Hei på deg Python
=================
**💡 Læringsmål:** _I dette kapitlet skal du lære deg å kjøre Python-programmer i terminalen._

Når man lærer seg et programmeringsspåk, er ofte det første programmet man skrivet et ["Hallo verden"-program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program). Dette er helt enkelt et program som skriver ut teksten "Hallo verden". La oss skrive et sånt program sammen!


Hva er Python?
--------------

Python er et programmeringsspråk som fikk sin spede begynnelse i juleferien til nederlenderen Guido van Rossum i 1989.
Han publiserte prosjektet på internett (Usenet) i 1991, og det har siden blitt etablert en ideell stiftelse som videreutvikler og forvalter Python.
Guido van Rossum tok navnet fra et manuskript han leste i tida rundt da prosjektet startet, nemlig _Monty Python's Flying Circus_.

Språket er i dag mye brukt i introduksjonskurs i programmering.
Det er likevel ikke begrenset til lek og undervisning; Python er mye brukt innenfor områder som vitenskap, maskinlæring (KI), og nettsideutvikling.

[Les mer om Python på Store norske leksikon](https://snl.no/Python_-_programmeringsspr%C3%A5k).


Python som programmeringsspråk
------------------------------

Når vi programmerer Python, lager vi vanligvis tekstfiler med instruksjoner skrevet i Python-programmeringsspråket.
Filene har filendelsen `.py`.
Språket følger en bestemt _syntaks_, som sier noe om hvordan gyldig Python-kode skal se ut, og en _semantikk_, som sier noe om hva datamaskinen skal gjøre når den kjører koden.

Python-kode kan skrives i et hvilket som helst program som produserer rene tekstfiler, som for eksempel Notepad/Notisblokk på Windows.
Vi anbefaler dog at du bruker et verktøy som er spesialdesignet for å skrive Python-kode, siden du får hjelp til å se hvordan koden blir tolket av datamaskinen.
[Introduksjonen til kurset](../README.md) har anbefalinger for deg som ikke har en kodeeditor fra før.


Python som dataprogram
----------------------

Python er _også_ navnet på et dataprogram, som formelt sett heter CPython.
For å faktisk _kjøre_ koden du har skrevet starter vi Python-programmet, og ber det om å tolke tekstfila vi har skrevet og utføre instruksjonene der.
Det finnes også andre dataprogram som kan kjøre Python-koden vi skriver, men vi holder oss til CPython her.

[I introduksjonen](../README.md) står det instruksjoner for hvordan du kan installere Python-dataprogrammet.
Når det er installert, skal vi kunne starte det fra _terminalen_.


### Kjøre Python i terminalen

Start en terminal som [Powershell på Windows](https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell), [Terminal på Mac](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac) eller noe tilsvarende på Linux.
Du vil få et nesten tomt vindu med en blinkende markør.
Terminalen venter på at du skal skrive en kommando som den skal kjøre.

I hele dette kurset skal vi starte Python-dataprogrammet fra terminalen.
Men nøyaktig _hva_ programmet heter, kommer an på hvilket operativsystem du bruker, og hvordan du har installert Python.

| OS      | Installasjonsmåte | Navnet på Python-dataprogrammet |
|---------|-------------------|---------------------------------|
| Windows | Python.org        | `py`                            |
| Windows | Filewave          | `python`                        |
| Windows | Windows Store     | `python`                        |
| Linux   | Pakkebehandler    | `python3`                       |
| MacOS   | Python.org        | `python3`                       |

I alle eksemplene kommer vi til å kalle programmet for `python`, men det bytter du bare ut med riktig navn når du kjører kommandoer hos deg.

La oss teste at Python er installert ved å skrive `python --version` i terminalen og trykke `[ENTER]`:

```shell
> python --version
Python 3.10.2
```

Du vil sannsynligvis få en annen versjon hos deg, men så lenge den er nyere enn eller lik 3.8 skal alle delene av kurset fungere.


### Mulige feil og løsninger når du kjører Python i terminalen

* Når jeg kjører `python --version` får jeg til svar `Python 2.7` eller en annen gammel variant
  * Prøv å kjøre `python3` i stedet for `python`:

    ```shell
    > python3 --version
    Python 3.10.12
    ```
    
* Jeg får feilmelding `Python ble ikke funnet; kj°r uten argumenter for Õ installere fra Microsoft Store, eller deaktiver denne snarveien fra Innstillinger > Administrer app utf°relses aliaser.`
  * Har du installert fra Python.org? Prøv å kjøre med `py` i stedet for `python`:

    ```shell
    > py --version
    Python 3.11.5
    ```

* Jeg får feilmelding `python: command not found` eller `python: The term 'python' is not recognized as a cmdlet, …`
  * Prøv med andre varianter, som `py` eller `python3`
  * Er du sikker på at du har installert Python?
  * Det kan hende Python ligger i ei mappe som terminalen ikke er satt opp til å søke i.
    Prøv å installere på nytt, men huke av for valg om å legge til Python i "PATH".
  
* Jeg får feilmelding fra `py` om at `No suitable Python runtime found`
  * På Windows blir Python-installasjonen vanligvis installert personlig.
    Åpnet du terminalen med den samme brukeren som du installerte Python med?
  * Du kan eventuelt installere Python på nytt, men velge «Customize install» – da kan du velge å installere Python for alle brukerne på maskinen, og ikke bare din egen.
  * Du kan også få denne feilmeldingen hvis du har installert fra Python.org, men seinere fjernet Python-installasjonen.
    Da kan `py` bli liggende igjen.
    Prøv å installere på nytt.


Interaktiv Python: Test ut ting rett i terminalen
-------------------------------------------------

<!-- TODO: Skriv om hvordan teste Python interaktivt -->


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

Da skal vi kjøre Pythonkoden! Dette gjør du helt enkelt ved å kjøre kommandoen `python`:

```shell
kurs $> python hallo_verden.py
Hallo verden
```

_Hvis du bruker Linux eller Mac, kan det være at du må kjøre kommandoen `python3` i stedet for `python`. Hvis dette er tilfellet, bruker du bare denne kommandoen alle steder hvor det er referert til `python` i denne kursbeskrivelsen._

Gratulerer! Du har nå kjørt ditt første Pythonprogram.

Sånn printer du til terminalen
------------------------------
I programmet over brukte vi funksjonen `print(...)` til å skrive tekst til terminalen. Dette er ofte den enkleste måten å vise frem data. Man kan skrive tekst til terminalen med `print(...)` stort sett hvor som helst i et program, så denne funksjonen kan være nyttig i mange sammenhenger.

`print(...)` er et eksempel på en innebygget funksjon i Python. Funksjoner skal vi lære mer om senere i kurset, blant annet hvordan du kan lage dine egne funksjoner, men nå i første omgang kan vi notere oss tre ting:
1. Funksjonen har ett navn, `print`, og dette navnet står først, sånn at Python forstår hvilken funksjon vi ønsker å bruke.
2. Parentesene etter funksjonsnavnet, står rundt teksten vi sender inn til funksjonen, sånn at Python vet hvilke tekst vi ønsker å skrive til terminalen.
3. Selve teksten er skrevet med anførselstegn (`"`). Dette forteller Python at det her er snakk om tekst, og ikke mer programkode.

✍️ **Oppgave:** _Kan du utvide `hallo_verden.py`, sånn at den printer ut en tekst til?_
