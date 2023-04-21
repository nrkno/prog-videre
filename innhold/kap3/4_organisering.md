Organisering med moduler og pakker (Heidi)
=========================================================================


**💡 Læringsmål:** _I dette avsnittet lærer du hvordan du kan organisere koden på en strukturert måte så det blir lettere å finne fram_

## Moduler

Etterhvert som programmet vokser og man skriver stadig mer kode kan det fort oppleves rotete og uoversiktlig om all kode er i samme fil. For å få det mer ryddig kan man derfor strukturere koden i flere filer, der funksjonalitet som hører sammen eller handler om det samme er i samme modul. 

En modul i Python er ikke noe annet enn en fil med python-kode, altså slike filer vi allerede kjenner til, som slutter på `.py`.

La oss si at vi vil lage et program som konverterer en tekststreng som brukeren angir til å være på [røverspråk]https://no.wikipedia.org/wiki/R%C3%B8verspr%C3%A5ket), for deretter å teksten ut på røverspråk i terminalen.

Hittil ville vi ha skrevet all kode i samme fil, men så skal vi lage en røverspråk-modul. Start med å lage en fil som heter `røverspråk.py`. I denne filen vil ha funksjonen `til_røverspråk` som tar inn en streng, og returnerer røverspråk strengen. Lim inn koden under i `røverspråk.py`.

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

I koden er det et par ting vi kan merke oss. Den første linja `import røverspråk` trenger vi for å få tilgang til funksjonen `til_røverspråk` som er i `røverspråk.py`. Da kan vil på den fjerde linja kalle funksjonen ved å skrive `røverspråk.til_røverspråk`. Dette er god måte å importere på, for vi ser også modulnavnet `røverspråk` så vi skjønner med en gang hvor funksjonen `til_røverspråk` kommer fra. 

Kjør programmet og se at det fungerer som du forventer!

### Andre måter å importere på

Det finnes også andre måter i importere moduler på i filen der man vil bruke modulen.
* `import røverspråk as rs` med `rs.til_røverspråk` der man kaller funksjonen. Dette er nyttig hvis navnet på modulen er litt langt, `rs` kortere å skrive enn `røverspråk`.
* Man kan unngå helt å ha modulnavn som prefiks ved å importere med `from røverspråk import til_røverspråk`. Da bruker man bare funksjonsnavnet `til_røverspråk` der funksjonen kalle. Det blir mindre å skrive, men kan være litt vanskeligere å vite hvor funksjonen kommer fra om man har mange imports.
* En siste variant er å importere med `from røverspråk import *`, da har man importert alle navnene fra `røverspråk` inn i program-modulen. Det som er skummelt med denne varianten er at man lett kan miste kontroll over hva som er importert, og man kan ved uhell overskrive navn som allerede er tatt i bruk. Det er derfor anbefalt å unngå denne måten å importere på.

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

Så nå har endringen vi gjorde i `røverspråk.py` ødelagt funksjonaliteten i programmet vårt. Det er fordi Python kjører koden i modulen `røverspråk.py` når den importeres! Det er derfor viktig å tenke på at man ikke har kode på rotnivå i filen som har sideffekter, som for eksempel `print` som skriver ut.



## Pakker

## Oppgaver

✍️ **Oppgave:**
_Skriv om programmet der du jobber med EPG-er til å bruke moduler og eventuelt pakker der du synes det passer slik at koden blir ryddigere_

## Videre lesning

[Moduler i Python tutorial](https://docs.python.org/3/tutorial/modules.html)
