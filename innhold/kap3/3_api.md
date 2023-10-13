Applikasjonsprogrammeringsgrensesnitt (API)
===========================================

**💡 Læringsmål:**
_I dette kapitlet lærer du hva et API er og hva det benyttes til, og hvilke muligheter Python har til å arbeide med et API_

## Hva er et API?
API står for "Application Programming Interface" og kan defineres som et set med protokoller, definisjoner og verktøy for å bygge og integrere applikasjonsprogramvare.
Et API hjelper rett og slett applikasjoner, programvare, og tjenester med å kommunisere og utveksle data med hverandre.

Se for deg at kelneren i en restaurant er et API. På samme måte som kelneren mottar bestillingen din og viderefører den til kjøkkenet på restauranten, så tar et API imot en forespørsel og viderefører denne til programvaren som utfører en bestemt handling.
Når programvaren har utført handlingen vil API'et videreføre en respons tilbake til tjenesten som opprinnelige sendte forespørselen,
tilsvarende kelneren som kommer med maten når kokken har tilberedt den.


## HTTP-meldinger
En type API som vi skal se på og lære mer om i dette kapitlet er web-API.

Web-API som benytter HTTP sender meldinger som følger en bestemt standard, og kan deles inn i to typer; forespørsler og responser (`request` og `response`). Forespørslene er meldingene som sendes til API'et, mens responsen er svaret som API'et gir til klienten som sendte forespørselen.

Både forespørsler og responser har en lignende oppbygging og struktur:

- En startlinje som beskriver metoden som skal benyttes når det er en forespørsel, eller om meldingen er en respons, en statuskode forteller om forespørselen var vellykket eller førte til feil.
- En valgfri "header" som gir ekstra kontekst eller metadata til meldingen
- En blank linje
- En valgfri "payload body" som utgjør selve innholdet i meldingen.

Eksempel på en HTTP-forespørsel:

```
POST /bestilling HTTP/1.1
Host: restaurant.com
Content-Type: plain/txt

Forrett: Gresskarsuppe
Hovedrett: Kalkun
Dessert: Iskrem
Drikke: Vann 
```

Den første linjen i eksemplet over viser hva startlinjen inneholder. Det første ordet i linjen er "POST" og dette viser hvilken HTTP-metode som skal benyttes.
Videre ser vi "/bestilling" som forteller hva "request-target" er. Altså hvilket endepunkt hos "host" meldingen skal ende opp på. Noen ganger kan "request-target" være en fullstendig URL som f.eks. kan bestå av forskjellige parametere i tillegg, men i vårt eksempel lar vi den være kort og konsis.
Det siste vi ser er "HTTP/1.1" som indikerer hvilken versjon av HTTP som benyttes.

De to neste linjene spesifiserer hva som ligger i det som kalles "header". I eksemplet over finnes det to HTTP-headers, `host` og `content-type`. Den siste delen under linjeskiftet etter "header"-delen er det som kalles "payload body", som utgjør selve innholdet i meldingen som sendes. 

Responsen på forespørselen over kan se ut på følgende måte:

```
HTTP/1.1 201 Created
Content-Type: text/plain

Bestillingen din er registrert! Dine valg er:
Forrett: Gresskarsuppe
Hovedrett: Kalkun
Dessert: Iskrem
Drikke: Vann

Takk for din bestilling! Den blir snart behandlet.
```

I responsen er inneholder første linje en statuskode i stedet for HTTP-metode og url som det var i forespørselen. 

### Metoder

Web-API som benytter HTTP operer med et sett med metoder for forespørslene ("request methods") som sendes.
Disse [metodene](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) benyttes for å spesifisere hva slags type handling som skal utføres.
Det finnes en rekke av disse metodene, men i dette kapittelet skal vi forholde oss til kun noen få, og da spesifikt de som dekker
CRUD akronymet (**C**reate **R**ead **U**pdate **D**elete). Ikke alle API'er forholder seg helt likt til denne betegnelsen, men i dette kapittelet forsøker vi å forholde oss til den vanligste bruken av metodene som samsvarer med CRUD.

