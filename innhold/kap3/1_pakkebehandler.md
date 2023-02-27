Pakkebehandler og pip (Thorben)
===============================

_Hvorfor skrive egen kode når du kan bruke andres? Velkommen til jungelen av bibliotekspakker!_

## Åpen kildekode

Når vi programmerer, ender vi ofte opp med å løse problemer som allerede har blitt løst av andre programmerer mange ganger før.
For eksempel det å gjøre nettverkskall til en server,
tolke et spesielt filformat,
ta i mot nettverkskall fra nettlesere med mer.
I stedet for at du må løse dette «ferdig løste» problemet enda en gang,
kan du gjenbruke løsninger som andre har skrevet før deg.

I utgangspunktet er all koden som du finner på nettet underlagt opphavsretten.
Den begrenser deg sånn at du ikke får lov til å kopiere og gjenbruke andres kode uten tillatelse,
på samme måte som du ikke kan skrive avskrift av ei bok du har kjøpt.
Du kan dog inngå en avtale med forfatteren som slår fast at du har lov til å bruke koden.

I praksis blir denne gjenbrukbare koden gjort tilgjengelig under en _«åpen kildekode»-lisens_.
En _lisens_ er en avtale som du kan velge å følge for å få visse rettigheter under bestemte vilkår,
uten at du må kontakte forfatteren, besøke et advokatkontor og signere en avtale i tre eksemplarer.
Lisenser for «åpen kildekode» vil som regel gi deg rett til å gjenbruke kildekoden,
men bare på visse betingelser.
Hvis du bryter med betingelsene så har du ikke lenger rett til å bruke koden.

De aller fleste lisensene har betingelser som er helt greie å oppfylle.
Men du bør være obs på at det finnes _copyleft_-lisenser som stiller krav til at også _din_ kode må være lisensiert med den samme lisensen.
Disse lisensene sørger for at en bedrift ikke bare kan nyttiggjøre seg av koden uten å donere forbedringene tilbake til fellesskapet.
Motsatt finnes _permissive_-lisenser som nesten ikke stiller noen krav i det hele tatt.

Nettstedet https://choosealicense.com/ gir en fin introduksjon til hvilken lisens du bør velge hvis du selv ønsker å dele kildekoden din.
På undersiden https://choosealicense.com/appendix/ kan du slå opp lisenser som du finner der ute på nettet,
for å få oversikt over hvilke rettigheter de gir deg og
hvilke betingelser som følger med.

På nettet kan du finne mye åpen kildekode på nettsteder som [GitHub.com](https://github.com).
Du kan kopiere kode fra prosjekter du finner der og bruke den i ditt eget prosjekt,
så lenge koden er lisensiert med en «åpen kildekode»-lisens og du oppfyller lisensens betingelser.
Lisensen ligger som regel i ei fil som heter `LICENSE` eller `LICENSE.txt`
i den øverste mappa i prosjektet,
eller den er nevnt øverst i hver enkelt kodefil.
[Hvis du ikke finner noen lisens][no-license] så må du bare anta at koden ikke er åpen kildekode.

[no-license]: https://choosealicense.com/no-permission/

Åpen kildekode utvikles i fellesskap.
Hvis du finner en feil eller har forslag til forbedring,
kan du som oftest melde dette på prosjektets nettside.
Du kan også foreslå endringer i koden og bidra som frivillig.
Det er dessverre et problem i dette økosystemet med at vi har veldig viktige åpne programvarer
som store bedrifter har gjort seg helt avhengige av å bruke,
som sliter med å holde programvaren oppdatert og fri for feil fordi alle er veldig glade i å bruke koden,
men ingen er villige til å legge ned tid og krefter i å vedlikeholde den.
Som poengert av XKCD:

[![Tegneserie der "All modern digital infrastructure" er en høy stabel med esker som balanserer oppå en veldig liten eske kalt "A project some random person in Nebraska has been thanklessly maintaining since 2003"](https://imgs.xkcd.com/comics/dependency.png)](https://xkcd.com/2347/)


## Pakker

Det å kopiere kode fra andres prosjekter inn i ditt prosjekt har noen svakheter:

* Du får ikke med oppdateringer som blir gjort på koden du kopierte fra,
  for eksempel hvis det var en viktig sikkerhetsfeil som ble fikset.
* Koden du kopierer fra kan gjenbruke andres kode i tur,
  som gjør at du potensielt må kopiere inn den koden, og så videre.

Å la deg inspirere av andres åpne kildekode eller kopiere én funksjon eller noen få kodelinjer pleier å gå greit,
men det øyeblikket du vil gjenbruke mer så bør du gjøre det i mer ordna former.

For å gjøre det lettere å gjenbruke andres kode, organiserer vi gjenbrukbar kode i _pakker_.
Ei pakke har et pakkenavn og kan også ha flere versjoner,
der hver versjon er identifisert med et versjonsnummer.
Ei pakke består av ei samling med kodefiler som er pakket sammen i én fil.
Disse pakkene kan installeres, litt på samme måte som du installerer et dataprogram på maskinen din.
Hver pakke kan også ha _avhengigheter_ (dependencies) til andre pakker,
som må installeres for at pakken skal fungere.

For å installere, avinstallere og holde styr på installerte pakker bruker vi en _pakkebehandler_.
I Python er det en innebygd pakkebehandler ved navn [pip],
men den har ikke noen god innebygd funksjonalitet for å holde styr på hvilke pakker prosjektet ditt krever er installert.
Vi skal derfor bruke en pakkebehandler som heter [Poetry].

[pip]: https://packaging.python.org/en/latest/tutorials/installing-packages/#use-pip-for-installing
[Poetry]: https://python-poetry.org/


## Installere Poetry

Poetry har et eget Python-skript du kan kjøre for å installere det.
Følg [installasjonsveiledningen til Poetry](https://python-poetry.org/docs/#installation).

Når du har installert Poetry, skal du kunne kjøre `poetry --version` i terminalen.


### venv?
- Eller skal vi heller bytte ut pip med [poetry](https://python-poetry.org/)?
