Tips og triks om terminalen
===========================

Terminalen, på engelsk ofte kalt _command line_, er en tekstbasert måte å starte programmer på.
Vi bruker den ofte når vi lager dataprogram.

I terminalen skriver du kommandoer etter hverandre, som ber datamaskinen om å gjøre noe.
Hvis du ikke får noen feilmelding, har det som regel gått bra – terminalprogram pleier ikke å si fra at ting er OK.

Denne sida tar med diverse temaer som kan være nyttige hvis du er ny bruker av terminal.


## Alle terminaler er ikke like

Det finnes mange forskjellige typer _shell_.
Et skall er programmet som du snakker med når du jobber i terminalen.

Hvilket skall du bruker, avgjør hvilken avansert funksjonalitet du har tilgang til.
Den grunnleggende funksjonaliteten for å starte et program, er mer eller mindre helt lik for alle skall.

Skjellet `bash` er velkjent og mye brukt, spesielt på Linux og Mac før macOS Catalina.

Fra og med macOS Catalina er `zsh` det innebygde skallet.

På Windows er `cmd` og `Powershell` vanlige, der sistnevnte er den mest avanserte.
Men de fungerer ganske annerledes fra andre skall.
Du bør vurdere å installere `bash` eller oppsøke en annen innføring i `Powershell`.


## Vanlig funksjonalitet i skall

### Kjør et program

Den første delen av enhver kommando bestemmer hvilket program du skal kjøre.

Når vi kjører Python, skriver vi alltid `python` først i kommandoen.
Da er det Python-programmet som kommer til å kjøre.


### Programargumenter

Etter navnet på programmet kan du legge til argumenter som vil bli gitt til programmet.
Vi kaller dem for programargument (arguments).
Når vi kjører Python-kode vi har skrevet, skriver vi navnet på `.py`-fila etter `python`, men med et mellomrom i mellom.
Python-programmet vet at filnavn du gir til det skal tolkes som Python-skript som skal kjøres.

For eksempel så har `cp hei.txt hallo.txt` to programargument som blir gitt til `cp`:
1. `hei.txt`
2. `hallo.txt`

Hvis en filsti skal inneholde mellomrom, må du bruke hermetegn rundt argumentet sånn at skallet oppfatter det som ett argument og ikke flere.
For eksempel:

```shell
cp "hilsen hei.txt" "hilsen hallo.txt"
```

har to programargument som blir gitt til `cp`:
1. `hilsen hei.txt`
2. `hilsen hallo.txt`

Glemmer du hermetegn, får du:

```shell
cp hilsen hei.txt hilsen hallo.txt
```

som har fire programargument som blir gitt til `cp`:
1. `hilsen`
2. `hei.txt`
3. `hilsen`
4. `hallo.txt`

Det blir feil.


### Avbryte kjørende program

Du kan avslutte et program med `[CTRL]` + `C`.


### Autofullfør

Når du skriver kommandoer i terminalen,
kan du bruke `[TAB]`-tasten til å fullføre argumentet du skriver på.
Hvis det du har skrevet er nok til å vite hvilken fil du tenker på,
kan du fylle ut resten med ett trykk.
Er det flere filer, må du gjerne trykke flere ganger for å få forslag eller gå gjennom forslagene.

Dette er veldig nyttig siden du ofte vil skrive filnavn i kommandoer.
Du kan bruke autofullfør både når du skal skrive hvilket skript Python-programmet skal kjøre,
og når du skal fortelle skriptet hvilken fil du vil lese fra eller skrive til.


### Historikk

Bruk `[PILTAST OPP]` og `[PILTAST NED]` til å bla gjennom historikken.
Vil du kjøre den forrige kommandoen din én gang til,
kan du trykke `[PILTAST OPP]` én gang, etterfulgt av `[ENTER]`.
Du kan også endre på kommandoen etter at du har bladd deg opp til den,
for eksempel hvis du vil kjøre det samme med en liten endring.


## Navigere filsystemet

### Working Directory

Du står til enhver tid i ei mappe, kalt _working directory_.
Du kan sammenlikne det et vindu av en filutforsker, som til envher tid har ei mappe åpen.

Med kommandoen `pwd` kan du Print Working Directory. Da ser du hvor du står.

Bruk kommandoen `cd MAPPE` for å bytte (Change Directory) til MAPPE.


### Absolutte filstier

Uansett hvor du står, kan du alltid referere til en hvilken som helst fil som ligger hvor som helst.
Da bruker du _absolutt filsti_.
Absolutte filstier _starter_ med en skråstrek, bortsett fra Windows hvor de også kan starte med stasjonen og kolon.

