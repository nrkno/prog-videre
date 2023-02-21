Programargumenter
=================

**💡 Læringsmål:**
_I dette kapitlet skal du bli kjent med hvordan du kan gi brukeren kontroll
over hva applikasjonen skal gjøre, uten at applikasjonen stopper opp underveis._

Hvordan kan applikasjonen din vite hvilken fil den skal lese fra?
Eller hvilken fil den skal skrive til?
Eller hva den i det hele tatt skal gjøre med innholdet i fila?

Den enkleste løsningen er å bestemme alt dette inni applikasjonen, såkalt *[hardkoding][wiki-hardcoding]*.
For eksempel kan du skrive filstien direkte i koden.
Dette kan fungere helt greit når du tester,
men det blir fort veldig upraktisk å måtte endre programmet hver gang du vil endre et parameter.

I del 0 av kurset var vi innom [`input()`-funksjonen][doc-input],
som lar deg stille brukeren et spørsmål som hen må svare på før programmet fortsetter.
Dette fungerer bra for interaktive applikasjoner der brukeren skal sitte parat ved tastaturet hele veien,
men det er ofte mye mer praktisk for brukeren å kunne bestemme alt dette helt i starten,
og så gjøre noe annet mens det kjører.


## Anatomien til en kommando

Du har så langt brukt terminalen til å kjøre kommandoer,
men har du tenkt over hvordan disse kommandoene er bygd opp?

Vi kan starte med kommandoen du bruker for å kjøre et Python-skript:

<!-- skriv_til_fil.py her er ment å være samme navn som er brukt i eksemplet ovenfor -->

```shell-session
kurs $> python skriv_til_fil.py
```

Denne består av to deler som er atskilt med mellomrom:

* `python`: Dette er navnet på, eller filstien til, programmet vi ønsker å kjøre
* `skriv_til_fil.py`: Dette er argumentet som blir gitt til `python`-kommandoen

**Mellomrom er meningsbærende**: De skiller mellom de ulike delene av en kommando.
Hvis du lager ei fil der navnet inneholder et mellomrom,
må du derfor bruke hermetegn for å indikere at mellomrommet _ikke_ skiller mellom to argument,
men i stedet inngår i ett og samme argument.

Her er en kommando som vil bli tolket feil:

```shell-session
kurs $> python skriv til fil.py
python3.10: can't open file '/home/n123456/kurs/skriv': [Errno 2] No such file or directory
```

Denne kommandoen består av fire deler:

* `python`: Programmet vi ønsker å kjøre
* `skriv`: Dette er det første argumentet som blir gitt til `python`-programmet.
  Python-programmet vil tolke det første argumentet som en filsti til skriptet som skal kjøres.
* `til`: Dette er det andre argumentet som blir gitt til `python`-programmet.
  Python vil sende dette argumentet videre til skriptet som heter `skriv`.
* `fil.py`: Dette er det tredje argumentet som blir gitt til `python`-programmet.
  Python vil sende dette argumentet videre til skriptet som heter `skriv`.

Selvfølgelig finnes det ikke noe skript som heter `skriv`,
så derfor feiler `python` med en feilmelding om at fila ikke finnes.

La oss bruke hermetegn rundt filstien:

```shell-session
kurs $> python "skriv til fil.py"
```

Denne kommandoen består av to deler:

* `python`: Programmet som vi ønsker å kjøre
* `skriv til fil.py`: Dette er det første argumentet som blir gitt til `python`-programmet,
  og er skriptet som vi ønsker at `python`-programmet skal kjøre


## Hvordan gi argumenter til et Python-program?

Så langt har vi kun spesifisert at vi vil kjøre `python`,
og gitt `python`-programmet ett argument.
Men du kan faktisk fortsette å skrive på kommandoen og legge til flere argumenter.

For eksempel kan du helt fint kjøre denne kommandoen:

```shell-session
kurs $> python skriv_til_fil.py "dette er en test" testefil.txt
```

Du vil ikke få noen feil, men programmet vil ikke akkurat bruke de ekstra argumentene til noe helt ennå.

