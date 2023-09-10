# Dataklasser
**Data Classes**, også kalt dataklasser er relativt ny, innebygd funksjonalitet i Python som gjør det lettere og sikrere å definere klasser. Færre kodelinjer, med samme funksjonalitet. Her får man mye av de objektorienterte funksjonene fra forrige avsnitt ut av boksen. init, repr og eq. En annen viktig fordel med dataklasser er bruk av typer i klassedeklareringen slik at det er enklere å jobbe med dataene i klassen når man vet hva den forventer.

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

**Oppgave:** _Skriv om Kanal-klassen fra forrige kapittel til å bruke dataclass_


Bruk field for standard-verdier

Bruk frozen

Bruk post-init for validering