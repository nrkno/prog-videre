Dag 0: Introduksjon til Python
==============================
_Hei og velkommen til Pythonkurs for viderekomne! Som en myk start, skal vi se litt på hvordan man bruker Python, og de helt enkle verktøyene som finnes i dette programmeringsspråket._

Hei på deg Python
-----------------
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å kjøre Python-programmer i terminalen._

Når man lærer seg et programmeringsspåk, er ofte det første programmet man skrivet et ["Hallo verden"-program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program). Dette er helt enkelt et program som skriver ut teksten "Hallo verden". La oss skrive et sånt program sammen!

### Filer og mapper
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

### Sånn printer du til terminalen
I programmet over brukte vi funksjonen `print(...)` til å ...

_Her forklarer vi litt hvordan print fungerer, og en veldig kort forklaring på hva en funksjon er og gjør._

✍️ **Oppgave:** _Kan du utvide `hallo_verden.py`, sånn at den printer ut en tekst til?_


Kommentarer (Teodor)
-----------
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å skrive forklaringer som kan ligge sammen med koden._

_Her forklarer vi at du kan kommentere med forklarende tekst, og at du kan "kommentere ut" kodelinjer og kanskje også multiline-kommentarer_

✍️ **Oppgave:** _Kan du skrive en kommentar på hva du prøver å få til med en `print`-linje i `hallo_verden.py`_
<!-- TODO: Kanskje dette kan være eksemplet vårt? -->

✍️ **Oppgave:** _Kan du kommentere ut en `print`-linje i `hallo_verden.py`, og observere hva som da skjer når du kjører programmet?_


Enkle datastrukturer og variabler (Teodor)
---------------------------------
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke enkle datastrukturer som tall, tekst og boolske verdier. I tillegg skal vi se litt på variabler._

### Tall
- Operasjoner som `+`, `-`, `*`, `%`, `**`, `/` og `//`.
- Typer tall `int`, `float`.

### Variabler
- Tilegne verdier til en variabel
- Gyldige variabelnavn
  - Inkludert æøå?
- gode variabel navn `sesong_nummer = 4`
    - tips om finne gode variabelnavn ved å se det variabelen skal brukes til
- Bruke en variabel
- `i = 2` `i +=1 `

```python
i = 14
print(i)
i = 45
print(i)
a = 2
b = 3
c = a + b
```

### Strenger
- Hvordan lager du de? `"`
- Kunne escape enkelte tegn
- Multiline-strenger `'''`
- Hvordan gjør
- `contains`, `split`, `in`
- Bruke programID som eksempel
- Bruke medvirkende som eksempel
    - Sørge for stor forbokstav osv.
- Vise hvordan man bruker f-strenger
    - _Du kan også bruke `+` for å konkatinere strenger, men f-strenger er anbefalt_
- https://docs.python.org/3/library/string.html

### Boolske verdier
- `True`, `False`, and or not, hvordan parenteser kan påvirke ting

| `a`     | `b`     | `a and b` |
| ------- | ------- | --------- |
| `True`  | `False` | `False`   |
| `False` | `True`  | `False`   |
| `False` | `False` | `False`   |
| `True`  | `True`  | `True`    |

| `a`     | `b`     | `a or b` |
| ------- | ------- | -------- |
| `True`  | `False` | `True`   |
| `False` | `True`  | `True`   |
| `False` | `False` | `False`  |
| `True`  | `True`  | `True`   |

| `a`     | `not a` |
| ------- | ------- |
| `True`  | `False` |
| `False` | `True`  |

- Faske og sanne verdier f.eks. `not 0`
- Kortslutning av boolske uttrykk

```python
a = True
c = a or b
print(c)
```

```python
a = ""
b = "hei igjen"
c = a or b
```

Input (Thorben)
-----
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å få inn data fra omverdenen._

- Vise hvordan du kan hente tekst fra bruker

```python
navn = input("Hva heter du?> ")
print(f"Hei {navn}!")
alder = input("Hvor gammel er du?> ")
neste_alder = alder + 1
# Se at dette kræsjer, forklare problemet og hvordan det kan løses med int.
# Hva skjer om bruker taster inn noe som ikke er tall? hvordan løse det?
# motivasjon til hvis omatte å sjekke hva input er før man prøver å caste string.isnumeric()
print(f"Så fint, da er du {neste_alder} om et år!")
```