✍️ **Oppgave:**
_Hvor mange argumenter inneholder kommandoen ovenfor? Hva er verdien til hvert argument?_

<details>
<summary>Fasit</summary>

Kommandoen består av fire deler, hvorav ett er programmet vi skal kjøre (`python`) og **tre** av dem er argumenter.

Argumentene er:
1. `skriv_til_fil.py`
2. `dette er en test`
3. `testefil.txt`

</details>

## Tips og triks når du skriver kommandoer i terminalen

**Autofullfør**: Når du skriver kommandoer i terminalen,
kan du bruke `[TAB]`-tasten til å fullføre argumentet du skriver på.
Hvis det du har skrevet er nok til å vite hvilken fil du tenker på,
kan du fylle ut resten med ett trykk.
Er det flere filer, må du gjerne trykke flere ganger for å få forslag eller gå gjennom forslagene.

Dette er veldig nyttig siden du ofte vil skrive filnavn i kommandoer.
Du kan bruke autofullfør både når du skal skrive hvilket skript Python-programmet skal kjøre,
og når du skal fortelle skriptet hvilken fil du vil lese fra eller skrive til.

**Historikk**: Bruk `[PILTAST OPP]` og `[PILTAST NED]` til å bla gjennom historikken.
Vil du kjøre den forrige kommandoen din én gang til,
kan du trykke `[PILTAST OPP]` én gang, etterfulgt av `[ENTER]`.
Du kan også endre på kommandoen etter at du har bladd deg opp til den,
for eksempel hvis du vil kjøre det samme med en liten endring.


## Lese argumentene til Python-skriptet

La oss starte med den innebygde måten du kan lese argumenter på.

For å nyttiggjøre deg av de ekstra argumentene brukeren skriver,
kan du importere [`sys`-modulen][doc-sys].
Deretter kan du lese argumentene fra [lista `sys.argv`][doc-sys.argv].

La oss lage et lite testeverktøy som forteller oss hvilke argumenter som finnes:

```python
# print_argumenter.py
import sys

print(sys.argv)
```

Eksempel på kjøring:

```shell-session
kurs $> python print_argumenter.py
['print_argumenter.py']
kurs $> python print_argumenter.py "dette er en test" testefil.txt
['print_argumenter.py', 'dette er en test', 'testefil.txt']
```

Var resultatet sånn som du forventet?
De ekstra argumentene som du skriver starter alltid på plass nummer 1.
Navnet på skriptet ligger alltid som argument nummer 0.

_**Sidespor**: Det kan virke litt rart at navnet på skriptet alltid er argument nummer 0,
men det kan være nyttig å ha.
La oss si at du har laget et skript som du har sendt til andre,
og at du vil skrive hjelp til terminalen for hvordan det skal brukes.
Da kan du ikke vite hvilket navn brukeren har gitt skriptet ditt.
Ved hjelp av argument nummer 0 kan du likevel bruke riktig navn på skriptet
i eksemplene du skriver til terminalen, i stedet for å hardkode navnet._


## Eksempel: Bruke `sys.argv` til å lese filnavn fra programargumentene

La oss si at vi vil lage et program som leser innholdet av ei fil,
og skriver innholdet av fila til terminalen.
Men i stedet for å hardkode navnet på fila vi skal lese fra,
eller bruke `input()` til å lese navnet fra terminalen,
så ønsker vi at brukeren skal kunne skrive filnavnet etter skriptnavnet
når hen kjører skriptet.
For eksempel:

```shell-session
kurs $> python print_fil.py NAVN_PÅ_FIL.py
```

`NAVN_PÅ_FIL.py` her vil ligge på plass nummer 1 i `sys.argv`,
siden det er det første argumentet.
Her er et rett frem eksempel på hvordan vi kan lese det inn:

```python
# print_fil.py
import sys

valgt_fil = sys.argv[1]
with open(valgt_fil) as fil:
  for linje in fil:
    print(linje, end='')
```

Eksempel på kjøring:

