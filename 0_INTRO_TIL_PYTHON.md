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

Fram til nå har vi skrevet tekst fra programmet til terminalen.
Men hvis du ville endre hvilke verdier programmet ditt opererte på,
så har du måttet gå inn i koden og gjøre endringene der.
Hadde det ikke vært mer praktisk hvis du kunne latt koden være den samme,
og heller _lest inn_ verdier fra terminalen til programmet?
Da kan du kjøre programmet ditt flere ganger, men brukt ulike verdier hver gang.

[Funksjonen `input()`][doc-input] stopper programmet ditt,
og venter på at brukeren som sitter ved terminalen skriver inn ei linje med tekst.
Først når brukeren trykker `[ENTER]` vil programmet ditt fortsette.
Resultatet til `input()` er teksten som brukeren skrev,
så hvis du vil ta vare på teksten må du tilegne den til en variabel.

Her er et program som bruker `print()` til å _skrive til_ terminalen,
etterfulgt av `input()` for å _lese fra_ terminalen:

```python
# hilsen.py
print("Hei! Hva heter du?")
navn = input()
print(f"Så hyggelig å hilse på deg, {navn}!")
```

Når du kjører dette i terminalen, kan det se sånn her ut:

```shell-session
kurs $> python hilsen.py
Hei! Hva heter du?
Vibeke
Så hyggelig å hilse på deg, Vibeke!
```

✍️ **Oppgave:**
_Eksperimenter med å kjøre eksemplet ovenfor i terminalen.
Hva skjer når du skriver inn mange mellomrom før og etter navnet?
Hva skjer hvis du ikke skriver inn noe navn før du trykker `[ENTER]`?_


### Snarvei for å stille spørsmålet og hente svaret samtidig

Det finnes en snarvei du kan bruke for å stille spørsmålet som brukeren
skal svare på i samme slengen som du henter svaret: `input(prompt)`.
Teksten du sender inn vil bli skrevet til terminalen (likt som med `print`),
men den vil ikke avslutte med linjeskift.
Resultatet er at når brukeren begynner å skrive,
vil svaret stå på samme linje som spørsmålet.

Grunnen til at du helst bør oppgi en prompt,
er at det lar brukerne av programmet ditt vite at programmet venter på dem.
Det trenger ikke alltid være så åpenbart hvorvidt programmet bare har tatt seg en tenkepause,
eller om det venter på brukeren.
For terminalprogram er det derfor en innarbeidet konvensjon om at hvis du skal ta inn noe fra brukeren,
skal du indikere det ved å la markøren stå på samme linje som spørsmålet,
eller starte linja med `> ` (altså «større enn»-tegnet etterfulgt av mellomrom).

Her er samme eksemplet som ovenfor,
gjort om til å stille spørsmålet på samme linje som brukeren skal skrive svaret:

```python
# hilsen_med_prompt.py
navn = input("Hei! Hva heter du? ")
print(f"Så hyggelig å hilse på deg, {navn}!")
```

Når du kjører dette i terminalen, kan det se sånn her ut:

```shell-session
kurs $> python hilsen_med_prompt.py
Hei! Hva heter du? Vibeke
Så hyggelig å hilse på deg, Vibeke!
```

✍️ **Oppgave:**
_Hvorfor er det et ekstra mellomrom etter spørsmålstegnet i eksemplet ovenfor?
Hva skjer hvis du fjerner det?_


### Lese inn andre typer enn streng

Hittil har vi kun lest inn strenger med `input()`.
Og det er i grunn det eneste `input()` kan gi oss: strenger.

La oss si at vi vil lese inn brukerens alder, i tillegg til navn.
Her er første utkast:

```python
# input_alder.py
print("Hva heter du?")
navn = input("> ")

print(f"Hei, {navn}! Hvor mange år er du?")
alder = input("> ")
print(f"Ok, så du er {alder} år gammel. ")

print("Klarer vi regne ut hvor gammel du vil være om et år?")
neste_alder = alder + 1
print(f"Du vil være {neste_alder} år om et år!")
```

✍️ **Oppgave:**
_Skriv av eksemplet ovenfor og kjør det i terminalen.
Hva skjer? Kan du gjette hvorfor?_

Hvis du vil lese inn noe annet enn tekst fra brukeren, for eksempel et tall,
så må du selv gjøre jobben med å konvertere brukerens svar til den riktige datatypen.
For heltall kan du gjøre det med [`int(x)`][doc-int-funk].

Her er en fungerende versjon av eksemplet ovenfor:

```python
# input_alder_fikset.py
print("Hva heter du?")
navn = input("> ")

print(f"Hei, {navn}! Hvor mange år er du?")
rå_alder = input("> ")
print(f"Ok, så du er {rå_alder} år gammel. ")

print("Klarer vi regne ut hvor gammel du vil være om et år?")
konvertert_alder = int(rå_alder)
neste_alder = konvertert_alder + 1
print(f"Du vil være {neste_alder} år om et år!")
```

