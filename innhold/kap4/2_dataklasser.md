# Dataklasser
**Data Classes** eller dataklasser er relativt ny, innebygd funksjonalitet i Python som gjør det lettere og sikrere å definere klasser. 

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

What are Data Classes?
Data classes are a new feature available in Python built-ins since version 3.7. They provide a decorator and functions to create simpler, more convenient, and safer classes that are mainly used to process data, hence the name.

One of the main benefits of Data Classes is that they automatically generate several special methods for you, such as __init__, __repr__ and __eq__. This can save you a lot of time and redundant code when defining classes that are primarily used to process data.

Another main benefit of Data Classes is the use of strong typing, which ensures that the attributes of an instance are defined. This is achieved through the use of type annotations, which allow you to specify the type of each attribute when defining the class. This can prevent bugs due to type ambiguities and also makes the code easier to catch for other developers.

ChatGPT
Hva er Dataklasser?


En av de viktigste fordelene med dataklasser er at de automatisk genererer flere spesialmetoder for deg, som for eksempel init, repr og eq. Dette kan spare deg for mye tid og unødvendig kode når du definerer klasser som hovedsakelig brukes til å behandle data.

En annen viktig fordel med dataklasser er bruk av sterk typetilordning, som sikrer at attributtene til en instans er definert . Dette oppnås ved bruk av typeanmerkninger, som lar deg spesifisere typen til hver attributt når du definerer klassen. Dette kan forhindre feil på grunn av typemisforståelser og gjør koden lettere å forstå for andre utviklere.