```shell-session
kurs $> python print_fil.py print_fil.py
import sys

valgt_fil = sys.argv[1]
with open(valgt_fil) as fil:
    for linje in fil:
        print(linje, end='')
```

PS: Du kan allerede gjøre dette i terminalen ved å bruke det innebygde programmet `cat`,
for eksempel ved å kjøre `cat print_fil.py`.

Men hva skjer hvis du glemmer å gi navnet på ei fil?

```shell-session
kurs $> python print_fil.py
Traceback (most recent call last):
  File "/home/n123456/kurs/print_fil.py", line 4, in <module>
    valgt_fil = sys.argv[1]
IndexError: list index out of range
```

Å bruke `sys.argv` rett ute av boksen går greit hvis du aksepterer skjønnhetsfeil som dette,
for eksempel hvis det bare er du som skal kjøre skriptet.
Men det er vanlig etikette å gi brukeren litt mer hjelp på veien.


## Bestepraksis for kommandolinjeprogram

Som du så ovenfor, så er det i prinsippet ingen regler for hvordan programmet ditt håndterer programargumenter.
Men det har utviklet seg en bestepraksis over tid for hvordan kommandolinjeprogram bør oppføre seg.

For det første kan du dele programargumenter i to typer:
* Posisjonelle argumenter
* Frivillige tilvalg

For det andre er det noen uskrevne regler for hvordan programmet ditt dokumenterer seg selv,
og hvordan det håndterer manglende eller ugyldige data fra brukeren.

### Posisjonelle argumenter

Den mest grunnleggende formen for programargument er argument
som får sin mening ene og alene basert på _hvor_ det står.

For eksempel har vi kommandoen `cp` (kort for _copy_) som lager en kopi av ei fil.
Den tar inn to posisjonelle argumenter: Kildefila, og den nye kopien du vil lage:

```shell
kurs $> cp print_fil.py print_fil_v2.py
```

At `print_fil.py` er kildefila, er bestemt ene og alene av at den er satt først.
Tilsvarende vet vi at `print_fil_v2.py` er navnet på kopien,
siden det er det andre posisjonelle argumentet.

### Frivillige tilvalg

Tilvalg, eller option på engelsk, er en type programargument som starter med bindestrek.
Fordi tilvalget har et navn som du oppgir, spiller det ingen rolle hvilken rekkefølge du bruker.

#### Korte og lange tilvalg

Ett og samme tilvalg har som oftest to varianter:
En kort énbokstavsvariant (short option) og en lang fullvariant (long option).
De starter med henholdsvis én og to bindestreker.
For eksempel `-a` i `ls -a`, eller den ekvivalente `ls --all`.

Når du til daglig sitter i terminalen er det praktisk å bruke korte tilvalg,
men hvis du skriver ned kommandoer i et skript eller i en guide,
bør du bruke lange tilvalg sånn at leseren lettere forstår hva de gjør.


#### Flagg

Noen tilvalg står alene og kalles _flagg_.
De signaliserer at noe skal aktiveres eller deaktiveres
simpelthen fordi de er der.
  
Hvis du trenger å bruke flere flagg og bruker énbokstavsvarianten,
kan du bruke én bindestrek og så liste opp alle flaggene etter hverandre.
For eksempel er `ls -larth` ekvivalent med `ls -l -a -r -t -h`.


#### Tilvalg med verdi

Andre tilvalg tar inn en verdi.
Den kan du angi som det neste programargumentet.
For lange tilvalg kan du alternativt bruke et likhetstegn.

Som et eksempel kan vi oversette `ls -larth`-kommandoen ovenfor til å bruke lange tilvalg.
Da bruker vi `--format`, som tar inn typen format, i dette tilfellet `long`.
Og vi bruker `--sort`, som tar inn hva vi skal sortere på, i dette tilfellet `time`.

```shell
kurs $> ls --format long --all --reverse --sort time --human-readable
```

Alternativt med likhetstegn i stedet for mellomrom mellom tilvalg og tilhørende verdi:

