Input (Thorben)
=====

**💡 Læringsmål:** _I dette avsnittet skal du lære deg å få inn data fra brukeren._

Fram til nå har vi skrevet tekst fra programmet til terminalen.
Men hvis du har villet endre hvilke verdier programmet ditt opererte på,
så har du måttet gå inn i koden og gjøre endringene der.

Hadde det ikke vært mer praktisk hvis du kunne latt koden være den samme,
og heller _spurt brukeren_ om hvilke verdier du skal bruke?
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


## Snarvei for å stille spørsmålet og hente svaret samtidig

Det finnes en snarvei du kan bruke for å stille spørsmålet som brukeren
skal svare på i samme slengen som du henter svaret: `input(prompt)`.
Teksten du sender inn vil bli skrevet til terminalen (likt som med `print`),
men den vil ikke avslutte med linjeskift.
Resultatet er at når brukeren begynner å skrive,
vil svaret stå på samme linje som spørsmålet.

Grunnen til at du helst bør bruke en prompt,
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


## Lese inn andre typer enn streng

Hittil har vi kun lest inn strenger med `input()`.
Og det er i grunn det eneste `input()` kan gi oss: strenger.

La oss si at vi vil lese inn brukerens alder, i tillegg til navn.
Her er første utkast:

```python
# input_alder_feil.py
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
Hva skjer? Kan du se hvorfor?_

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


## Stille ja/nei-spørsmål

Du kan ofte ha behov for å stille kontrollspørsmål til brukeren.
Det kan for eksempel være at du vil spørre om bekreftelse før du overskriver ei fil.


### Hvorfor ikke `bool(x)`?

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

### Eksempel på problemløsing: Tolke ja/nei-svar

Hvis vi skal få til å tolke svaret på ja/nei-spørsmål,
må vi i grunn gjøre en god del arbeid.
La oss starte med å lage en liste med krav:

* `"y"`, `"Y"`, `"Yes"` og `"yes"` skal tolkes som `True`
* `"n"`, `"N"`, `"No"` og `"no"` skal tolkes som `False`
* Hvis du bare trykker `[ENTER]` skal du bruke en forvalgt verdi

Dette er ganske mange krav...
I stedet for å skulle løse alt på én gang,
er det enklere å bare starte med én bit.
La oss starte med å bare godta `"y"` for `True`, og anta alt annet som `False`.

#### Runde 1: Godta kun y som «ja»

```python
# input_ja_nei_v1.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ")
vil_fortsette_tolket = vil_fortsette == "y"
print(f"{vil_fortsette_tolket=}")
```

I spørsmålet har vi skrevet `(Y/n)`.
Dette kommuniserer to ting til brukeren:

1. Vi stiller et yes/no-spørsmål
2. Hvis du bare trykker `[ENTER]`, vil programmet anta svaret er `"yes"`

Hvis vi derimot hadde skrevet `(y/N)` ville vi kommunisert at forvalget hadde vært `"no"`.
(Legg merke til hvilken bokstav som er stor.)

En annen teknikk vi har brukt,
er å sette likhetstegn etter uttrykket som vi ønsker å vise frem i f-strengen:

```python
f"{vil_fortsette_tolket=}"
```

Dette er en snarvei som vil vise _både_ uttrykket du har brukt _og_
resultatet av uttrykket.
For eksempel vil det stå `vil_fortsette_tolket=True` hvis du svarte `y`.

Hvis du prøvekjører dette programmet i terminalen,
vil du fort nok oppdage tre feil:
* `"Y"` (en stor y) blir tolket som `False`
* `"yes"` blir tolket som `False`
* Hvis du bare trykker `[ENTER]` får du `False`, selv om forvalget er `True`.

La oss prøve å løse det første problemet først.


#### Runde 2: Ignorer store/små bokstaver

Hvis vi konverterer til [minuskler][minuskel] (små bokstaver) først,
kan vi beholde sammenlikningen som den er.

```python
# input_ja_nei_v2.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ")
# Ignorer forskjellen på store og små bokstaver ved å
# normalisere til små bokstaver
vil_fortsette_minuskler = vil_fortsette.lower()
vil_fortsette_tolket = vil_fortsette_minuskler == "y"
print(f"{vil_fortsette_tolket=}")
```

Nå gjenstår kun to problemer.
La oss gå løs på problemet med at `"yes"` blir tolket som `False`.

#### Runde 3: Godta yes som «ja»

```python
# input_ja_nei_v3.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ")
vil_fortsette_minuskler = vil_fortsette.lower()
# Ignorer alle bokstaver etter den første
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

#### Runde 4: Ikke krasj ved tom verdi

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
# Fortsett med å ignorere alle tegn etter det første,
# men la en tom streng forbli tom
vil_fortsette_forbokstav = vil_fortsette_minuskler[0:1]
vil_fortsette_tolket = vil_fortsette_forbokstav == "y"
print(f"{vil_fortsette_tolket=}")
```

Legg merke til at `[0:1]` kan forkortes til `[:1]`, siden starten er `0`.

`vil_fortsette_forbokstav` vil bli satt til det første tegnet hvis det finnes,
ellers en tom streng.

Det siste problemet som gjenstår er å få `True` som forvalg.

#### Runde 5: Godta tom verdi som «ja»

```python
# input_ja_nei_v5.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ")
vil_fortsette_minuskler = vil_fortsette.lower()
vil_fortsette_forbokstav = vil_fortsette_minuskler[:1]
# Aksepter tom streng, i tillegg til "y", som sann
vil_fortsette_tolket = (
    vil_fortsette_forbokstav == "y"
    or vil_fortsette_forbokstav == ""
)
print(f"{vil_fortsette_tolket=}")
```

Det er fortsatt en svakhet her:
Du kan skrive hva som helst,
og det vil bli tolket som «nei» så lenge det ikke starter på bokstaven y.
Vi kunne valgt å kjefte på brukeren hvis de gjorde noe så tullete,
men for enkelthetens skyld antar vi heller at brukeren ikke vil fortsette.

#### Runde 6: Trekk sammen til ei linje

Nå har vi gjort én ting av gangen i dette eksemplet,
men du kan ta noen snarveier og få til det samme i færre kodelinjer:

```python
# input_ja_nei_v6.py
print("La oss late som at programmet ønsker å opprette ei fil.")
vil_fortsette = input("Vil du fortsette (Y/n)? ").lower()[:1] in ("y", "")
print(f"{vil_fortsette=}")
```

Her har vi gjort alle mellomstegene samtidig.
Vi har også brukt `in`-operatoren til å sjekke om uttrykket på venstre hånd
(den første bokstaven til brukeren som minuskel)
er å finne i tuplen av verdier på høyre hånd (`"y"` eller `""`).

Programmet oppfører seg helt likt som versjon 5,
det er bare litt vanskeligere å lese,
men desto kortere.
Balansegangen mellom «lettforståelig, men langt» og «kort, men vanskelig å lese»
kan være vanskelig å få rett.
I dette tilfellet hadde nok den beste løsninga vært å bruke den lange varianten,
men gjemt den bort som en gjenbrukbar funksjon.
Da tar den liten plass der hvor du spør brukeren om hen vil fortsette,
samtidig som du kan gå til den lange versjonen
når du trenger å tilpasse den eller se hvordan den funker.
Du lærer deg hvordan du kan lage slike funksjoner helt i slutten av denne delen.

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
