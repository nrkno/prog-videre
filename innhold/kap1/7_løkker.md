Løkker (Per Edvard)
=======

**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke løkker for å gjøre ting flere ganger._

Løkker lar deg gjøre handlinger og operasjoner flere ganger, for eksempel ved å itere over alle elementene i en samling og slette elementene som matcher et spesifikt kriterie.
Vi skal se på to typer løkker, nemlig for-løkker og while-løkker.

## for-løkker

For løkker benyttes for det meste for å itere over en gitt samling for å utføre handlinger og operasjoner for hvert enkelt element. Løkka utfører altså én handling for hvert element i lista, uavhengig av hvor mange elementer som finnes i lista.
Variablen for hvert enkelt element endres ved hver iterasjon, og eksisterer kun i «scopet» til for-løkka. I eksemplet under benytter vi kanal-lista vi tidligere så på, og hvis denne inneholder NRK1, NRK2, og NRK3 vil løkka kjøre tre ganger.
Ved første iterasjon vil variablen 'kanal' være "nrk1", neste iterasjon "nrk2" og i siste iterasjon "nrk3".

En for for-løkke kan altså definerers slik:

```python
for kanal in kanaler:
    print(kanal)                # Gjør noe med elementent, eller utfør andre handlinger
```

##  Generators

Man kan også benytte «genererings-funksjoner», eller «generators», i Python for å iterere over en en sekvens av verdier, i likhet med samlinger, men da uten at Python lagrer selve sekvensen i minnet slik som med en definert samling.
Og siden sekvensen ikke lagres i minnet og heller kun genereres «på sparket» så kan man kun iterere over disse én gang. Fordelen med «generators» er at de er veldig nyttige når man jobber med veldig store mengder data, eller bokstavelig talt uendelige sekvenser. 

Funksjonen `range()` er et eksempel på en «generator» i Python. Denne genererer en sekvens med nummer og defineres som følgende:

```python
range(start, stop, step)        # 'start' definerer det første nummeret i sekvensen
                                # 'stop' definerer det siste nummeret i sekvensen. Merk at nummeret ikke blir inkludert.
                                # 'step' definerer antallet det skal økes med
```

Eksemplet under starter altså sekvensen på `2`, går til `10`, men tar bare annenhvert tall.
Resultatet blir altså 2, 4, 6, 8.

```python
for i in range(2, 10, 2):
    print(i)
```

## while-løkker

While-løkker benyttes for å utføre handlinger og operasjoner så lenge et bestemt kriteriet er gitt. Det betyr at disse løkkene i teorien kan kjøre «for alltid» så lenge kriteriet for hva som skal stoppe løkka ikke gis, og dette må man være forsiktig med.

En while-løkke kan defineres slik:

```python
while kriterie:
    # handlinger eller operasjoner som skal utføres
```

Mer spesifikt:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

Her har vi en variable kalt 'count' som har verdien null. Denne verdien benyttes for å definere kriteriet til while-løkka; selve løkka skal altså kjøre helt til verdien til 'count' blir 5. I selve løkka øker vi verdien med en i hver iterasjon.

Mer å nevne:
    - 'Input fra bruker'
    - Flagg (true/false)
    - 'Break' og 'continue'
    - Oppgaver