Kjører du dette i terminalen, kan de se sånn ut:

```shell-session
kurs $> python input_alder_fikset.py
Hva heter du?
> Vibeke
Hei, Vibeke! Hvor mange år er du?
> 54
Ok, så du er 54 år gammel.
Klarer vi regne ut hvor gammel du vil være om et år?
Du vil være 55 år om et år!
```

✍️ **Oppgave:**
_Skriv av eksemplet ovenfor og test det ut i terminalen. 
Hva skjer hvis du leker at du er en tullebukk som skriver inn tullesvar?
Gjør programmet noen antakelser om hva brukeren skriver?_

I tillegg til `int(x)` kan du også konvertere til flyttall med [`float(x)`][doc-float-funk].


### Stille ja/nei-spørsmål

Du kan ofte ha behov for å stille kontrollspørsmål til brukeren.
Det kan for eksempel være at du vil spørre om bekreftelse før du overskriver ei fil.

Ovenfor så vi at du kan bruke `int(x)` og `float(x)` til å konvertere en streng til typen `int` eller `float`.
Hva så med boolske verdier — kan vi konvertere dem med `bool(x)`?
Vi kan teste det ut i en interaktiv Python-sesjon:

```shell-session
kurs $> python
Python 3.10.9 (main, Dec  7 2022, 01:12:00) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> bool("True")
True
>>> bool("yes")
True
>>> bool("y")
True
>>> bool("ja")
True
>>> 
```

Så langt ser jo dette lovende ut. Hva så med nei?

```shell-session
>>> bool("nei")
True
>>> bool("no")
True
>>> bool("False")
True
>>> bool("")
False
```

Oi, dette gikk visst ikke så bra.
Det eneste som ble konvertert til `False` var en tom streng.
Hva er det som skjer?

Alle objekter har en implisitt boolsk verdi,
med ulike regler for ulike typer.
For strenger så er denne implisitte boolske verdien `True`,
bortsett fra for tomme strenger — de er `False`.

Når du kaller `bool(x)`, 
får du den implisitte verdien til objektet som du sender inn.
Derfor blir `"False"` tolket til `True`:
Det er en ikke-tom streng, så da er den `True`.

Hvis vi skal få til å tolke svaret på ja/nei-spørsmål,
må vi i grunn gjøre en god del arbeid.
La oss starte med å lage en liste med krav:

* `"y"`, `"Y"`, `"Yes"` og `"yes"` skal tolkes som `True`
* `"n"`, `"N"`, `"No"` og `"no"` skal tolkes som `False`
* Hvis du bare trykker `[ENTER]` skal du bruke en forvalgt verdi

Dette er ganske mange krav...
La oss starte med å bare godta `"y"` for `True`, og anta alt annet som `False`.

```python
# input_ja_nei_v1.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ")
vil_fortsette_tolket = vil_fortsette == "y"
print(f"{vil_fortsette_tolket=}")
```

I spørsmålet har vi skrevet `(Y/n)`.
Dette sier to ting:

1. Vi stiller et yes/no-spørsmål
2. Hvis du bare trykker `[ENTER]`, vil programmet anta svaret er `"yes"`

Hvis vi derimot hadde skrevet `(y/N)` ville forvalget vært `"no"`.
(Legg merke til hvilken bokstav som er stor.)

Hvis du prøvekjører dette programmet i terminalen,
vil du fort nok oppdage tre feil:
* `"Y"` (en y som majuskel) blir tolket som `False`
* `"yes"` blir tolket som `False`
* Hvis du bare trykker `[ENTER]` får du `False`, selv om forvalget er `True`.

La oss prøve å løse det første problemet først.
Hvis vi konverterer til [minuskler][minuskel] først,
kan vi beholde sammenlikningen som den er.

```python
# input_ja_nei_v2.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ")
vil_fortsette_minuskler = vil_fortsette.lower()
vil_fortsette_tolket = vil_fortsette_minuskler == "y"
print(f"{vil_fortsette_tolket=}")
```

Nå gjenstår kun to problemer.
La oss gå løs på problemet med at `"yes"` blir tolket som `False`:

```python
# input_ja_nei_v3.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ")
vil_fortsette_minuskler = vil_fortsette.lower()
vil_fortsette_forbokstav = vil_fortsette_minuskler[0]
vil_fortsette_tolket = vil_fortsette_forbokstav == "y"
print(f"{vil_fortsette_tolket=}")
```