```shell
kurs $> ls --format=long --all --reverse --sort=time --human-readable
```

### Hjelp til selvhjelp

Det er god kotyme å gi brukeren en kort oppsummering over hvordan du skal bruke programmet hvis brukeren ikke skriver noe programargument,
i de tilfellene hvor det er påkrevd.
Sånne korte oppsummeringer pleier ikke å være lengre enn 2-3 linjer,
og tar med en mal på hvordan kjøringer av programmet kan se ut.

I tillegg er det et standard valg som alle programmer bør støtte:
`--help`, gjerne med kortvalget `-h`.
Hvis brukeren spesifiserer dette valget, så skal ikke programmet gjøre noe likevel.
Det skal i stedet printe en hjelpetekst til terminalen og så avslutte.
Hjelpeteksten skal forklare hva programmet gjør, hvilke argumenter du må oppgi og hvilke valg du kan bruke.

Tanken er at du skal få den hjelpen du trenger,
uten at du må lese deg opp på et dokument som ligger et eller annet sted
eller lese deg opp på hvordan skriptet er skrevet.


### Signalisering av feil

Alle program har en avslutningskode, _exit code_ på engelsk, som blir satt når programmet avslutter.
Denne blir brukt for å kommunisere hvordan det gikk med programmet.
For eksempel kan et skript som består av flere andre skript velge å avbryte kjøringa hvis et av programmene flagger at noe gikk galt.

Hvis alt gikk bra, så skal programmet avslutte med avslutningskode `0`.

Alle andre avslutningskoder indikerer at noe gikk galt.
Du vil typisk bruke `1` til å indikere at noe galt har skjedd.

Python-programmer trenger som regel ikke tenke på dette.
Hvis skriptet kjører ferdig uten at det krasjer, vil det avslutte med avslutningskode lik `0`.
Hvis skriptet derimot krasjer, avslutter det med avslutningskode lik `1`.
Det eneste måtte være hvis du avslutter skriptet tidlig med [`sys.exit`][sys.exit],
som tar inn avslutningskoden som et argument.

[sys.exit]: https://docs.python.org/3/library/sys.html#sys.exit


## Bruke `click` til å tolke programargumenter

Hvis du skal følge bestepraksisen beskrevet ovenfor, blir det mye arbeid.
Derfor finnes det flere verktøy som tolker `sys.argv` for deg,
sånn at du slipper å gjøre den jobben selv.
Et av de er inkludert i Python og heter [`argparse`][argparse],
men i dette kurset skal vi bruke et tredjepartsbibliotek kalt [`click`][click].

[argparse]: https://docs.python.org/3/howto/argparse.html#id1
[click]: https://click.palletsprojects.com/en/8.1.x/

Start med å installere click:

```shell-session
kurs $> poetry add click
Using version ^8.1.3 for click

Updating dependencies
Resolving dependencies... (0.2s)

Writing lock file

Package operations: 1 install, 0 updates, 0 removals

  • Installing click (8.1.3)
```

La oss starte med å re-implementere `print_fil.py` med `click`.
Skriptet skal fortsatt ta inn et posisjonelt argument med navnet på fila vi skal skrive til terminalen.

```python
# print_fil_click.py
import click

@click.command()
@click.argument('valgt_fil')
def print_fil(valgt_fil):
  """Skriv innholdet av VALGT_FIL til terminalen."""
  with open(valgt_fil) as fil:
    for linje in fil:
      print(linje, end='')

print_fil()
```

Her bruker vi noe som kalles for _dekoratører_.
De kjennetegnes av funksjonskall med en alfakrøll foran seg,
som er listet opp rett før en funksjonsdefinisjon.
I tilfellet her er `click.command()` og `click.argument('valgt_fil')`
dekoratører, som dekorerer `print_fil`-funksjonen.
Nøyaktig _hva_ dekoratører gjør sparer vi til en frivillig ekstra-del,
men vi nøyer oss med å si at de kan elte og kna på funksjonen du definerer sånn at den kan fungere på en annen måte enn den ellers ville gjort.