Eksempler på absolutte filstier på Linux/Unix:
* `/home/n123456/Documents`
* `/etc/hosts`
* `/etc/hostname`

Windows:
* `C:\Users\n123456\Desktop`
* `D:\Backup\2019\03\14.zip`

Absolutte filstier avhenger ikke av hvilken mappe du står i, de er alltid det samme.


### Hjemmemappa

De aller fleste skall opererer med ei spesiell mappe kalt hjemmemappa, eller _home_ på engelsk.
På Linux og Unix pleier den å være `/home/n123456`, på Windows `C:\Users\n123456`.

Skal du referere til hjemmemappa di, kan du som regel bruke tilde-tegnet, `~`.
På norsk tastatur holder du inne `[Alt Gr]`, trykker tasten mellom `Å` og `[ENTER]`,
slipper `[Alt Gr]` og trykker på `[MELLOMROM]`.

Eksempel:
* `~/Desktop`
* `~/Documents`

Merk at tilde blir utvidet av _skallet_.
De blir dermed gjort om til absolutte filstier før noe annet program begynner å lese dem.

Du kan alltids returnere til hjemmemappa ved å kjøre kommandoen `cd` uten argument.


### Relative filstier

Relative filstier tar utgangspunkt i mappa du står i.
De starter med navnet på ei fil eller ei mappe i den mappa.

Det ligger to spesielle filer i hver mappe:
* `.` er en referanse til den mappa.
* `..` er en referanse til foreldermappa.

Si at du står i `/home/n123456/kurs/ekstra`.
Tabellen nedenfor viser hvordan du kan bygge en relativ filsti for ulike destinasjoner:

| Absolutt filsti                         | Relativ filsti fra `/home/n123456/kurs/ekstra` |
|-----------------------------------------|------------------------------------------------|
| `/home/n123456/kurs/ekstra/terminal.md` | `terminal.md`                                  |
| `/home/n123456/kurs/ekstra`             | `.`                                            |
| `/home/n123456/kurs/ekstra`             | `./././././.`                                  |
| `/home/n123456/kurs`                    | `..`                                           |
| `/home/n123456/kurs`                    | `../../kurs/../kurs/../kurs/../kurs`           |
| `/home/n123456/kurs/kap1`               | `../kap1`                                      |
| `/home/n123456/kurs/kap1/README.md`     | `../kap1/README.md`                            |
| `/home/n123456`                         | `../..`                                        |
| `/home`                                 | `../../..`                                     |


### Jokertegn

Skallet lar deg bruke jokertegn for å velge flere filer ut fra likheter i filstien.
Stjerna, `*`, kan brukes for å matche hva som helst i en filsti.
Alle treffene vil bli lagt etter hverandre, med mellomrom, før de blir sendt til programmet som skal kjøres.

For eksempel så kan du konkattenere alle filene i mappa du står i som slutter på `.py`:

```shell
kurs $> cat *.py
```

Hvis du har `1.py`, `2.py` og `3.py` liggende i mappa du er i, vil `cat` få tre programargument:

1. `1.py`
2. `2.py`
3. `3.py`


## Vanlige kommandoer

Noen av disse kommandoene er utilgjengelige i PowerShell, som fungerer ganske annerledes fra andre skall.

* `cd MAPPENAVN`: Change Directory. Lar deg endre hvilken mappe du står i.
  Kan sammenliknes med å dobbelttrykke på ei mappe i filutforskeren.
* `cd`: Bytt til hjemmemappa.
* `cd -`: Bytt til den forrige mappa du sto i.
  Historikken går bare én mappe bakover i tid.
* `pwd`: Print Working Directory. Skriv til terminalen hvilken mappe du står i.
* `ls`: LiSt. Vis innholdet i mappa du står i.
* `ls MAPPE`: Vis innholdet av MAPPE.
* `cat FIL`: conCATenate. Vis innholdet av FIL. Du kan liste opp flere filer for å konkattenere dem sammen.
* `mv FRA TIL`: MoVe. Bytt navn på fila eller mappa FRA, sånn at den heter TIL.
  Du kan også flytte den til et annet sted. 
* `cp KILDE MÅL`: CoPy. Lag en kopi av KILDE som heter MÅL.
* `rm FIL`: ReMove. Slett FIL permanent.
* `man KOMMANDO`: MANual. Vis hjelpeinformasjon for KOMMANDO.
* `grep SØK FIL`: Vis alle tilfeller av SØK i FIL.
* `grep -r SØK MAPPE`: Vis alle tilfeller av SØK i filer i MAPPE.


