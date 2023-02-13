Programargumenter (Thorben)
=================

* Det er et bibliotek som heter click
* Her kommer det inn dekoratører, men det gjør vi veldig kort.
* Her er oppgaven på slutten av avsnittet at man skal skrive om programmet fra dag 1 til å bruke programargumenter.

Programargumenter uten click (to be flytta)
===========================================

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


## Hvordan gi flere argumenter til et program?

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


## Lese argumentene til Python-skriptet

For å nyttiggjøre deg av de ekstra argumentene brukeren skriver,
må du importere [`sys`-modulen][doc-sys].
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


## Eksempel: Angi fil som skal leses fra som argument

La oss ta i bruk `sys.argv` med et praktisk eksempel
hvor vi leser linjer fra ei fil og skriver dem til terminalen:

```python
# print_fil.py
import sys

if len(sys.argv) < 2:
    print("Du må oppgi hvilken fil du vil lese fra")
    sys.exit(2)

valgt_fil = sys.argv[1]
with open(valgt_fil) as fil:
    for linje in fil:
        print(linje, end='')
```

Eksempel på kjøring:

```shell-session
kurs $> python print_fil.py
Du må oppgi hvilken fil du vil lese fra
kurs $> python print_fil.py print_fil.py
import sys

if len(sys.argv) < 2:
    print("Du må oppgi hvilken fil du vil lese fra")
    sys.exit(2)

valgt_fil = sys.argv[1]
with open(valgt_fil) as fil:
    for linje in fil:
        print(linje, end='')
```

PS: Du kan allerede gjøre dette i terminalen ved å bruke det innebygde programmet `cat`,
for eksempel ved å kjøre `cat print_fil.py`.

✍️ **Oppgave:**
_Kan du skrive om `skriv_til_fil.py` fra forrige kapittel,
sånn at du kan bestemme hvilken fil den skal skrive til med et programargument?_


## Eksempel: Bruke argument 0 i tilbakemeldinger

Det kan virke litt tåpelig at navnet på skriptet skal ta opp den første plassen i `sys.argv`,
men det kan være nyttig å bruke hvis du vil ta med navnet på skriptet i en tilbakemelding.
For eksempel:

```python
# feilmelding_med_skriptnavn.py
import sys

if len(sys.argv) != 2:
    pythonnavn = sys.orig_argv[0]
    skriptnavn = sys.argv[0]

    print("Feil: Du må gi nøyaktig ett argument til skriptet.")
    print("Eksempel:")
    print(f"{pythonnavn} {skriptnavn} navn_på_fil.txt")
    sys.exit(2)

valgt_fil = sys.argv[1]
print(f"Vil jobbe på fila {valgt_fil}")
```

Her bruker vi [`sys.orig_argv`][doc-sys.orig_argv] til å hente navnet på Python-programmet.
På samme måte som skriptnavnet har plass nummer 0 i argumentlista til skriptet,
har Python-programmet programnavnet på plass nummer 0 i sin argumentliste.
Dermed vil det første argumentet ha plass nummer 1, det andre argumentet plass nummer 2, og så videre.
Forskjellen på `sys.argv` og `sys.orig_argv` er hvorvidt du ser på argumentene fra skriptet sitt ståsted,
eller fra Python-programmet sitt ståsted.

Eksempel på kjøring:

```shell-session
kurs $> python3.10 feilmelding_med_skriptnavn.py
Feil: Du må gi nøyaktig ett argument til skriptet.
Eksempel:
python3.10 feilmelding_med_skriptnavn.py navn_på_fil.txt
kurs $> python3.10 feilmelding_med_skriptnavn.py sti/til/fil.txt
Vil jobbe på fila sti/til/fil.txt
kurs $> # Bytt navn på fila
kurs $> mv feilmelding_med_skriptnavn.py skriptnavn_i_feilmelding.py
kurs $> python3.10 skriptnavn_i_feilmelding.py
Feil: Du må gi nøyaktig ett argument til skriptet.
Eksempel:
python3.10 skriptnavn_i_feilmelding.py navn_på_fil.txt
```

Uansett hva brukeren kaller programmet hos seg,
vil eksemplet i tilbakemeldingen bruke riktig navn på Python og på skriptet.

## Eksempel: Gi brukeren hjelp

