Applikasjonsprogrammeringsgrensesnitt (API) (Per Edvard)
==================================================================================

**💡 Læringsmål:**
_I dette avsnittet lærer du hva et API er og hva det benyttes til, og hvilke muligheter Python har til å arbeide med et API_


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

De to neste linjene spesifiserer hva som ligger i det som kalles "header". 


## Metoder, payload og header
Web-API som benytter HTTP operer med et sett med metoder for forespørslene ("request methods") som sendes.
Disse [metodene](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) benyttes for å spesifisere hva slags type handling som skal utføres.
Det finnes en rekke av disse metodene, men i dette kapittelet skal vi forholde oss til kun noen få, og da spesifikt de som dekker
CRUD akronymet (**C**reate **R**ead **U**pdate **D**elete). Ikke alle API'er forholder seg helt likt til denne betegnelsen, men i dette kapittelet forsøker vi å forholde oss til den vanligste bruken av metodene som samsvarer med CRUD.

**Payload body**
Som nevnt tidligere kan en HTTP forespørsel noen ganger inneholde spesifikk informasjon i det som kalles "payload body", eller bare "body". Innholdet i denne er relevant for tjenesten som mottar meldingen, og tar vi utgangspunkt i eksemplet tidligere med kelneren i restauranten kan "body" sammenlignes med selve bestillingen som kelneren mottar fra deg.
Innholdet i "body" kan være ren tekst, eller det kan være JSON, XML eller lignende formater.

### POST - Create
Denne metoden sender data til tjenesten som mottar meldingen, og betegner som oftest at noe skal opprettes bak tjenesten som mottar meldingen.

## Arbeide med API'er i Python
I eksemplet over er det nettleseren din som gjør forespørslen mot



Kladd:

Forespørslene tar da form som en URL, og ja, du kan for enkelte forespørsler ofte lime inn URL'en i nettleseren din og få svaret servert tilbake.
Hvis du for eksempel benytter følgende URL og skriver denne inn i adressefeltet til nettleseren vil du se at du får en tilbakemelding i JSON-formatet.
[https://psapi.nrk.no/ipcheck](https://psapi.nrk.no/ipcheck)


* Her installerer vi bibliotekspakken som heter requests.
* Først bruker vi requests til å kalle morsomme API som:
    - https://psapi.nrk.no/ipcheck
    - finn noe morsomt:
    - youtube
    - ping https://psapi.nrk.no/ping
    - rss, feks https://www.nrk.no/nyheter/siste.rss

* Så bruker vi requests til å kalle epg-endepunktet.
* Fra programmet sist: Bytt ut json fra fil med json fra endepunkt
* Oppgave: Bruk programargument til å velge dato
