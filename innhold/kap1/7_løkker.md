Løkker
======

**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke løkker for å gjøre ting flere ganger._

Løkker lar deg gjøre handlinger og operasjoner flere ganger, for eksempel ved å itere over alle elementene i en samling og slette elementene som matcher et spesifikt kriterie.
Vi skal se på to typer løkker, nemlig for-løkker og while-løkker.

## for-løkker

For-løkker benyttes vanligvis for å itere over en gitt samling for å utføre handlinger og operasjoner for hvert enkelt element. Løkka utfører altså én handling for hvert element i lista, uavhengig av hvor mange elementer som finnes i lista.
Variabelen for hvert enkelt element endres ved hver iterasjon, og eksisterer kun i «scopet» til for-løkka. I eksemplet under benytter vi kanal-lista vi tidligere så på, og hvis denne inneholder NRK1, NRK2, og NRK3 vil løkka kjøre tre ganger.
Ved første iterasjon vil variabelen 'kanal' være "nrk1", neste iterasjon "nrk2" og i siste iterasjon "nrk3".

En for-løkke kan altså defineres slik:

```python
for kanal in kanaler:
    print(kanal)                # Gjør noe med elementent, eller utfør andre handlinger
```

### ✍️ Oppgave 1
Her en liste over alle fornavnene til de andre i avdelingen din. 

```python
navneliste = ["Vibeke", "Aisha", "Carlos", "Vibeke", "Lise", "Fatima", "Per", "Leyla", "Oliver", "Vibeke", "Henrik", "Anna"]
```

Hvor mange i avdelingen din heter Vibeke? Bruk en for-løkke til å finne det ut.

### ✍️ Oppgave 2
Lag en quiz med tre spørsmål. Spørsmålene skal være strukturert i en liste der hvert element skal være en oppslagstabell med èn nøkkel for `spørsmål` og en annen for `svar`. Bruk for-løkka til å iterere over spørsmålene og ta inn svar fra brukeren ved å bruke `input`-funksjonen.

Et spørsmål kan se slik ut:
```python  
{"spørsmål": "Hva er hovedstaden i Norge?", "svar": "Oslo"}
```

Ta vare på hvor mange ganger brukeren har svart korrekt og skriv det ut når quizen er ferdig.

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

✍️ **Oppgave:** _Fra 1947 har vi avholdt kommunevalg hvert fjerde år. Kan du liste opp alle de årene fra da frem til i dag?_

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

Her har vi en variable kalt 'count' som har verdien 0. Denne verdien benyttes for å definere kriteriet til while-løkka; selve løkka skal altså kjøre helt til verdien til 'count' blir 5. I selve løkka øker vi verdien med én i hver iterasjon.

## Kontrollere løkker ved å bruke break
Ved å bruke `break` stopper vi utførelsen av løkka. I dette eksempelet lar vi brukeren gjette hvilket år NRK ble grunnlagt. 

### Eksempel: NRK-quiz med break
```python
# Definerer det årstallet som skal gjettes
korrekt_årstall = 1933

while True:
    # Tar inn brukerens gjett
    gjett = input("Når ble NRK grunnlagt? ")

    # Sjekker om inputen er et tall
    if gjett.isdigit():
        gjett = int(gjett)

        # Sjekker om brukerens gjett er riktig
        if gjett == korrekt_årstall:
            print("Gratulerer! Du gjettet riktig.")

            # Stopper utførelsen av løkka og quizen er ferdig.
            break
        else:
            # Gir hint til brukeren
            if gjett > korrekt_årstall:
                print("Feil. NRK ble grunnlagt før dette. Prøv igjen. \n")
            else:
                print("Feil. NRK ble grunnlagt etter dette. Prøv igjen. \n")
    else:
        print("Vennligst oppgi et årstall.")

# Tilbakemelding til brukeren etter at spillet er ferdig
print("Takk for at du spilte!")
```

## Kontrollere løkker ved å bruke flagg
Et flagg er en variabel som signaliserer når en bestemt betingelse er oppfylt. Det kan brukes for å kontrollere flyten av programmet. Vi bruker samme eksempel som ovenfor, men nå ved å bruke flagg i stedet for break.

### Eksempel: NRK-quiz med flagg
Vi vil bruke et flagg kalt `korrekt_gjett` for å avgjøre om brukeren har gjettet riktig.

```python
# Definerer det årstallet som skal gjettes
korrekt_årstall = 1933

# Initialiserer flagget
korrekt_gjett = False

while not korrekt_gjett:
    # Tar inn brukerens gjett
    gjett = input("Når ble NRK grunnlagt? ")

    # Sjekker om inputen er et tall
    if gjett.isdigit():
        gjett = int(gjett)

        # Sjekker om brukerens gjett er riktig
        if gjett == korrekt_årstall:
            print("Gratulerer! Du gjettet riktig.")
            korrekt_gjett = True
        else:
            # Gir hint til brukeren
            if gjett > korrekt_årstall:
                print("Feil. NRK ble grunnlagt før dette. Prøv igjen. \n")
            else:
                print("Feil. NRK ble grunnlagt etter dette. Prøv igjen. \n")
    else:
        print("Vennligst oppgi et årstall.")

# Tilbakemelding til brukeren etter at spillet er ferdig
print("Takk for at du spilte!")
```

Å bruke et flagg på den måte gjør koden mer lesbar ved å klart vise hva som er kriteriet til løkka.

## ✍️ Oppgave: Interaktiv handleliste

**Mål**: Skriv et program som lar brukeren legge til varer i en handleliste til hen bestemmer seg for å avslutte. Når hen avslutter, skal programmet skrive handlelisten ut til brukeren.

**Tips**:

1. Start med en tom handleliste.
2. Bruk en `while`-løkke for å be brukeren legge til varer.
3. Hvis brukeren skriver "AVSLUTT", skal programmet avsluttes og vise hele listen.
4. Hvis brukeren skriver inn noe annet, legg det til i handlelisten.
5. Hold styr på antall varer i listen og vis dette antallet før programmet avsluttes.

**Forventet interaksjon**:
```
Legg til en vare i handlelisten (eller skriv 'AVSLUTT' for å avslutte): Epler
Legg til en vare i handlelisten (eller skriv 'AVSLUTT' for å avslutte): Melk
Legg til en vare i handlelisten (eller skriv 'AVSLUTT' for å avslutte): Brød
Legg til en vare i handlelisten (eller skriv 'AVSLUTT' for å avslutte): AVSLUTT

Din handleliste:
1. Epler
2. Melk
3. Brød
Totalt 3 varer i handlelisten.
```

## Ekstra: Bruk av continue i løkker
Bruken av `continue` i en løkke kan være nyttig når du vil hoppe over en bestemt iterasjon basert på et gitt kriterie, men vil fortsette med de neste iterasjonene. 

### Eksempel: Skrive ut tall som ikke er delelige med 5 mellom 1 og 20

La oss si at du vil skrive ut tallene fra 1 til 20, men du vil hoppe over de tallene som er delelige med 5. Her kan `continue` brukes:

```python
for num in range(1, 21):
    if num % 5 == 0:  # Sjekker om tallet er delelig med 5
        continue
    print(num)
```
