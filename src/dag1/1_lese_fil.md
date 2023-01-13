Vi leser data fra en fil (Heidi)
========================

Vi skal starte med å se på hvordan vi kan lese fra fil, det er jo nyttig til mange slags ting. Lag deg en `.py`-fil som du vil skrive programmet ditt i. Vi skal lese fila `serier.txt` som på hver linje inneholder `serieId` og `tittel` for en tv-serie, separert med `,`. Vi skal lese fila, splitte innholdet og printe ut alle titlene i fila.

For å lese en fil må vi først åpne fila, deretter leser vi innholdet. For å åpne fila brukes funksjonen `open`, du kan lese mer om denne funksjonen i [Python-dokumentasjonen](https://docs.python.org/3/library/functions.html?highlight=open#open).

```python
fil = open("serier.txt", "r")
```
Første argumentet til `open` er navnet på fila, det andre argumentet angir hva slags modus fila skal åpnes i, `r` står for `read`. Dette er også default-verdien, så `r` kan utelates om man vil.

Når vi har åpnet fila kan vi lese ut alt som tekst med funksjonen `read`. Legg til linjene under og kjør programmet.

```python
tekst = fil.read()
print(tekst)
``` 

Ser du noe rart i det som skrives ut? For eksempel at tittelen til "Fra bølle til bestevenn" ser ut som `Fra bÃ¸lle til bestevenn`. Det er fordi fila leses med feil tegnsett, men det kan vi løse ved å sette tegnsett eksplitt som argument til `open` ved å bruke parameteren `encoding`. Endre linja med `open` til følgende:
```
fil = open("serier.txt", "r", encoding="utf-8")
``` 
Her setter vi eksplisitt at fila er enkodet i `utf-8`.

En annen ting det er fint å gjøre når man har åpnet en fil er å lukke den pent etter seg når man er ferdig med den. Det er to måter å gjøre det på, den ene måten er å ha en linje etter at man er ferdig med filen, som lukker den, `fil.close()`. Det vi i stedet vil gjøre er å bruke en `with`-blokk. Da vet Python selv at den skal lukke fila når man går ut av blokken. og vi slipper å huske på å lukke fila, og finne ut hvor i koden det er lurt å lukke fila. Men `with` kan det se slik ut:
```python
with open("series.txt", "r", encoding="utf-8") as fil:
    tekst = fil.read()
    print(tekst)
```
Bytt ut innholdet i programmet ditt med linjene over og se at programmet kjører som før. 

Vi leser nå hele filen til en stor streng, men for å oppnå målet vårt med å skrive ut en liste med bare titlene må vi kunne lese hver linje for seg. Det er flere måter å få til det på, men string har metoden `splitlines` som vi vil bruke. Vi kan derfor bytte ut innholdet i `with`-blokka med følgende linjer:
```python
    linjer = fil.read().splitlines()
    for linje in linjer:
        print(linje)
```
Men fortsatt er vi ikke helt i mål, nå printer vi hele linja, ikke bare tittelen. For å få tak i tittelen kan vi bruke  `split`-metoden til string, som deler en streng for hver gang den finner den angitt skille-strengen.
 
✍️ **Oppgave:** _Kan du fullføre programmet slik at det bare skriver ut tittelen?_
```python
    for linje in linjer:
        deler = linje.split(",")
        # print(???)
```
