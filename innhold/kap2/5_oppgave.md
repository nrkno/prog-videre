Lek og Moro med Elektronisk Program-Guide! (Heidi)
===================================================

**💡 Læringsmål:** _I dette avsnittet lærer du hvordan enkeltdelene i dag 1 kan settes sammen og bli til et nyttig program_

Vi skal i korte trekk lage et program som:
1. Leser inn Elektronisk Program-Guide (EPG) for flere kanaler fra en JSON-fil.
2. Teller opp hvor mange programmer som finnes i hver kategori.
3. Skriver ut antall programmer per kategori, i synkende rekkefølge, til terminalen.

Vi har også mange andre ideer til ting du kan eksperimentere med når du er ferdig med listen over, i tillegg får du kanskje ideer selv underveis til ting du vil teste ut.

## Hva er Elektronisk Program Guide (EPG)?

[EPG](https://en.wikipedia.org/wiki/Electronic_program_guide) er en programoversikt, gjerne for en gitt dato, som viser sendeplanen for lineærkanalene. Oversikten har start- og stopptidspunkt, tittel og annen informasjon om programmene som skal sendes.  

Filen(e) vi skal bruke i programmet vårt inneholder json med følgende struktur for en kanal:

```json
{
    "id": "epg_nrk1",
    "channel": {
        "id": "nrk1",
        "title": "NRK1",
        "sourceMedium": 1,
        "isLive": true,
        "hasEpg": true,
        "isOndemandChannel": true,
        "isDistrictChannel": false,
        "hasDistrictChannels": true,
        "priority": 1
    },
    "entries": [
        {
            "programId": "NNFA05022723",
            "seriesId": "nyhetsmorgen-tv",
            "category": {
                "id": "nyheter",
                "displayValue": "Nyheter",
                "isTvCategory": true,
                "isRadioCategory": true
            },
            "legalAge": null,
            "title": "Nyhetsmorgen",
            "description": "Nyhetsmorgen, Politisk kvarter og Kulturnytt – alt du trenger for en oppdatert start på dagen. Direkte fra studio 50 hver morgen."
        }
    ]
}
```
Dette formatet er en forenkling av det som brukes i [TV guiden på tv.nrk.no](https://tv.nrk.no/guide), som passer fint for det vi skal lage nå. Filen inneholder en liste av kanaler, og hver kanal har et felt `entries` som igjen inneholder en liste over alle programmene som skal gå på kanalen denne dagen. 

I utdraget over vises det én kanal med ett program, men i filen vil det være flere kanaler og hver kanal har flere programmer.

## Kom i gang

Start med en tom Python-fil eller ta utgangspunkt i filen [epg.py](/oppgave/epg.py). Denne filen inneholder en funksjon som er kjekk å ha til ekstraoppgavene. 

Kopier filen [epg.json](/oppgave/epg.json) til samme mappe som Python-filen over. Dette er filen som vi skal få Python-programmet til å lese og prosessere.

## Les json fra fil

Bruk det du lærte i del [1](1_lese_fil), [3](3_feilhåndtering) og [4](4_json) til å lese innholdet i `epg.json`som json. I første omgang kan du bare skrive ut innholdet av json-objektet til terminalen som verifikasjon på at filen er lest inn.   

## Tell opp antall programmer for hver kategori

I stedet for å skrive ut jsonen til terminalen må vi hente ut kategorien for hvert program, og lagre kategoriene i en passende struktur. En mulig måte å gjøre dette på er å lage en oppslagstabell der kategoriene er nøkler og antall programmer for den gitte kategorien er verdien.

```
{
    "nyheter": 7,
    "dokumentar": 4
}
```
For å få til dette må vi iterere over listen av kanaler, og for hver kanal interere gjennom programmene, og til sist, for hvert program må vi hente ut katogorien. Dette kan for eksempel løses med to `for`-løkker inni hverandre. Når man har fått tak i kategorien må oppslagstabellen oppdateres. Om man bruker kategoriens `id` som nøkkel må man sjekke iden finnes finnes i oppslagstabellen fra før, i såfall må man øke verdien med 1. Hvis ikke, må den nye nøkkelen legges til i tabellen.

__Gratulerer, du har et fiks ferdig program! 🎉__

## Lag mer gøy! 🎨

Om du har fullført stegene over kan du utvide programmet ditt hvis du har lyst. Du kan for eksempel prøve på å:

- Skrive antallet programmer per kategori til en JSON-fil, i stedet for til terminalen.
- La programmet spørre brukeren om å angi en kategori, og gi tilbake informasjon om programmer som har denne gitte kategorien. For at brukeren skal kunne velge kategori kan det være lurt å liste ut mulige kategorier i terminalen først.
- La programmet spørre brukeren om en tidsperiode i minutter, og gi tilbake informasjon om programmer som varer like lenge eller kortere. Dette er nyttig om du vil se eller høre på noe men bare har en gitt tid til rådighet.
- Har du en idé selv til en utvidelse, test den ut!

### 🎯 Kan det du gjør på jobb bli mer effektivt med et Python program?

Temaene vi har jobbet med i dag kan kanskje brukes direkte i noe du gjør på jobb, f.eks om du manuelt henter ut informasjon fra filer. Om du har filer på andre format enn `json` kan de fortsatt leses og tolkes, enten manuelt eller ved å bruke andre biblioteker. Det fins for eksempel en eget [csv-bibliotek](https://docs.python.org/3/library/csv.html) for å håndtere `csv`-filer.
