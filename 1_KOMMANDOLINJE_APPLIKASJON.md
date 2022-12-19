Dag 1: Kommandolinjeapplikasjon
===============================

**💡 Læringsmål:** _I dag skal du lære å lage en enkel kommandolinjeapplikasjon som leser input fra fil og fra bruker og gir et fornuftig svar._

Hva skal vi lage i dag?
-----------------------
Når du er ferdig med denne dagen ender du opp med et program som fungerer omtrent som dette (fyll ut når man vet)

- forklare hva en kommandolinjeapplikasjon er


Vi leser data fra en fil (Heidi)
------------------------
- Helt enkelt tekstfil
    Programider nedover, eller to ting på en linje som de kan splitte opp
- Huske å lukke filen når man er ferdig. with (context managers).


Vi skriver data til en fil (Heidi)
--------------------------
- Helt enkel tekstfil
    Skriv programider og hvilken bærer disse har (kort forklaring om hva en bærer er?)


Programargumenter (Thorben)
-----------------
- Lese fra `sys.argv`
- Banalt eksempel (Hei, sys.argv!)
- Ugunstig med filnavn hardkodet i koden, men du kan jo lese det fra argumentlista!
    - Nevne tab-completion
- Printe hjelpemelding hvis du bruker `-h` eller `--help`
    - «Funket ikke med -h, da er det ingen hjelp å få»


Feilhåndtering (Teodor)
--------------
- Hva gjør vi hvis det ikke finnes en fil?
    - Hva kan gå feil: fila finnes ikke, feil filnavn, feil tillatelser, et annet program holder i filhåndtaket.
- Unntak (exceptions), try/except/finally, raise.
- Situasjoner hvor man returnerer to verdier, men én av indikerer en feil.
    - _Kun hvis det er plass til dette_
- Skrive ut med print(file=sys.stderr)

_Tips. `with` som vi akkurat har lært om, er egentlig bare en snedig variant av try/except/finally._


JSON: Et dataformat (Per Edvard)
-------------------
- Forklare hva JSON er, og hvordan JSON-data ser ut
- Introdusere JSON-støtte i standardbiblioteket.
    - Lese inn et JSON-objekt i en oppslagstabell.
    - Skrive inneholdet i en oppslagstabell til JSON.
- Lese inn en JSON-fil, til en liste med små oppslagstabeller i.
- Skrive data til en fil som JSON.


Stort og spennende eksempel som syr sammen trådene
--------------------------------------------------

- Lese lokasjon til fil fra argv
- Innholder JSON-data
- Manipulere
- Skrive til ny JSON-fil
- Gi tilbakemelding til terminalen om fremgangen
    - Skrive over samme linja flere ganger ved å avslutte med `\r`
- Si fra til terminalen om at vi er ferdige
