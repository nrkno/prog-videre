Organisering med moduler og pakker (Heidi)
=========================================================================

**💡 Læringsmål:** _I dette avsnittet lærer du hvordan du kan organisere koden på en strukturert måte så det blir lettere å finne fram_

## Moduler

Etterhvert som programmet vokser, og man skriver stadig mer kode, kan det fort oppleves rotete og uoversiktlig om all kode er i samme fil. For å få programmet mer ryddig kan man derfor strukturere koden i flere filer, der funksjonalitet som hører sammen eller handler om det samme er i samme modul. 

En modul i Python er ikke noe annet enn en fil med python-kode, altså slike filer vi allerede kjenner til, som slutter på `.py`.

La oss si at vi vil lage et program som tar som input en tekststreng som brukeren oppgir, og skriver denne teksten, gjort om til å være på [røverspråk](https://no.wikipedia.org/wiki/R%C3%B8verspr%C3%A5ket), tilbake i terminalen. 

Hittil har vi skrevet all kode i samme fil, men nå skal vi lage en røverspråk-modul. 

Start med å lage en fil som heter `røverspråk.py`. Denne filen vil ha funksjonen `til_røverspråk`, som tar inn en tekststreng, og returnerer denne teksten omgjort til røverspråk. Lim inn koden under i `røverspråk.py`.

```python
konsonanter = "bcdfghjklmnpqrstvwxz"

def til_røverspråk(tekst):
    str = ""
    for bokstav in tekst:
        if bokstav in konsonanter:
                str += f'{bokstav}o{bokstav}'
        else:
             str += bokstav
    return str
```

Nå vil vi lage selve programfilen som spør brukeren om en tekst, konverterer denne til røverspråk, og skriver den ut i terminalen. Lag en fil som for eksempel heter `program.py`, og  
lim inn koden under.

```python
import røverspråk

tekst = input("Hva vil du si på røverspråk?> ")
print(røverspråk.til_røverspråk(tekst))
```

I koden er det et par ting vi kan merke oss. Den første linja, `import røverspråk`, trenger vi for å få tilgang til funksjonen `til_røverspråk` som er i modulen `røverspråk.py`. Da kan vil på den fjerde linja kalle funksjonen ved å skrive `røverspråk.til_røverspråk`. Dette er god måte å importere modulen på, for når vi ser modulnavnet `røverspråk` skjønner med en gang hvor funksjonen `til_røverspråk` kommer fra. 

Kjør programmet og se at det fungerer som du forventer!

### Andre måter å importere på

Det finnes også andre måter i importere moduler på i filen der man vil bruke modulen.
* `import røverspråk as rs` med `rs.til_røverspråk` der man kaller funksjonen. Dette er nyttig hvis navnet på modulen er litt langt, `rs` er kortere å skrive enn `røverspråk`.
* Man kan unngå helt å ha modulnavn som prefiks ved å importere med `from røverspråk import til_røverspråk`. Da bruker man bare funksjonsnavnet `til_røverspråk` der funksjonen kalles. Det blir mindre å skrive, men det kan være vanskeligere å vite hvor funksjonen kommer fra om man har mange importeringer.
* En siste variant er å importere med `from røverspråk import *`. Da har man importert alle navnene fra `røverspråk` inn i program-modulen. Det som er skummelt med denne varianten er at man lett kan miste kontroll over hva som er importert, og man kan ved uhell overskrive navn som allerede er tatt i bruk. Det er derfor anbefalt å unngå denne måten å importere på.

### Kjøre modul som et program

Noen ganger er det praktisk å også kunne kjøre en modul som et program, samtidig som den fungerer som en modul for at annet program. Vi skal gjøre et lite eksperiment. Lim inn linjene under nederst i fila `røverspråk.py`.

```python
røverspråk = til_røverspråk("nrk er verdens beste arbeidsplass")
print(røverspråk)
```

Kjør nå fila `røverspråk.py` som et skript, på samme måte som du kjørte `program.py` i stad. Da blir du antakelig ikke så overrasket over at terminalen skriver ut:

```
nonrorkok eror voverordodenonsos bobesostote arorbobeidodsospoplolasossos
```

Men gå tilbake til `program.py` og kjør programmet på nytt. Hva skjer nå?

Der vil det nå skrives ut følgende til terminalen:

```
nonrorkok eror voverordodenonsos bobesostote arorbobeidodsospoplolasossos
Hva vil du si på røverspråk?> 
```

Så nå har endringen vi gjorde i `røverspråk.py` ødelagt funksjonaliteten i programmet vårt. Det er fordi Python kjører koden i modulen `røverspråk.py` når den importeres! Det er derfor viktig å tenke på at man ikke har kode på rotnivå i filen som gjør ting, det som kaller sideeffekt, nettopp som funksjonen `print` som skriver ut.

Men det er heldigvis mulig å få til begge deler, både å unngå å ødelegge for programmet som bruker modulen, og samtidig kunne kjøre modulen som et program som gjør noe. Måten man løser dette på å bruke det at moduler har navn. 

I python finnes det en global variabel `__name__` som inneholder navnet på modulen. Modulen `røverspråk.py` vil ha navnet `røverspråk`, men når `røverspråk.py` kjøres som program vil den få navnet `__main__`. Derfor kan vi løse problemet vårt ved å legge til en if-test i `røverspråk.py`. Vi vil bare skrive ut `nrk er verdens beste arbeidsplass` når navnet er `__main__`. Gjør derfor om `røverspråk` til å inneholde en if-test:

```python
if __name__ == "__main__":
    røverspråk = til_røverspråk("nrk er verdens beste arbeidsplass")
    print(røverspråk)
```

Test å kjøre både `program.py` og `røverspråk.py`, og se at begge programmene nå fungerer som de skal.

## Pakker

Når man har flere moduler som inneholder lignende funksjonalitet eller er relatert til hverandre kan det noen ganger være fint å samle de i en pakke, slik at de importeres med `<pakkenavn>.<modulnavn>`. For eksempel om vi lager en ny modul med språket [Leet](https://no.wikipedia.org/wiki/Leet), kunne det være fint å samle røverspråk og leet i en pakke, la oss kalle den språk.

En pakke i Python er en filmappe som inneholder en fil som heter `__init__.py`. Det er den litt mystiske Python-filen som forteller Python at denne mappen er en modul. Så i mappen der du har filene dine kan du nå lage mappen `språk`, med filen `__init__.py`, og så flytter du `røverspråk.py` inn hit. Da har filene dine følgende struktur:

```txt
språk/
    __init__.py
    røverspråk.py
program.py
<eventuelt andre filer>
```

Om man nå skal importere `røverspråk`-modulen i `program.py` må man prefikse med `språk`, så det blir `språk.røverspråk`.

✍️ **Oppgave:**
_Fiks programmet `program.py`slik at det fungerer nå som røverspråk er i en pakke_

Nå vil vi gjøre om tekst til leet også. Lag en fil som heter `leet.py` i mappa `språk`, og kopier inn følgende kode:

```python
erstatninger = {
    'o': '0',
    'i': '1',
    'z': '2',
    'e': '3',
    'a': '4',
    's': '5',
    'g': '6',
    't': '7',
    'B': '8',
    'p': '9'
}

def til_leet(tekst): 
    str = ""
    for bokstav in tekst:
        str += erstatninger.get(bokstav, bokstav)
    return str
```

✍️ **Oppgave:**
_Oppdater `program.py` så den også bruker funksjonen `til_leet`. Du velger selv hvordan du ta i bruk funksjonen, om brukeren må velge om teksten skal oversettes til røverspråk eller leet, eller om du bare skriver ut begge oversettelsene._

## EPG-programmet

✍️ **Oppgave:**
_Skriv om programmet der du jobber med EPG-er slik at det bruker moduler og eventuelt pakker der du synes det passer for at koden skal bli ryddigere_

## Ekstraoppgaver

Her er et par ekstraoppgaver hvis du har litt ekstra tid og vil leke mer med språk.

✍️ **Oppgave:**
_Oversettelsen til røverspråk har den svakheten at den bare støtter små bokstaver. Skriv om `til_røverspråk` slik at den også håndterer store bokstaver, og erstatter for eksempel `B`med `BOB`_

✍️ **Oppgave:**
_Les mer på om [Leet på den engelske wikipedia-siden](https://en.wikipedia.org/wiki/Leet), og legg til noen nye erstatninger av bokstaver, for eksempel `K = |<`, `D = |)`._

## Les mer

[Moduler i Python - tutorial](https://docs.python.org/3/tutorial/modules.html)