Hvis, omatte og ellers (Thorben)
----------------------
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å skrive kode som gjør valg._

- Hvis/omatte/ellers
- if, else, elif
- forklare kolon/inntrykk

```
if
```

```python
a = ""
c = "hei igjen"
if a:
    c = a
```

```python
d = "a er sann" if a else "a var usann"
```

Samlinger (Per Edvard)
---------
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke datastrukturer som samler flere forskjellige ting._

- Datastrukturer og operasjoner på de:
    - Tupler
    - Lister
    - Oppslagstabeller
- Enkle generatorer som `range`
- dictionary .get
    - `None`
- Eksempler man kan dekke:
    - Lage liste / oppslagstabell
        - Lage tom liste + sette inn elementer.
        - Lage en liste med innhold i med en gang.
    - Hente element
    - Metadata om et program kan f.eks. ligge i en oppslagstabell.
    - Utsnitt av lister.

Løkker (Per Edvard)
------
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke løkker for å gjøre ting flere ganger._

- `for element in samling:`
    - Vi kan f.eks. printe ut alle elementene i en samling til terminalen.

- `while`
    - Vi kan også bygge opp en liste med programkoder fra bunnen
        - Bygge opp input fra consol



Funksjoner (Heidi)
----------
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke funksjoner for dele opp koden i mindre biter og for å kunne bruke samme kodebit flere steder._

Funksjoner i programmering ligner på funksjoner man lærte om i matematikken på skolen. Matematiske funksjoner tar inn en verdi og gir en verdi tilbake. 

| `x`     | `f(x) = x - 2` |
| ------- | -------------- |
| `4`     | `4 - 2 = 2`    |
| `2`     | `2 - 2 = 0`    |
| `0`     | `0 - 2 = -2`   |

Funksjoner brukes til å abstrahere vekk detaljer så man i lengre programmer ikke behøver å forholde seg til alle ting hele tiden. I stedet kan man dele koden opp i flere funksjoner, og trenger bare å  vite navnet på funksjonen og verdiene den eventuelt trenger som input, på det stedet der man vi bruke funksjonen. Det er litt på samme måte som i en matoppskrift, det er ikke alle detaljer som forklares hele tiden. Om det for eksempel står "kok opp 2 liter vann" i oppskriften er det vanligvis ikke forklart hvordan man koker vann.

Funksjoner gjør at man ikke trenger å gjenta kodelinjer som skal gjøre neste det samme. Da er det bedre å ha denne samme funksjonaliteten ett sted: Man trenger man bare å forsikre seg ett sted om at funksjonaliteten er som forventet, og om man trenger å endre funksjonaliteten senere en gang, er det bare ett sted man trenger å oppdatere.

En funksjon i Python ser ut på følgende måte:

```python
def lag_hilsen(navn):
    hilsen = f"Hei {navn}!"
    return hilsen
```
Første linje i funksjonen består av nøkkelordet `def` som angir at her starter definisjonen av funksjonen. Teksten som kommer etterpå er navnet på selve funksjonen, deretter kommer parametrene inni parentesen, før linja avsluttes med `:`. Hvis funksjonen ikke skal ta inn noen verdier er det tomt mellom parentesene `()`, hvis funksjonen har flere parametre er de separert med med komma `(fornavn, etternavn)`. Parametrene brukes som variable inni funksjonen og en parameter vil inneholde verdien som angis når man bruker funksjonen, det som sendes inn som argument til funksjonen.

Selve innholdet i funksjonen kommer på linja etter `:`, og alt som skal være inni funksjonen må ha et innrykk. Til sist i funksjonen returneres verdien man vi ha tilbake fra funksjonen ved å skrive `return` etterfulgt av det man vil returnere. Funksjoner i Python må ikke ha en eksplisitt returverdi, om det ikke er noen linje med `return` til slutt, vil funksjonen implisitt returnere verdien `None`.

