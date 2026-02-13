Mer lek og moro med Elektronisk Program-Guide!
==========================================

**💡 Læringsmål:** _I dette kapittelet vil du lære hvordan enkeltdelene fra de foregående kapitlene kan brukes sammen for å utvide og forbedre EPG-programmet_

Nå som vi både har lært om kommandolinjeargumenter, kan hente data fra API , og kan lage moduler og pakker, kan vi forbedre programmet fra [kapittel 2.5](../kap2/5_oppgave.md).

Tidligere brukte vi en fil for å arbeide med EPG-data på JSON-format, men disse dataene finnes også i et API, som vi nå vil bruke istedet. 

Endepunktet for EPG-data for TV er https://psapi.nrk.no/tv/epg/, og endepunktet har egen [dokumentasjon](https://psapi.nrk.no/documentation/redoc/epg/2.0/). Det kan være litt uvant å lese en slik dokumentasjon i starten, men på høyre side kan vi se urlen til endepunktet, det står at det er en GET-metode med sti `/tv/epg/{channelIds}`, og vi ser hvordan responsen kan se ut.

I midtdelen står det noe om en path-parameter `channelIds` og en query-parameter `date`. 
Parameteren `channelIds` er påkrevd, og den må være en kommaseparert liste av kanal id-er man vil hente EPG for, for eksempel `nrk1` for bare NRK1, `nrk1,nrk2` for NRK1 og NRK2. Siden den er en path-parameter skal den være en del av stien, og settes inn i urlen der det står `{channelIds}`.  Parameteren `date`er en query-parameter på formatet `yyyy-mm-dd`, og om den utelates, får man EPG for dagens dato.

## Eksempler på bruk av endepunktet

| Url |  Forklaring |
|-----|-------------|
| `https://psapi.nrk.no/tv/epg/nrk3`| EPG for kanalen NRK3 på dagens dato |
| `https://psapi.nrk.no/tv/epg/nrk2?date=2026-01-01`| EPG for kanalen NRK2 på datoen 1. januar 2026 |
| `https://psapi.nrk.no/tv/epg/nrk2,nrksuper`| EPG for kanalene NRK2 og NRK Super på dagens dato |
| `https://psapi.nrk.no/tv/epg/nrk1,nrk3?date=2026-02-01`| EPG for kanalene P1, P13, NRK Super og NRK1 på datoen 1. januar 2023 |

## Hent EPG fra API-et

Oppdater EPG-programmet ditt fra tidligere til å hente data fra API-et i stedet for å lese fra fil. Bruk API-et uten å bruke parameteren for dato, og med de kanalene du ønsker. 

Formatet på JSON-en som kommer fra API-et er ganske lik som i fila vi brukte tidligere, men det er noen forskjeller. JSON-en fra API-et mange flere felter enn fila vi jobbet med tidligere og det er et nivå ekstra, `transmissionGroup`, mellom kanal og programmer. For å få tak i programmene må man loope over kanalene, for hver kanal loope over `transmissionGroups`, og for hver `transmissionGroup` hente ut `entries`, der programmene er. Men ikke alt under `entries` er programmer. Det kan man løse ved å filtere så man bare beholder entries med `itemType` lik `program` eller `episode`.

## La bruker angi dato og kanaler

Bruk det du har lært om kommandolinjeargumenter til å la bruker angi datoen og kanalene for EPG-en programmet skal bruke for å lage kategori-statistikk.

For å sette datoen som query-parameter når man gjør kall til API-et, kan man bruke en format-streng som vi har brukt når vi vil bruke verdi fra variabel i en tekst. Men det som er ryddigere, særlig om man har flere en én query-parameter, er bruke bibliotekets egne funksjonalitet for disse parametrene. Da må man lage en oppslagstabell for parametrene, sende de med som parameter `params` til  `requests.get`.

```python
parametre = {
    "date": "2023-10-16"
}
respons = requests.get("https://psapi.nrk.no/tv/epg/nrk2", params = parametre)
```

Kanalene, som er en path-parameter må fortsatt settes med en format-streng.


Eksperimenter med å angi ulike kanaler og datoer, og se om du ser noen mønstre i hvilke kategorier som brukes.

## Rydd i koden

Er det noe i programmet som kan ryddes? Lag moduler og eventuelt pakker der du synes det passer. Det kan være at lange sekvenser med kode bør deles opp i flere mindre funksjoner som kun utfører én oppgave, og som har et beskrivende navn. Kanskje er det også noen testutskrifter som kan fjernes, navn på variable og funksjoner som kan bli bedre, og lignende.