Som du ser, er `click` orientert rundt funksjoner som blir gjort om til kommandoer.
Du spesifiserer hvilke valg og argumenter som kommandoen skal ta i mot,
og tar dem inn som funksjonsargumenter.
Pass på at navnet på argumentet stemmer overens med navnet som er gitt i [`click.argument`][doc-click.argument].

Eksempel på kjøring:

```shell
kurs $> poetry run python print_fil_click.py 
Usage: print_fil_click.py [OPTIONS] VALGT_FIL
Try 'print_fil_click.py --help' for help.

Error: Missing argument 'VALGT_FIL'.
kurs $> poetry run python print_fil_click.py --help
Usage: print_fil_click.py [OPTIONS] VALGT_FIL

  Skriv innholdet av VALGT_FIL til terminalen.

Options:
  --help  Show this message and exit.
kurs $> poetry run python print_fil_click.py print_fil_click.py
import click

@click.command()
@click.argument('valgt_fil')
def print_fil(valgt_fil):
  """Skriv innholdet av VALGT_FIL til terminalen."""
  with open(valgt_fil) as fil:
    for linje in fil:
      print(linje, end='')

print_fil()
kurs $> # Eksempel på fil som ikke finnes
kurs $> poetry run python print_fil_click.py finnes_ikke.txt
Traceback (most recent call last):
  File "/home/n123456/kurs/print_fil_click.py", line 11, in <module>
    print_fil()
  File "/home/n123456/.cache/pypoetry/virtualenvs/kurs-hRZI2kkF-py3.10/lib/python3.10/site-packages/click/core.py", line 1130, in __call__
    return self.main(*args, **kwargs)
  File "/home/n123456/.cache/pypoetry/virtualenvs/kurs-hRZI2kkF-py3.10/lib/python3.10/site-packages/click/core.py", line 1055, in main
    rv = self.invoke(ctx)
  File "/home/n123456/.cache/pypoetry/virtualenvs/kurs-hRZI2kkF-py3.10/lib/python3.10/site-packages/click/core.py", line 1404, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/n123456/.cache/pypoetry/virtualenvs/kurs-hRZI2kkF-py3.10/lib/python3.10/site-packages/click/core.py", line 760, in invoke
    return __callback(*args, **kwargs)
  File "/home/n123456/kurs/print_fil_click.py", line 7, in print_fil
    with open(valgt_fil) as fil:
FileNotFoundError: [Errno 2] No such file or directory: 'finnes_ikke.txt'
```

Noen punkter å notere seg:
* Click sjekker at brukeren har spesifisert det posisjonelle argumentet
* Click skriver automatisk en melding til terminalen når argumentet mangler
* Click skriver en automatisk generert hjelpemelding til terminalen når brukeren spesifiserer `--help` som et valg, uten at den kjører koden inni `print_fil`-funksjonen
* Doc-strengen vi la til helt i starten av funksjonen blir tatt med i hjelpeteksten
* Stacktracen som skrives til terminalen når skriptet krasjer,
  har med seg en del ekstra lag med funksjonskall siden det er en del mekanismer i Click som kjører før selve `print_fil`-funksjonen vår kjører


## Valg med Click

I eksemplet ovenfor så vi at `click.argument` brukes til å registrere at vi skal ta inn et posisjonelt argument.
Tilsvarende kan vi bruke [`click.option`][doc-click.option] til å registrere et valg.

### Flagg

La oss utvide eksemplet fra i stad med et valg som lar deg skru på nummerering av linjene:

```python
# print_fil_click_v2.py
import click

@click.command()
@click.option('-n', '--number', is_flag=True, help='Skriv linjenummer foran hver linje.')
@click.argument('valgt_fil')
def print_fil(number, valgt_fil):
  """Skriv innholdet av VALGT_FIL til terminalen."""
  with open(valgt_fil) as fil:
    for linjenummer, linje in enumerate(fil, start=1):
      # Skriv linjenummer hvis aktivert
      if number:
        # Sørg for konsekvent venstremargin på koden
        # (for filer på opptil 999 linjer)
        print(f'{linjenummer: 3d}: ', end='')
      # Skriv linja
      print(linje, end='')

print_fil()
```