| HTTP Verb | CRUD ekvivalent | Beskrivelse |
|-----------|-----------------|-------------|
| POST | Create | Denne metoden sender data til API som mottar forespørselen, og betegner som oftest at noe skal opprettes i systemet bak tjenesten.|
| GET | Read | Denne metoden benyttes for å spørre etter data hos et API. Selve forespørselen inneholder ikke noe body, men responsen fra API'et vil inneholdet dataen som ble etterspurt.|
| PUT | Update | Denne metoden benyttes for å oppdatere noe i tjenesten bak et API. |
| DELETE | Delete | Denne metoden benyttes for å slette noe i tjenesten bak et API.|

### Statuskoder

Statuskoden i en respons forteller hvordan det gikk med behandlingen av en forespørsel. Den kan ha feilet, da sier statuskoden noe om hva slags type feil som skjedde. Hvis forespørselen var vellykket kan statuskoden gi nyttig tilleggsinformasjon.

Statuskoden er en tresifret kode der første siffer sier noe om hva slags type status det dreier seg om, tabellen viser de ulike typene.

| Statuskode | Type | Forklaring |
|------------|------|------|
| 1xx        | Informerende | Forespørselen er mottatt og den prosesseres |
| 2xx | Vellykket | Forespørselen ble vellykket mottatt, forstått og akseptert |
| 3xx | Videresending | Forespørselen ble videresendt |
| 4xx | Klientfeil | Forespørselen inneholder feil og kan ikke fullføres |
| 5xx | Tjenerfeil | Tjeneren feilet i å fullføre forespørselen | 

De mest vanlige statuskodene er de som starter på 2, 4 og 5. Det er vanlig å se `200 OK` når alt gikk bra, `201 Created` om noe har blitt opprettet på tjenersiden, og `204 No Content` om forespørselen var vellykket, men responsen er tom. Av feilkoder er de vanlige `400 Bad Request` om klienten sender noe feil, `401 Unauthorized` eller `403 Forbidden` om man ikke har tilgang til tjenesten eller ikke har autentisert seg på riktig måte. På tjenersiden er `500 Internal Server Error` og `503 Service Unavailable` vanlige, den første er typisk at noe uventet skjer på tjeneren, mens den siste forekommer når en tjener er overbelastet.

### Header

Header-delen av en melding består av linjer som er delt inn i nøkkel og verdi (som i Pythons oppslagstabeller), med en kolon som skilletegn. Det er kun ett nøkkel-verdi-par per linje. 

Dataene som fins header-felter er som oftest ikke interessante for en sluttbruker, men brukes for å utveksle informasjon mellom tjener og klient. Det fins en rekke faste nøkler som brukes, i tillegg kan tjener og klient fritt legge til egne.

