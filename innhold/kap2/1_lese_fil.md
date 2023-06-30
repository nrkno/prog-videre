Vi leser data fra en fil (Heidi)
========================

**💡 Læringsmål:** _I dette avsnittet lærer du hvordan du leser data fra en fil._


Vi skal starte med å se på hvordan vi kan lese fra fil, som på mange måter er nyttig. Lag deg en `.py`-fil som du vil skrive programmet ditt i, og kopier fila [serier.txt](/prog-videre/kap2/filer/serier.txt) til samme mappe som Python-filen.

Vi skal arbeide med fila `serier.txt` som på hver linje inneholder `serieId` og `tittel` for en tv-serie, separert med `,`. Vi skal lese fila, splitte innholdet og skrive ut alle titlene i fila.

For å lese en fil må vi først åpne fila, deretter kan vi lese ut innholdet. Funksjonen `open` brukes for å åpne fila, du kan lese mer om denne funksjonen i [Python-dokumentasjonen](https://docs.python.org/3/library/functions.html?highlight=open#open).

```python
fil = open("serier.txt", "r")
```
Første argumentet til `open` er navnet på fila, det andre argumentet angir hva slags modus fila skal åpnes i, `r` står for `read`. Dette er også default-verdien, så `r` kan utelates om man vil.

Når vi har åpnet fila kan vi lese ut alt som tekst med funksjonen `read`. Legg til linjene under og kjør programmet.

```python
tekst = fil.read()
print(tekst)
``` 

Ser du noe rart i det som skrives ut? For eksempel at tittelen til "Fra bølle til bestevenn" ser ut som `Fra bÃ¸lle til bestevenn`. Det er fordi fila leses med feil tegnsett. Det kan vi løse ved å sette tegnsettet vi ønsker eksplitt som argument til `open`, med parameteren `encoding`. Endre linja med `open` til følgende:
```
fil = open("serier.txt", "r", encoding="utf-8")
``` 
Her sier vi eksplisitt at fila skal enkodes med `utf-8`.

Når man har åpnet en fil er det fint å lukke den pent etter seg når man er ferdig med den. Det er to måter å gjøre det på, den ene måten er å ha en linje etter at man er ferdig med filen, som lukker den, `fil.close()`. Det vi i stedet vil gjøre er å bruke en `with`-blokk. Da vet Python at den skal lukke fila når man går ut av blokken. og vi slipper selv å huske på det, og å finne ut hvor i koden det er lurt å lukke fila. Men `with` kan det se slik ut:
```python
with open("serier.txt", "r", encoding="utf-8") as fil:
    tekst = fil.read()
    print(tekst)
```
Bytt ut innholdet i programmet ditt med linjene over og se at programmet kjører som før. 

Vi leser nå hele filen til en stor streng, men for å oppnå målet vårt med å skrive ut en liste med bare titlene må vi kunne lese hver linje for seg. Det er flere måter å få til det på. Fil har en metode `readLines()`, men det som er upraktisk med den er at den beholder linjeskift-tegnet `\n` i slutten av hver linje. I stedet bruker vi string sin metode `splitlines()`. Vi kan derfor bytte ut innholdet i with-blokka med følgende linjer:
```python
    linjer = fil.read().splitlines()
    for linje in linjer:
        print(linje)
```
Men fortsatt er vi ikke helt i mål, nå skriver vi ut hele linja, ikke bare tittelen. For å få tak i tittelen kan vi bruke  `split`-metoden til string, som deler en streng for hver gang den finner den angitt skille-strengen.
 
✍️ **Oppgave:** _Kan du fullføre programmet slik at det bare skriver ut tittelen?_
```python
    for linje in linjer:
        deler = linje.split(",")
        # print(???)
```

✍️ **Oppgave:** _Finn eller lag en fil med tekstlig innhold, og eksperimenter med å lese fila og skrive ut innholdet i terminalen_

Om du trenger litt inspirasjon kan du se om du liker noen av csv-filene på [denne siden](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html).

