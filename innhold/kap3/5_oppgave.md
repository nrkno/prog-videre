Mer lek og moro med Elektronisk Program-Guide!
==========================================

**💡 Læringsmål:** _I dette kapitlet vil du lære hvordan enkeltdelene fra de foregående kapitlene kan brukes sammen for å utvide og forbedre EPG-programmet_

Nå som vi både har lært om kommandolinjeargumenter, kan hente data fra API , og kan lage moduler og pakker, kan vi forbedre programmet fra [kapittel 2.5](../kap2/5_oppgave.md).

Tidligere brukte vi en fil for å arbeide med EPG-data på JSON-format, men disse dataene finnes også i et API, som vi nå vil bruke istedet. 

Det spesifikke endepunktet for EPG-data er `https://psapi.nrk.no/epg/`, og og endepunktet har egen [dokumentasjon](https://psapi.nrk.no/documentation/redoc/epg/). Det kan være litt uvant å lese en slik dokumentasjon i starten, men på høyre side kan vi se urlen til endepunktet, det står at det er en GET-metode med sti `/epg/{channelIds}`, og vi ser hvordan responsen kan se ut. 

I midtdelen står det noe om en path-parameter `channelIds` og en query-parameter `date`. 
Parameteren `channelIds` er påkrevd, og den må være en kommaseparert liste av kanal id-er man vil hente EPG for, for eksempel `nrk1` for bare NRK1, `nrk2,p1,p2` for NRK2, P1 og P2. Siden den er en path-parameter skal den være en del av stien, og settes inn i urlen der det står `{channelIds}`.  Parameteren `date`er en query-parameter på formatet `yyyy-mm-dd`, og om den utelates, får man EPG for dagens dato.

## Eksempler på bruk av endepunktet

| Url |  Forklaring |
|-----|-------------|
| `https://psapi.nrk.no/epg/p1`| EPG for kanalen P1 på dagens dato |
| `https://psapi.nrk.no/epg/nrk2?date=2023-10-01`| EPG for kanalen NRK2 på datoen 1. oktober 2023 |
| `https://psapi.nrk.no/epg/nrk2,p1,p2`| EPG for kanalene NRK2, P1 og P2 på dagens dato |
| `https://psapi.nrk.no/epg/p1,p13,nrksuper,nrk1?date=2023-04`| EPG for kanalene P1, P13, NRK Super og NRK1 på datoen 1. januar 2023 |

## Hent EPG fra API-et

Oppdater EPG-programmet ditt fra tidligere til å hente data fra API-et i stedet for å lese fra fil. Bruk API-et uten å bruke parameteren for dato, og med de kanalene du ønsker. 

Formatet på JSON-en som kommer fra API-et matcher med fila vi brukte tidligere, forskjellen er at JSON-en fra API-et inneholder flere felter. Det betyr at koden vi skrev tidligere for å hente ut informasjon fra JSON-strukturen i fila fortsatt bør fungere når vi går over til å bruke API-et i stedet. Men virkelighetens data er ikke like perfekt som dataene i fila, det kan for eksempel hende at et program ikke har kategori. Det kan være at det vil kræsje programmet ditt, så det må du i så fall rette opp i. En mulig løsning er å bruke en jukse-kategori `ukjent` om programmet ikke har kategori.

## La bruker angi dato og kanaler

Bruk det du har lært om kommandolinjeargumenter til å la bruker angi datoen og kanalene for EPG-en programmet bruker for å lage kategori-statistikk.

Eksperimenter med å angi ulike kanaler og datoer, og se om du ser noen mønstre i hvilke kategorier som brukes.

## Rydd i koden

Er det noe i programmet som kan ryddes? Lag moduler og eventuelt pakker der du synes det passer. Det kan være at lange sekvenser med kode bør deles opp i flere mindre funksjoner som kun utfører én oppgave, og som har et beskrivende navn. Kanskje er det også noen testutskrifter som kan fjernes, navn på variable og funksjoner som kan bli bedre, og lignende.
