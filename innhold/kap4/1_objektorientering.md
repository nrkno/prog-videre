# Objektorientert programmering i Python
Python er et **objektorientert språk(OOP)**, som betyr at et program er strukturert slik at egenskaper og oppførsel er representert i objekter. Et objekt kan for eksempel representere et menneske med egenskaper som navn, alder eller by og oppførsel som for eksempel å gå, snakke eller puste. Eller det kan representere en handlekurv med egenskaper som beskriver hvilke varer som er i handlekurven og oppførsel for å legge til eller fjerne varer. 

Sagt på en annen måte så kan man si at objektorientert programmering er en måte å modellere virkeligheten på. Både ved å definere egenskapene og oppførselen til forskjellige ting, men også relasjonen mellom dem.

En annen måte å gjøre det på kan være **prosedyreorientert programmering** der man strukturer et program som en slags oppskrift med forskjellige steg. Stegene kan være bygd opp av funksjoner og kode som utføres etter hverandre for å utføre en oppgave. Hovedforskjellen er at objektene er i sentrum av objektorientert programmering. Ikke bare for å representere data, som i prosedyreorientert programmering, men også i selve struktureringen av kode.

De fleste moderne programmeringsspråk, for eksempel Java, C# og C++, følger prinsipper fra OOP, så mye av teorien lenger ned vil man kunne dra nytte av ved en senere anledning.

## Definere klasser
En klasse er en blåkopi eller en mal for å lage objekter. Den definerer egenskapene og oppførselen til objektene som skal opprettes. Egenskaper kalles ofte attributter eller variabler, mens oppførselen er definert av funksjoner som kalles metoder.

For eksempel kan vi definere en klasse som heter "Menneske", som inneholder attributter som "navn", "alder", og "by", og metoder som "gå" og "snakke". Slik gjøres det i Python:

```python
class Menneske:
    art = "Homo sapiens"

    def __init__(self, navn, alder, by):
        self.navn = navn
        self.alder = alder
        self.by = by
        
    def gå(self):
        print(self.navn, "går")
    
    def snakk(self):
        print(self.navn, "snakker")
```

Her er det forskjell på attributter som er definert i __init__, såkalte objektattributter, og attributter som er definert i selve klassen, klasseatributter. Objektattributter er egenskaper som hører til hvert nye objekt, mens klasseattributtene er noe som er felles for alle nye objekter av en klasse.

## Instansiere objekter fra klasser
Vi kan så opprette objekter av klassen "Menneske" for å representere konkrete personer i koden vår. Dette kalles for å instansiere et objekt. For å gjøre dette kaller man konstruktøren ____init____ med de nødvendige parameterne:

```python
m1 = Menneske("Vibeke", 54, "Oslo")
m2 = Menneske("Gry", 52, "London")
```
Her har vi instansiert et objekt av klassen Menneske som heter "m1" med navnet "Vibeke", alderen 54 og byen "Oslo" og et annet objekt. Nå kan man hente ut attributtene til objektet ved å bruke punktnotasjon:

```python
print(m1.navn) # output: Vibeke
print(m1.alder) # output: 54
print(m1.art) # output: Homo sapiens

print(m2.navn) # output: Gry
print(m2.alder) # output: 52
print(m2.art) # output: Homo sapiens
```

Her kan man bite seg merke i at attributen __art__ er den samme på begge objektene selv om de ikke er sendt inn i instansieringen av objektene.

Man kan også kalle metodene til objektet for å utføre handlingene de representerer:
```python
m1.gå()  # output: Vibeke går
m1.snakk()  # output: Vibeke snakker
```

## Arv
Arv er en måte å lage nye klasser som baserer seg på andre klasser. Den nye klassen kalles en avledet klasse, mens den eksistertende klassen kalles en baseklasse. Slik kan man lage en klasse som baserer seg på klassen vi definerte i tidligere.

```python
class Ansatt(Menneske):
    pass
```

Her kan man se at et objekt av den avledede klassen kan bruke egenskaper og oppførsel som er definert i baseklassen.
```python
a1 = Ansatt("Vibeke", 54, "Oslo")
a2 = Ansatt("Gry", 52, "London")

print(a1.navn)  # output: Vibeke
a1.gå()  # output: Vibeke går

print(a2.navn)  # output: Gry
a2.snakk()  # output: Gry snakker

```

Det er mulig å bruke den innebygde funksjonen type() for å se hvilken klasse et objekt tilhører. Man kan også bruke isinstance() for å se at et objektet er utledet av en annen klasse.

```python
print(type(m1))  # output: <class '__main__.Menneske'>
print(type(a1))  # output: <class '__main__.Ansatt'>

print(isinstance(m1, Menneske)) # output: True
print(isinstance(m1, Ansatt)) # output: False
print(isinstance(a1, Menneske)) # output: True
print(isinstance(a1, Ansatt)) # output: True
```
Her kan man se at en ansatt er et menneske, men et menneske ikke er en ansatt.

Man kan også legge på egne egenskaper og oppførsel spesifikt for den avledede klassen. For å sette egne egenskaper for klassen, så man lage en egen __init__-funksjon som vi gjorde tidlegere. Når man gjør det overskriver man __init__metoden fra baseklassen, så derfor må man huske å sette å sende inn verdiene som hører til baseklassen inn i __init__-metoden til baseklassen. Det gjør man ved å bruke den innebygde super()-funksjonen. 

```python
class Ansatt(Menneske):
    def __init__(self, navn, alder, by, arbeidsgiver, stilling):
        super().__init__(navn, alder, by)
        self.arbeidsgiver = arbeidsgiver
        self.stilling = stilling

    def ansattpresentasjon(self):
        print(f"{self.navn}% er {self.alder} år og jobber som {self.stilling} hos {self.arbeidsgiver}.")

a3 = Ansatt("Fredrik", 46, "Oslo", "NRK", "Programleder")
a3.ansattpresentasjon() # output: Fredrik er 46 år og jobber som Programleder hos NRK.
```

I ansattpresentasjon-funksjonen bruker man egenskaper som både er definert for Menneske og Ansatt.

## Mutering

## Innkapsling
Innkapsling er en programmeringsteknikk i objektorientert programmering som har som formål å hindre direkte tilgang til tilstanden til et objekt fra objekter av andre klasser. Dette vil man gjøre i hovedsak av to grunner. Den første er å være sikker på at tilstanden til objektet er gyldig og at man da har kontroll på hvilke endringer som blir gjort.

## Internmetoder