Med `click.option` spesifiserer vi at vi ønsker å legge til et valg.
Kortvalget er `'-n'`, mens langvalget er `'--number'`.
Takket være `is_flag=True` så vet Click at det er flagg,
og at det derfor ikke skal ta inn en verdi.
Da vil det også bli tolket som et boolsk valg,
som er `False` med mindre brukeren tar det med.
Teksten i `help='...'` blir tatt med i hjelpeteksten for dette valget.

For å få linjenummeret, bruker vi funksjonen [`enumerate`][docs-builtins.enumerate].
Den tar inn noe som du kan iterere over, for eksempel `['a', 'b', 'c']`,
og legger på et løpenummer, for eksempel `[(0, 'a'), (1, 'b'), (2, 'c')]`.
Siden elementene er tupler, kan vi pakke dem ut i `for` ved å skrive `for linjenummer, linje ...`.
For at ikke første linje skal bli kalt linje 0, ber vi `enumerate` om å starte på 1.

Når vi skriver `f'{linjenummer: 3d}: '` bruker vi formateringsspråket til å be om at linjenummeret formateres med ledende mellomrom, sånn at linjenummeret alltid tar opp tre tegn.
Siden vi forteller `print` at den ikke skal skrive noe linjeskift til terminalen etter teksten vår,
vil linja som skrives ut havne på samme linje som linjenummeret vårt.

Eksempel på kjøring:

```shell
kurs $> poetry run python print_fil_click_v2.py print_fil_click_v2.py --help
Usage: print_fil_click_v2.py [OPTIONS] VALGT_FIL

  Skriv innholdet av VALGT_FIL til terminalen.

Options:
  -n, --number  Skriv linjenummer foran hver linje.
  --help        Show this message and exit.
kurs $> poetry run python print_fil_click_v2.py print_fil_click_v2.py --number
  1: import click
  2: 
  3: @click.command()
  4: @click.option('-n', '--number', is_flag=True, help='Skriv linjenummer foran hver linje.')
  5: @click.argument('valgt_fil')
  6: def print_fil(number, valgt_fil):
  7:   """Skriv innholdet av VALGT_FIL til terminalen."""
  8:   with open(valgt_fil) as fil:
  9:     for linjenummer, linje in enumerate(fil, start=1):
 10:       # Skriv linjenummer hvis aktivert
 11:       if number:
 12:         # Sørg for konsekvent venstremargin på koden
 13:         # (for filer på opptil 999 linjer)
 14:         print(f'{linjenummer: 3d}: ', end='')
 15:       # Skriv linja
 16:       print(linje, end='')
 17: 
 18: print_fil()
```

### Valg som tar inn verdi

La oss gi brukeren mulighet til å filtrere bort linjer som er for korte.
For eksempel vil vi at `poetry run python print_fil_click_v3.py --min-length 40`
bare skriver ut linjene som er 40 tegn eller lengre.
Hvis brukeren ikke bruker `--min-length`, gjør vi ikke noen filtrering:

```python
# print_fil_click_v3.py
import click

@click.command()
@click.option('-n', '--number', is_flag=True, help='Skriv linjenummer foran hver linje.')
@click.option('--min-length', metavar='LENGDE', default=0, help='Hopp over linjer med færre tegn enn LENGDE.')
@click.argument('valgt_fil')
def print_fil(number, min_length, valgt_fil):
  """Skriv innholdet av VALGT_FIL til terminalen."""
  with open(valgt_fil) as fil:
    for linjenummer, linje in enumerate(fil, start=1):
      # Hopp over linjer med for få tegn
      antall_tegn_før_linjeskift = len(linje.rstrip())
      if antall_tegn_før_linjeskift < min_length:
        continue

      # Skriv linjenummer hvis aktivert
      if number:
        # Sørg for konsekvent venstremargin på koden
        # (for filer på opptil 999 linjer)
        print(f'{linjenummer: 3d}: ', end='')

      # Skriv linja
      print(linje, end='')

print_fil()
```

