# Objektorientert programmering i Python
Python er et objektorientert språk, som betyr at all data og funksjoner i Python er representert i objekter. **Objektorientert programmering** fokuserer på å strukture programmer slik at man samler egenskaper og oppførsel i *objekter*.

Objektorientert programmering er en måte å modellere virkeligheten på. For eksempel, et objekt kan representere en person med egenskaper som navn, alder eller adresse og oppførsel som for eksempel å gå, snakke eller puste. Eller det kan representere en handlekurv med egenskaper som beskriver hvilke varer som er i handlekurven og oppførsel for å legge til eller fjerne varer. Man kan også modellere

En annen måte å gjøre det på kan være **prosedyreorientert programmering** der man strukturer et program som en slags oppskrift med forskjellige steg. Stegene kan være bygd opp av funksjoner og kode som utføres etter hverandre for å utføre en oppgave. Hovedforskjellen her er at objektene er i sentrum av objektorientert programmering i Python. Ikke bare for å representere data, som i prosedyreorientert programmering, men også i selve struktureringen av kode.

# Definere klasser i Python
En klasse i Python er en blåkopi eller en mal for å lage objekter. Det definerer egenskapene og oppførselen til objektene som skal opprettes. Egenskaper kalles ofte attributter eller variabler, mens oppførselen er definert av funksjoner som kalles metoder.

For eksempel kan vi definere en klasse som heter "Person", som kan inneholde egenskaper som "navn", "alder", og "adresse", og metoder som "gå" og "snakke". Vi kan så opprette objekter av klassen "Person" for å representere konkrete personer i koden vår.

Her er et eksempel på hvordan du kan definere en enkel klasse i Python:

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

Vi kan nå opprette et objekt av klassen "Person" ved å kalle konstruktøren __init__ med de nødvendige parameterne:

```python
person1 = Person("Vibeke", 54, "Bjørnstjerne Bjørnsons plass 1")
```
Her har vi opprettet et personobjekt som heter "person1" med navnet "Vibeke", alderen 54, og adressen "Bjørnstjerne Bjørnsons plass 1". Vi kan nå kalle metodene til personobjektet for å utføre handlingene de representerer:

```python
person1.gå()  # output: Vibeke går
person1.snakk()  # output: Vibeke snakker
```