## Konvensjoner for program du kjører i terminalen

Her er noen konvensjoner som terminalprogram pleier å følge.
Men du har selvfølgelig ingen garantier for at _alle_ program følger disse.

Når du skriver egne program, bør du etterstrebe å overholde disse konvensjonene.
Det gjør det enklere for andre å ta i bruk programmet ditt.
[Kapittel 3.2 om programargumenter](/kap3/2_programargumenter.md) går i detalj på hvordan du får til det.


### Korte tilvalg/flagg

Kommandoers virkemåte kan justeres med tilvalg (options).
De starter alltid med bindestrek.
Korte tilvalg (short options) er alltid ett tegn lange.

For eksempel kan du få `ls` til å vise flere detaljer med `-l` hvis du bruker `bash` som skall:

```shell
kurs $> ls -l
total 1128
-rw-r--r--  1 n123456 n123456    1008 Mar 27 15:59  README.md
-rw-r--r--  1 n123456 n123456     622 Feb 13 13:08  book.toml
...
-rw-r--r--  1 n123456 n123456 1094001 Feb 13 13:08  mermaid.min.js
...
```

Du kan vise filstørrelser med suffiks for kilo, mega, og så videre med `-h`:

```shell
kurs $> ls -l -h
...
-rw-r--r--  1 n123456 n123456 1.1M Feb 13 13:08  mermaid.min.js
...
```

Når du gir flere korte tilvalg, kan du kombinere dem ved å bruke én bindestrek etterfulgt av alle tilvalgene uten bindestrek, for eksempel:

```shell
kurs $> ls -lh
...
-rw-r--r--  1 n123456 n123456 1.1M Feb 13 13:08  mermaid.min.js
...
```

Tilvalg skal som regel plasseres rett etter navnet på programmet du kjører, men rekkefølgen på dem spiller ingen rolle.

Tilvalgene som er vist i dette delkapitlet tar ikke inn noen tilhørende verdi.
De kalles også for _flagg_.


#### Korte tilvalg med tilhørende verdi

Noen tilvalg tar inn en verdi.
Den kan du angi som det neste programargumentet.

`grep`, programmet som lar deg søke etter en tekst i ei fil, printer vanligvis bare de linjene som har søkestrengen i seg.
Du kan få den til å skrive linjene som kommer før og etter med tilvalget `-C <antall linjer>`. For eksempel:

```shell
kurs $> grep -C 2 Python README.md
...
```

Også disse tilvalgene kan kombineres med bare én bindestrek, så lenge tilvalget som skal ta inn en verdi er den siste i gruppa:

```shell
kurs $> grep -iC 2 Python README.md
...
```

`-i` er her et flagg som sier at søket skal ignorere små og store bokstaver.


### Lange tilvalg/flagg

Lange tilvalg starter alltid med to bindestreker, etterfulgt av hele ord eller fraser.

Ett og samme tilvalg har ofte en kort og en lang variant.
For eksempel kan du bruke enten `-a` eller `--all` for å vise skjulte filer med `ls`.

Når du til daglig sitter i terminalen er det praktisk å bruke korte tilvalg,
men hvis du skriver ned kommandoer i et skript eller i en guide,
bør du bruke lange tilvalg sånn at leseren lettere forstår hva de gjør.


#### Lange tilvalg med tilhørende verdi

Den tilhørende verdien til et langt tilvalg kan gis som et nytt programargument, likt som for korte tilvalg.
Men du kan også gi verdien ved å bruke et likhetstegn.

For eksempel:

```shell
kurs $> ls --format=long --all --reverse --sort time --human-readable
```

Her bruker `--format` likhetstegn og `--sort` mellomrom, men det kunne like gjerne vært omvendt,
eller begge kunne brukt den samme måten.


### Få hjelpeinformasjon

Legg til flagget `--help` på en kommando for å få en hjelpetekst som forklarer hva programmet gjør, og hvilke tilvalg det har.

Noen kommandoer støtter kun det korte tilvalget `-h`, mens andre kommandoer bruker `-h` for noe annet enn hjelp.


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
Det eneste måtte være hvis du avslutter skriptet tidlig med [`sys.exit`][doc-sys.exit],
som tar inn avslutningskoden som et argument.


## Temaer som ikke er dekket av denne gjennomgangen

* _Piping_ av output fra et program til et annet
* Omdirigering, _redirecting_, av output eller input til eller fra ei fil
* Input- og output-strømmene til alle program: `stdout`, `stderr` og `stdin`
* Powershell
* Programmering i skall (if, while, for, ...)
* Variabler