Av de vanlige er `Accept` som klienten kan bruke for å angi hva slags type innhold den ønsker å få tilbake i body, og både klient og tjener kan angi `Content-Type` for å si hva slags type innhold som er i body i meldingen de sender. For eksempel `application/json` for meldinger som inneholder JSON eller `text/html` for meldinger som inneholder html. I sistnevnte tilfelle vil headeren i meldingen inneholde `Content-Type: text/html`. [Wikipedia](https://en.wikipedia.org/wiki/Media_type) har en liste over vanlige mediatyper. 

### Body

En HTTP forespørsel eller respons inneholde informasjon i det som kalles "payload body", eller bare "body", dette er den egentlige informasjonen som partene i meldingsutvekslingen ønsker å sende til hverandre. Tar vi utgangspunkt i eksemplet over med kelneren i restauranten kan "body" i forespørselen sammenlignes med selve bestillingen som kelneren mottar fra deg. Responsen tilsvarer det kelneren kunne svart tilbake. Han gjentar bestillingen så du kan sjekke at den ble riktig, og han forteller at den snart lages.

Innholdet i "body" kan være ren tekst, eller det kan være JSON, XML, HTML eller andre formater, informasjon om hva meldingen inneholder finnes i header-feltet `Content-Type`. Når en forespørsel sendes kan headeren `Accept` settes for å angi hva slags format klienten godtar for innholdet i responsen.  

## Arbeide med API'er i Python
I et web-API tar forespørslene form som en URL, og ja, du kan for enkelte forespørsler ofte lime inn URL'en i nettleseren din og få svaret servert tilbake.
Hvis du for eksempel benytter følgende URL og skriver denne inn i adressefeltet til nettleseren vil du se at du får en tilbakemelding i JSON-formatet.
[https://psapi.nrk.no/ipcheck](https://psapi.nrk.no/ipcheck). Her gjør altså nettleseren din en GET-forespørsel mot ps-api og svaret den mottar vises i nettleservinduet, litt som med en vanlig nettside.

I Python har man en rekke bibliotek og rammeverk for å sende spørringer og motta svar fra API.
Et populært og mye brukt bibliotek er [requests](https://requests.readthedocs.io/en/latest/). 
Det er dette biblioteket vi kommer til å benytte i dette kapittelet, men du står selv fritt til å velge andre HTTP-bibliotek eller rammeverk som finnes i Python hvis du ønsker.

✍️ **Oppgave** Biblioteket `requests` er ikke standard i Python, og må derfor installeres. Installer `requests` basert på det du lærte om [pakkebehandling i kapittel 3.1](1_pakkebehandler.md).

Etter at `requests` er installert kan vi prøve å sende samme forespørslen mot ps-api som over, men denne gangen fra et Python script og ikke via nettleser.
```python
import requests

respons = requests.get('https://psapi.nrk.no/ipcheck')

print(respons.status_code)
print(respons.headers)
print(respons.text)
```

Variabelen `response` er et objekt av typen [Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) som inneholder mye ulik informasjon om responsen. Blant annet `.status_code` som er nyttig for å vite om kallet gikk bra eller ikke, `.headers` for å hente ut headerne og selve responsen kan man hente ut som rå tekst `.text`. 

I eksempelet over ser vi at responsen egentlig er på JSON-format, og da ønsker man vanligvis i kode å få dette parset til en en oppslagstabell, slik som da vi tidligere leste JSON fra fil. Bibloteket `requests` har heldigvis støtte for dette også, responsobjektet har metoden `json()` som man kan kalle for å få ut.

✍️ **Oppgave** Lag en variabel for å holde på resultatet av å kalle `response.json()`, og skriv ut IP-en din, som fins i feltet `clientIpAddress` i JSON-objektet

✍️ **Oppgave** Test å legge til noen tilfeldige tegn i slutten av urlen som brukes i `requests.get()`, hva slags respons får du da?

✍️ **Oppgave** Det fins et eget api som gir farger til radio og tv, nemlig fargerik. Og det har et eget endepunkt for å hente ut fargene som brukes for en gitt tv-kanal. For eksempel `https://fargerik-psapi.nrk.no/tv/channel/nrk1` for å hente ut fargene for NRK 1. Bruk `requests.get()` til å kalle endepunktet. Skriv ut headere, og  finn ut hva slags `Content-Type` som brukes i responsen. 

Vi vil gjerne ha JSON tilbake, og API-et støtter at hvis vi ber om JSON ved å bruke `Accept`-headeren når vi sender responsen, får vi JSON tilbake. Requests sin `get`-funksjon kan ta inn et argument, `headers`, som må være en oppslagstabell der nøkkel er navn på headeren man vil sette og verdien er verdien headeren skal ha. I vårt tilfelle vil vi sette `Accept` til å være `application/json`. Gjør kallet igjen men nå med parameteren `headers`, og se at responsen du får tilbake er på JSON-format.

// TODO: poste melding
// TODO: oppgaver med å teste ut morsomme apier

## Videre lesning

* [HTTP - Wikipedia](https://en.wikipedia.org/wiki/HTTP)
* [HTTP Headers - Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
* [Mediatyper - Wikipedia](https://en.wikipedia.org/wiki/Media_type)
* [HTTP Statuskoder - Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