Hvis du lager et Python-skript som er ment å brukes av noen andre,
er det veldig hyggelig hvis du kan bygge inn en hjelp til selvhjelp i skriptet.
Husk på at «noen andre» i dette tilfellet her også kan være deg om seks måneder,
når du returnerer noe forvirret og ikke helt husker hva du har tenkt.

Det er to måter brukeren typisk vil be applikasjonen om hjelp:

* Kjøre skriptet uten å spesifisere noe argument
    * Dette vil typisk gi en veldig kort oppsummering på én eller to linjer
* Bruke flagget `-h` eller langformen `--help` som argument (uansett hvor)
    * Dette vil typisk gi en mer utfyllende introduksjon til programmet

La oss utvide `print_fil.py` sånn at den gir brukeren litt mer hjelp enn den allerede gjør.

```python
# print_fil_hjelp.py
import sys

pythonnavn = sys.orig_argv[0]
skriptnavn = sys.argv[0]

if len(sys.argv) == 1:
    print(f"Bruk: {pythonnavn} {skriptnavn} FILSTI")
    sys.exit(2)
elif "-h" in sys.argv or "--help" in sys.argv:
    print(f"""\
Bruk: {pythonnavn} {skriptnavn} FILSTI
Skriv ut innholdet av FILSTI til terminalen.

Flagg:
 -h, --help  Skriv denne hjelpeteksten til
             terminalen og avslutt\
""")
    sys.exit(0)  # kode 0 betyr ingen feil
# Hvis vi hadde krevd mer enn ett argument,
# skulle vi sjekket om det ble gitt for få
# argumenter her og eventuelt feilet

valgt_fil = sys.argv[1]
with open(valgt_fil) as fil:
    for linje in fil:
        print(linje, end='')
```

✍️ **Oppgave:**
_Prøv å kjøre `print_fil_hjelp.py`.
Klarer du å kjøre skriptet sånn at du får hjelpeteksten?_

✍️ **Oppgave:**
_Prøv å legge til støtte for hjelpetekst på et av eksemplene på skriving til fil._


## Eksempel: Bruk prompt når argument mangler

Nedsiden med programargumenter er at brukeren er nødt til å lese seg opp
før hen kan kjøre programmet ditt.
Der var `input()` bedre: Programmet stiller spørsmål, og brukeren svarer.

Det er fullt mulig å kombinere programargumenter med prompt,
og få det beste fra begge verdener.
I denne varianten av `print_fil.py` prøver vi først å lese filnavnet fra programargumentet,
og faller tilbake på å spørre brukeren direkte hvis det ikke går.

```python
# print_fil_prompt.py
import sys

if len(sys.argv) > 1:
    # Brukeren har skrevet filnavnet som argument
    valgt_fil = sys.argv[1]
else:
    valgt_fil = input("Hvilken fil vil du skrive til konsollen? ")

with open(valgt_fil) as fil:
    for linje in fil:
        print(linje, end='')
```

Brukere som vil automatisere skriptet ditt kan sende inn filnavnet som et programargument,
som en slags hurtigtast.
Brukere som ikke kjenner skriptet ditt kan bare kjøre det,
og trenger bare forholde seg til spørsmålene hen blir stilt.

✍️ **Oppgave:**
_Hva skjer hvis du skriver inn navnet på ei fil som ikke finnes?
Eller bare trykker `[ENTER]` uten å skrive noe?_


## Kort om mer avanserte argumenter

Det å lese programargumentene direkte fra [`sys.argv`][doc-sys.argv] er en god start,
og vil gi deg mange av fordelene som programargumenter kan gi.
Men det øyeblikket du har flagg som skal kunne skrus av og på,
eller du trenger å kunne fininnstille flere variabler,
blir det veldig fort veldig komplisert å lage funksjonaliteten selv.

Dette er et såpass vanlig problem at det finnes ferdige bibliotek som har gjort mesteparten av jobben allerede.
[Biblioteket `argparse`][doc-argparse] følger med Python, og har implementert det aller meste du trenger.
Problemet med `argparse` er at det er komplisert og omstendelig.

I del 2 av kurset skal vi begynne å ta i bruk installerbare pakker.
Da kan vi ta for oss [tredjepartsbiblioteket `click`][click],
som gjør det lekende lett å ta i bruk programargumenter og -flagg.


## Videre lesning

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