Vi sammenlikner fortsatt bare med `"y"`,
men det kan vi gjøre siden vi bare henter ut den første bokstaven brukeren skrev.
Vi har dog introdusert et nytt problem, for hva skjer hvis du ikke skriver noe?

```shell-session
kurs $> python input_ja_nei_v3.py
La oss late som at programmet ønsker å opprette ei fil.
Vil du fortsette (Y/n)? 
Traceback (most recent call last):
  File "input_ja_nei_v3.py", line 4, in <module>
    vil_fortsette_forbokstav = vil_fortsette_minuskler[0]
IndexError: string index out of range
```

Når vi gjør `vil_fortsette_minuskler[0]`,
antar vi at det er minst ett tegn i strengen.
Den antakelsen holder ikke når du ikke skriver inn noe før du trykker `[ENTER]`.

Kan vi tilpasse koden så den ikke gjør noen antakelser om strengen,
men heller aksepterer at den kan være tom?

Her kan vi utnytte det faktum at en _slice_ godtar en slutt forbi slutten på strengen.
Du kan eksperimentere selv i en interaktiv Python-sesjon:

```shell-session
kurs $> python
Python 3.10.9 (main, Dec  7 2022, 01:12:00) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> "yes"[0]
'y'
>>> ""[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> "yes"[0:1]
'y'
>>> ""[0:1]
''
```

Hvis vi bruker denne nyvunne kunnskapen i eksemplet vårt,
kan det bli seende sånn her ut:

```python
# input_ja_nei_v4.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ")
vil_fortsette_minuskler = vil_fortsette.lower()
vil_fortsette_forbokstav = vil_fortsette_minuskler[0:1]
vil_fortsette_tolket = vil_fortsette_forbokstav == "y"
print(f"{vil_fortsette_tolket=}")
```

Legg merke til at `[0:1]` kan forkortes til `[:1]`, siden starten er `0`.

`vil_fortsette_forbokstav` vil bli satt til det første tegnet hvis det finnes,
ellers en tom streng.

Det siste problemet som gjenstår er å få `True` som forvalg:

```python
# input_ja_nei_v5.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ")
vil_fortsette_minuskler = vil_fortsette.lower()
vil_fortsette_forbokstav = vil_fortsette_minuskler[:1]
vil_fortsette_tolket = vil_fortsette_forbokstav == "y" or vil_fortsette_forbokstav == ""
print(f"{vil_fortsette_tolket=}")
```

Nå har vi gjort én ting av gangen i dette eksemplet,
men du kan ta noen snarveier og få til det samme i færre kodelinjer:

```python
# input_ja_nei_v6.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ").lower()[:1] in ("y", "")
print(f"{vil_fortsette=}")
```

Når du kjører eksemplet, kan det se sånn her ut:

```shell-session
kurs $> python input_ja_nei_v6.py
La oss late som at programmet ønsker å opprette ei fil.
Vil du fortsette (Y/n)? No
vil_fortsette=False
```

✍️ **Oppgave:**
_La oss si at vi ønsker å_ slette _ei fil i stedet.
Da bør jo forvalget være `False`, for å unngå uhell.
Klarer du tilpasse `input_ja_nei_v5.py` sånn at den antar `False`
når brukeren bare trykker `[ENTER]` uten å skrive noe?_

✍️ **Oppgave:**
_I eksemplet ovenfor antok vi at brukeren svarte på engelsk.
Klarer du tilpasse `input_ja_nei_v5.py` sånn at brukeren kan svare på norsk (ja/nei)?_

Det er en ganske åpenbar bit som mangler i eksemplet vi har bygd ut her:
Det spiller ingen rolle om du svarer ja eller nei.
Det vil så klart skrives ulike ting til terminalen,
men programmet vil utføre de samme instruksjonene uansett hva du svarer.
Hvordan kan programmet gjøre ulike ting, avhengig av hva du svarer?

[doc-input]: https://docs.python.org/3/library/functions.html#input
[doc-int-funk]: https://docs.python.org/3/library/functions.html#int
[doc-float-funk]: https://docs.python.org/3/library/functions.html#float
[doc-bool-funk]: https://docs.python.org/3/library/functions.html#bool
[minuskel]: https://ordbokene.no/bm/38583


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
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke funksjoner for dele opp og gjenbruke kode._

- Analogier
    - Matematiske funksjoner
    - Ting som er «abstrahert bort», f. eks. hvordan vannkoking ikke forklares i oppskrift
- `def print_hjelp():`
    - Definerer en funksjon
    - Starter med en ingen argument
    - Tar med `return None`

- `def lag_bærer(programkode, bærer_type):`
    - Definerer en funksjon som tar to argumenter som input
    - Returnerer resultatet (ingen sideeffekter)

- `def del_opp_bærer(bærer):`
    - Returnere flere verdier (implisitt tuppel)
