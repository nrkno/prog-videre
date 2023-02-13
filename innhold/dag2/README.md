Dag 2: Hente data fra API
=========================

Pakkebehandler og pip (Thorben)
--------------------------------
_Hvorfor skrive egen kode når du kan bruke andres? Velkommen til jungelen av bibliotekspakker!_

### venv?
- Eller skal vi heller bytte ut pip med [poetry](https://python-poetry.org/)?


Programargumenter (Thorben)
-----------------
* Det er et bibliotek som heter click
* Her kommer det inn dekoratører, men det gjør vi veldig kort.
* Her er oppgaven på slutten av avsnittet at man skal skrive om programmet fra dag 1 til å bruke programargumenter.


Applikasjonsprogrammeringsgrensesnitt (API) (Up for grabs - skriv navnet ditt her)
----------------------------------------------------------------------------------
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

Organisering med moduler og pakker (Up for grabs - skriv navnet ditt her)
-------------------------------------------------------------------------
* skriv noe om moduler og pakker (modul = fil, pakke = mappe med `__init__` fil)
* trekk leseren gjennom et eksempel for moduler og pakker
* skriv om programmet man jobber med til å bruker moduler og pakker


Flere oppgaver
--------------
* Støtte datospenn og gjøre apikall for alle datoene i spennet, akkumulere resultatet