Lag en ny Python-fil, f.eks med navn `funksjoner.py`, og kopier funksjonen over inn i fila. Deretter kan du i fila kalle funksjonen og lagre resultatet i en variabel, og så printe resultatet:

```python
hilsen = lag_hilsen("Jens")
print(hilsen)
```

Bytt ut navnet med ditt eget navn, og prøve å kalle funksjonen flere ganger med forskjellige navn. 

Når man skal sende inn argument til en funksjon kan man eksplitt navngi parameteren. Det er spesielt nyttig når man har flere argumenter, så man er sikker på at riktig parameter får riktig verdi. I eksempelet kan man derfor skrive:

```python
hilsen = lag_hilsen(navn = "Jens")
```

I eksempelet er  `navn` en parameter og `Jens` er et argument for funksjonen `lag_hilsen`.

Test å legge til eller endre noe i funksjonen du har i skriptet. Klarer du å endre funksjonen så programmet feiler når du kjører det? Hvorfor feiler det?

✍️ **Oppgave:** _Lag en funksjon som skriver ut hjelp til terminalen_

1. Lag funksjonen `print_hjelp()` som ikke tar inn noe argument og som ikke returnerer noen verdi. Bruk `print()`-funksjonen til å skrive ut en valgfri setning om hjelp til terminal.
2. Kall funksjonen i programmet, og se at hjelpeteksten skrives ut når programmet kjører.
3. Lagre returnverdien fra funksjonen i en variabel, for eksempel `hjelp = print_hjelp()`, og print ut denne variabelen. Hva skrives ut?
4. Prøv å legge inn en eksplisitt `return None` i slutten av programmet, hva skrives ut fra variabelen nå?

✍️ **Oppgave:** _Lag en funksjon som setter lager bærer fra programkode og type_
 Tv- og radioprogram har en programkode (eller programid) består av fire bokstaver og åtte tall, for eksempel `KMNO10010922`. En type bærer består av to bokstaver, for eksempel `AH`, og et program sin bærer består av programkoden til programmet satt sammen med bærertypen.

1. Lag funksjonen `lag_bærer(programkode, bærertype)`. Denne har to parametere, `programkode` og `bærertype`, og skal returnere en streng der programkode og bærertype er satt sammen.
2. Kall funksjonen i programmet og se at verdien som returneres er som du forventer.

✍️ **Oppgave:** _Lag en funksjon som splitter opp en bærer_

1. Lag funksjonen  `del_opp_bærer(bærer)` som er motsatt av `lag_bærer(programkode, bærertype)`. Den skal ta inn en bærer, og dele denne opp i `programkode` og `bærertype`, og returnere disse to verdiene. Funksjoner kan bare returnere en ting, så en måte å returnere flere ting på er å sette de sammen til et tuppel.
2. Kall funksjonen i programmet og se at verdien som returneres er som du forventer.
3. Prøv å kombinere de to bærer funksjonene, kall først `lag_bærer` og  bruk resultatet herfra som argument til `del_opp_bærer`, og motsatt, kall `del_opp_bærer` og  bruk resultatet herfra som argument til `lag_bærer`. Hvordan forventer du at disse funksjonene fungerer sammen?

✍️ **Oppgave:** _Rydd opp i programmet_

Rydd opp i programmet slik at man unngår at samme funksjonalitet kodes på ulik måte, og ikke har funksjonalitet duplisert i koden. Bruk minst én av bærer-funksjonene over, du kan også lage nye funksjoner der du synes det passer.

```python
program1_kode = "DVFJ60000121"
program1_bærertype = "AH"
program1_bærer = program1_kode + program1_bærertype

program2_kode = "ODRP20002101"
program2_bærertype = "AB"
program2_bærer = "ODRP20002101AB"

program3_kode = program1_kode
program3_bærer = program3_kode + "AA"

programmer = [
    {
        "kode": program1_kode,
        "bærertype": program1_bærertype,
        "bærer": program1_bærer
    },
     {
        "kode": program2_kode,
        "bærertype": program2_bærertype,
        "bærer": program2_bærer
    },
     {
        "kode": program3_kode,
        "bærertype": program3_bærer[-2:],
        "bærer": program3_bærer
    }
]

print(programmer)
```
