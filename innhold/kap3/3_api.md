Applikasjonsprogrammeringsgrensesnitt (API) (Per Edvard)
==================================================================================

**💡 Læringsmål:**
_I dette avsnittet lærer du hva et API er og hva det benyttes til, og hvilke mulihgeter Python har til å arbeide med et API_

## Hva er et API?
API står for "Appication Programming Interface" og kan defineres som et set med protoller, definisjoner og verktøy for å bygge og integrere applikasjonsprogramvare.
Et API hjelper rett og slett applikasjoner, programvare, og tjenester med å kommunisere og utveklse data med hverandre!

Se for deg at kelneren i en restaurant er et API. På samme måte som kelneren mottar bestillingen din og viderefører den til kjøkkenet på restauranten,
så tar et API imot en forespørslel og viderefører denne til programvaren som utfører en bestemt handling.
Når programvaren har utført handlingen vil API'et videreføre en respons tilbake til tjenesten som opprinnelige sendte forespørselen,
tilsvarende kelneren som kommer med maten når kokken har tilberedt den.

En type API som vi skal se på og lære mer om i dette kapitlet er "web-API". 
Disse bruker vanligvis HTTP for å sende forespørsler, og dataen i tilbakemeldingene fra API'et er da vanligvis enten XML eller JSON.

Forespørslene tar da form som en URL, og ja, du kan for enkelte forespørsler ofte lime inn URL'en i nettleseren din og få svaret servert tilbake.
Hvis du for eksempel benytter følgende URL og skriver denne inn i addressefeltet til nettleseren vil du se at du får en tilbakemelding i JSON-formatet.
[https://psapi.nrk.no/ipcheck](https://psapi.nrk.no/ipcheck)

## HTTP metoder

## Arbeide med API'er i Python
I eksmeplet over er det nettleseren din som gjør forespørslen mot

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
