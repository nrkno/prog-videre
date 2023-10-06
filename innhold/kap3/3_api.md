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


## HTTP meldinger
En type API som vi skal se på og lære mer om i dette kapitlet er "web-API". 
Web-API som benytter HTTP sender meldinger som følger en bestemt standard, og kan deles inn i to typer; forespørsler og responser ("request" og "response"). Forespørslene er meldingene som sendes til API'et, mens responsen er svaret som API'et gir til tjenesten som sendte forespørselen.

Både forespørsler og responser har en lignende oppbygging og struktur

- Startlinje som beskriver metoden som forespørselen skal benytte, eller en status i responsen som forteller om forespørselen ble vellykket eller førte til feil.
- En valgfri "header" som gir ekstra kontekst eller metadata til meldingen
- En valgfri "payload body" som inneholder selve informasjonen i meldingen.

Eksempel på en HTTP-request melding:
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
Videre ser vi "/bestilling" som forteller hva "request-target" er. Altså hvilket endepunkt hos "host" meldingen skal ende opp på. Noen ganger kan "request-target" være en fullstending URL som f.eks. kan bestå av forskjellige parametere i tillegg, men i vårt eksempel lar vi den være kort og konsis.
Det siste vi ser er "HTTP/1.1" som indikerer hvilken versjon av HTTP som skal benyttes.

De to neste linjene spesifiserer hva som ligger i det som kalles "header". I eksemplet over finnes det to HTTP-headers, `host` og `content-type`. #TODO
Den siste delen under linjeskiftet etter "header"-delen er det som kalles "payload body".

Alle responser returnerer en statuskode som forteller noe om #TODO

## Metoder, payload og header
Web-API som benytter HTTP operer med et sett med metoder for forespørslene ("request methods") som sendes.
Disse [metodene](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) benyttes for å spesifisere hva slags type handling som skal utføres.
Det finnes en rekke av disse metodene, men i dette kapittelet skal vi forholde oss til kun noen få, og da spesifikt de som dekker
CRUD akronymet (**C**reate **R**ead **U**pdate **D**elete). Ikke alle API'er forholder seg helt likt til denne betegnelsen, men i dette kapittelet forsøker vi å forholde oss til den vanligste bruken av metodene som samsvarer med CRUD.

**Payload body**
Som nevnt tidligere kan en HTTP forespørsel noen ganger inneholde spesifikk informasjon i det som kalles "payload body", eller bare "body". Innholdet i denne er relevant for tjenesten som mottar meldingen, og tar vi utgangspunkt i eksemplet tidligere med kelneren i restauranten kan "body" sammenlignes med selve bestillingen som kelneren mottar fra deg.
Innholdet i "body" kan være ren tekst, eller det kan være JSON, XML eller lignende formater.

### POST - Create
Denne metoden sender data til API som mottar forespørslen, og betegner som oftest at noe skal opprettes i systemet bak tjenesten.

### GET - Read
Denne metoden benyttes for å spørre etter data hos et API. Selve forespørslen inneholder ikke noe body, men responsen fra API'et vil inneholdet dataen som ble etterspurt.

### PUT - Update
Denne metoden benyttes for å oppdatere noe i tjenesten bak et API. 

### DELETE - Delete
Denne metoden benyttes for å slette noe i tjenesten bak et API.

// TODO mer her
* responsekoder
* parametertyper

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

r = requests.get('https://psapi.nrk.no/ipcheck')

print(r.status_code)
print(r.headers)
print(r.text)
```

// TODO: mer her

* Først bruker vi requests til å kalle morsomme API som:
    - https://psapi.nrk.no/ipcheck
    - finn noe morsomt:
    - youtube
    - ping https://psapi.nrk.no/ping
    - rss, feks https://www.nrk.no/nyheter/siste.rss

