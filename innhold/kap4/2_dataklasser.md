# Dataklasser
**Data Classes**, også kalt dataklasser er en relativt ny, innebygd funksjonalitet i Python som gjør det lettere og sikrere å definere klasser. **Data class** transformerer en vanlig klasse til en klasse med mange av de objektorienterte funksjonene fra forrige kapittel ut av boksen. For eksempel init, repr og eq. Det gjør at man får mye av den samme funksjonaliteten med færre kodelinjer. En annen viktig del av dataklasser er bruk av typer i klassedeklareringen slik at det er enklere å jobbe med dataene i klassen når man vet hva den forventer.

## Hvordan lager jeg en data class?
For å bruke denne innebygde funksjonaliteten så må man bruke en dekoratør. Kort fortalt er dekoratører et verktøy som lar oss utvide oppførselen til en funksjon eller klasse uten å endre selve funskjonen eller klassen permanent. Les mer om dekoratører [her](https://docs.python.org/3/glossary.html#term-decorator).

Slik kan man lage klassen fra forrige kapittel ved å bruke dataklasser.

```python
from dataclasses import dataclass

@dataclass
class Person:
    navn: str
    alder: int
    by: str

p1 = Person("Vibeke", 54, "Oslo")
print(p1)  # Output: Person(Navn="Vibeke", Alder=54, By="Oslo")

p2 = Person("Vibeke", 54, "Oslo")

print(p1==p2) # Output: True
```

Her ser vi at vi har definert hvilken type et felt skal ha og hvis man for eksempel prøver å lage en Person med "54" som alder, så vil dette hintet dukke opp:
```python
Expected type 'int', got 'str' instead
```

**Oppgave:** _Skriv om Kanal-klassen fra forrige kapittel til å bruke dataclass_

## Hvilke andre funksjoner til dataclass kan det være lurt å vite om?
### Bruk av standard-verdier
I tillegg til vanlige type-annoteringer, kan man også spesifisere default-verdier.

```python 
@dataclass
class Bil:
    merke: str
    modell: str = "Ukjent"
```

Her vil modell ha en default verdi lik "Ukjent" dersom den ikke spesifiseres.

### Uforanderlige dataklasser
Ved å sette parameteren frozen=True kan du lage en uforanderlig dataklasse:
```python
@dataclass(frozen=True)
class UforanderligPunkt:
    x: float
    y: float
```
Etter at et objekt av denne klassen er opprettet, kan du ikke endre attributtene. Ethvert forsøk på å gjøre det vil resultere i en FrozenInstanceError.

### Bruk post-init for validering
Dersom du ønsker å utføre validering eller andre handlinger etter at et objekt er initialisert, kan du definere en __post_init__ metode:

```python
@dataclass
class Produkt:
    navn: str
    pris: float

    def __post_init__(self):
        if self.pris < 0:
            raise ValueError("Pris kan ikke være negativ!")

```
I eksemplet ovenfor vil en ValueError bli kastet dersom du prøver å lage et Produkt med en negativ pris.

**Oppgave:** _Legg til en validering for Kanal-klassen som sjekker at navnet til kanalen ikke er en tom streng og at kanallista ikke er tom_

## Når skal jeg bruke dataclass og når burde jeg bruke en vanlig klasse? 
**Data classes** er veldig nyttig når det ikke er noe kompleks logikk i konstruktøren til klassen. Noen ganger skjer det for eksempel validering og databasetilkoblinger i konstruktøren og da kan det være lurt å ha en helt egen konstruktør for det. Når det er sagt, så kan det være ryddigst å bruke klasser for å kun holde på data og da er **Data classes** veien å gå.
