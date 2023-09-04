# Programmeringskurs

## [→ Åpne kursets nettside](https://nrkno.github.io/prog-videre)

_Under arbeid - vi jobber med å utvikle et nytt pythonkurs!_

Mens du venter på kurset kan du se på [Datastart](https://tv.nrk.no/serie/datastart)


## Tidsplan

Bruke 2 x 2 timer pr kapittel i kurset
Vurdere om dag 0 skal også være det (ellers 3 timers økt?)

Hvordan hjelpe folk med å velge om de trenger dag 0:
- Gi et eksempel på kode man bør skjønne?
- henvise til ting man skal lære? 


## Hvordan bygge nettsida?

Vi bruker [mdbook] til å lage en nettside ut av Markdown.

Vi bruker i tillegg to plugins:
* [mdbook-mermaid] til å generere diagrammer
* [mdbook-toc] til å lage innholdsfortegnelser for navigering innad i et dokument

Alle tre kan installeres ved å velge den nyeste utgivelsen på GitHub, laste ned fila som passer til din maskin, pakke den ut og legge den til i `PATH`.
Da kan du jobbe med innholdet samtidig som du ser det ferdige resultatet med `mdbook serve`.

Nettsida som vi har i GitHub Pages blir automatisk lagd av GitHub Actions ved push til `main`-greina.

[mdbook]: https://rust-lang.github.io/mdBook/
[mdbook-mermaid]: https://github.com/badboy/mdbook-mermaid
[mdbook-toc]: https://github.com/badboy/mdbook-toc

## Diplom

lages ved å bruke nrk logo generator - burde oversettes til Python

## For senere?

### Api - lage api (ekstra, et annet kurs)
* flask? FastAPI?
* valgfrie seksjoner (ligger på øverste nivå, lenkes inn fra dagene)
  * objektorientering (dataklasser) 
  * decorators
* Lærer verktøy for å lage egne apier (godt utgangspunkt for githubactions/kuberneteskurs)

## Ekspert-temaer
* venv