Eksempel på kjøring:

```shell
kurs $> poetry run python print_fil_click_v3.py --help
Usage: print_fil_click_v3.py [OPTIONS] VALGT_FIL

  Skriv innholdet av VALGT_FIL til terminalen.

Options:
  -n, --number         Skriv linjenummer foran hver linje.
  --min-length LENGDE  Hopp over linjer med færre tegn enn LENGDE.
  --help               Show this message and exit.
kurs $> poetry run python print_fil_click_v3.py print_fil_click_v3.py --min-length 55 --number
  4: @click.option('-n', '--number', is_flag=True, help='Skriv linjenummer foran hver linje.')
  5: @click.option('--min-length', metavar='LENGDE', default=0, help='Hopp over linjer med færre tegn enn LENGDE.')
```

Her har vi spesifisert valget `--min-length`.
Hvis brukeren ikke bruker valget, blir minstelengden satt til 0 på grunn av `default`-argumentet.
I tillegg skjønner Click at brukeren må oppgi et _tall_,
siden default-verdien vår er et tall.
Alternativt kunne vi spesifisert `type=int` som enda et argument til `click.option`.

Vi bruker `metavar='LENGDE'` til å bestemme hva placeholderen for verdien skal være i hjelpeteksten.
Hadde vi ikke spesifisert metavar hadde den vært `INTEGER` siden det er et heltall.


## Andre ting du kan gjøre med Click

Når du får et nytt verktøy i hendene frister det kanskje ikke å slå opp bruksanvisningen,
men når det gjelder programvarepakker så kan dokumentasjonen være vel verdt et besøk.
Ofte kan verktøyet ha løst problemer som du ikke trodde det løste,
eller ha muligheter du ikke har tenkt på.
Sjekk ut [den offisielle dokumentasjone til Click][click] for å oppdage mange flere ting du kan gjøre, som for eksempel:

* Sette et minimum og/eller et maksimum for et valgs verdi, for eksempel kan `--min-length` ovenfor begrenses sånn at negative tall ikke er tillatt
* Be Click om å sjekke at et argument eller et valgs verdi er en gyldig filsti som peker mot en eksisterende fil
* Be Click spørre brukeren om verdier på valg som brukeren ikke bruker (likt `input()`)
* Lage program som kan gjøre flere ting, avhengig av hvilken underkommando brukeren spesifiserer (på samme måte som `poetry` gjør ulike ting avhengig om du skriver `poetry add` eller `poetry run` og så videre)
* Åpne opp en editor som brukeren kan bruke til å redigere ei fil
* Vise en progressbar

✍️ **Oppgave:**
_Kan du skrive om den store oppgaven fra dag 1 sånn at du tar inn navnet på JSON-fila fra programargumentene i stedet for at den ligger i koden?_


## Videre lesning

* [Click-dokumentasjonen][click]
* [12 Factor CLI Apps](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46)
* [Command Line Interface Guidelines](https://clig.dev/)
* [argparse-dokumentasjonen][doc-argparse]

[wiki-hardcoding]: https://en.wikipedia.org/wiki/Hard_coding
[doc-input]: https://docs.python.org/3/library/functions.html#input
[doc-sys]: https://docs.python.org/3/library/sys.html
[doc-sys.argv]: https://docs.python.org/3/library/sys.html#sys.argv
[doc-sys.orig_argv]: https://docs.python.org/3/library/sys.html#sys.orig_argv
[doc-argparse]: https://click.palletsprojects.com/en/8.1.x/
[click]: https://click.palletsprojects.com/en/8.1.x/
[doc-click.option]: https://click.palletsprojects.com/en/8.1.x/options/
[doc-click.argument]: https://click.palletsprojects.com/en/8.1.x/arguments/
[docs-builtins.enumerate]: https://docs.python.org/3/library/functions.html#enumerate
