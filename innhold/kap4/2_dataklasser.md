# Dataklasser (WIP)
**Data Classes** eller dataklasser er relativt ny, innebygd funksjonalitet i Python som gjør det lettere og sikrere å definere klasser. Her får man mye av de objektorienterte funksjonene fra forrige avsnitt ut av boksen. init, repr og eq. En annen viktig fordel med dataklasser er bruk av sterk typetilordning

For å bruke denne innebygde funksjonaliteten så må man bruke en dekoratør.

Slik kan man lage klassen fra forrige kapittel ved å dataklasser.

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    navn: str
    alder: int
    by: str

p = Person("Vibeke", 54, "Oslo")
print(p)  # Output: Person(Navn="Vibeke", Alder=54, By="Oslo")

```

```python
class Person:
    def __init__(self, navn, alder, adresse):
        self.navn = navn
        self.alder = alder
        self.adresse = adresse
        
    def gå(self):
        print(self.navn, "går")
    
    def snakk(self):
        print(self.navn, "snakker")
```