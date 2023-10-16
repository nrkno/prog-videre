# Objektorientert programmering i Python
**💡 Læringsmål:** _I dette kapittelet skal du lære om objektorientert programmering og hvordan du kan skrive dine egne klasser for å binde sammen egenskaper og oppførsel i objekter_

Python er et **objektorientert språk(OOP)**, som betyr at et program er strukturert slik at egenskaper og oppførsel er representert i objekter. Et objekt kan for eksempel representere et menneske med egenskaper som navn, alder eller by og oppførsel som for eksempel å gå, snakke eller puste. Eller det kan representere en handlekurv med egenskaper som beskriver hvilke varer som er i handlekurven og oppførsel for å legge til eller fjerne varer. Også typer som du har lært om tidligere, som for eksempel strenger, tall og lister, er representert som objekter i Python.

Sagt på en annen måte så kan man si at objektorientert programmering er en måte å modellere virkeligheten på. Både ved å definere egenskapene og oppførselen til forskjellige ting, men også relasjonen mellom dem.

En annen måte å gjøre det på kan være **prosedyreorientert programmering** der man strukturer et program som en slags oppskrift med forskjellige steg. Stegene kan være bygd opp av funksjoner og kode som utføres etter hverandre for å utføre en oppgave. Hovedforskjellen er at objektene er i sentrum av objektorientert programmering. Ikke bare for å representere data, som i prosedyreorientert programmering, men også i selve struktureringen av kode.

De fleste moderne programmeringsspråk, for eksempel Java, C# og C++, følger prinsipper fra OOP, så mye av teorien lenger ned vil man kunne dra nytte av hvis man hopper videre til andre programmeringsspråk på et senere tidspunkt.

_**Tips:** Når du går gjennom dette kapittelet, kan det være lurt å lage en kodefil som heter `dataklasser.py` i mappen `kurs/`, og bruke denne til å teste ut de forskjellige kodesnuttene du støter på._

## Definere klasser
En klasse er en blåkopi eller en mal for å lage objekter. Den definerer egenskapene og oppførselen til objektene som skal opprettes. Egenskaper kalles ofte attributter eller variabler, mens oppførselen er definert av funksjoner som kalles metoder.

For eksempel kan vi definere en klasse som heter "Menneske", som inneholder attributter som "navn", "alder", og "by", og metoder som "gå" og "snakke". Slik gjøres det i Python:

```python
class Menneske:
    art = "Homo sapiens"

    def __init__(self, navn, alder, by):
        self.__navn = navn
        self.__alder = alder
        self.__by = by
        
    def gå(self):
        print(self.navn, "går")
    
    def snakk(self):
        print(self.navn, "snakker")
```

Her er det forskjell på attributter som er definert i `__init__`, såkalte objektattributter, og attributter som er definert i selve klassen, klasseatributter. Objektattributter er egenskaper som hører til hvert nye objekt, mens klasseattributtene er noe som er felles for alle nye objekter av en klasse.

**Oppgave:** _Kan du skrive kode i `datastrukturer.py` som lager en klasse for en tv-kanal(kalt `Kanal`) som inneholder et felt for kanalnavn(kalt `navn`) og en liste over tv-programmer(kalt `programmer`) som vises på kanalen? Lag også en funksjon for å liste ut hvilke programmer som vises på kanalen i valgfritt format._

## Instansiere objekter fra klasser
Vi kan så opprette objekter av klassen "Menneske" for å representere konkrete personer i koden vår. Dette kalles for å instansiere et objekt. For å gjøre dette kaller man konstruktøren `__init__` med de nødvendige parameterne:

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

**Oppgave:** _Lag to instanser av klassen `Kanal` med kanalnavn "nrksuper" og "nrk2" med programmer henholdsvis `["Supernytt", "Minibarna" og "Fantus og maskinene"]` og `["Filmavisen" og "Med hjartet på rette staden"]`._

## Bruk av type()
Det er mulig å bruke den innebygde funksjonen `type()` for å se hvilken klasse et objekt tilhører. Sjekk for eksempel disse objektene:

```python
print(type(m1))  # output: <class '__main__.Menneske'>
print(type(a1))  # output: <class '__main__.Ansatt'>

a = 5.2 # <class 'float'>
b = 'Hello World' # <class 'str'>
c = [1, 2, 3] # <class 'list'>
d = False # <class 'bool'>
e = range(4) # <class 'range'>
f = (1, 2, 3) # <class 'tuple'>
g = complex(1, -1) # <class 'complex'>

for var in [a, b, c, d, e, f, g]:
    print(type(var))
```

**Oppgave:** _Sjekk at kanalene du har instansiert er av klassen `Kanal`_

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

Man kan også bruke `isinstance()` for å se om et objektet er utledet av en annen klasse.

```python
print(type(m1))  # output: <class '__main__.Menneske'>
print(type(a1))  # output: <class '__main__.Ansatt'>

print(isinstance(m1, Menneske)) # output: True
print(isinstance(m1, Ansatt)) # output: False
print(isinstance(a1, Menneske)) # output: True
print(isinstance(a1, Ansatt)) # output: True
```
Her kan man se at en ansatt er et menneske, men et menneske ikke er en ansatt 🤯

Man kan også legge på egne egenskaper og oppførsel spesifikt for den avledede klassen. For å sette egne egenskaper for klassen, må man lage en egen `__init__`-funksjon som vi gjorde tidligere. Når man gjør det overskriver man `__init__`-metoden fra baseklassen, så derfor må man huske å sette inn verdiene som hører til baseklassen inn i `__init__`-metoden til baseklassen. Det gjør man ved å bruke den innebygde `super()`-funksjonen. 

```python
class Ansatt(Menneske):
    def __init__(self, navn, alder, by, arbeidsgiver, stilling):
        super().__init__(navn, alder, by)
        self.arbeidsgiver = arbeidsgiver
        self.stilling = stilling

    def ansattpresentasjon(self):
        print(f"{self.navn} er {self.alder} år og jobber som {self.stilling} hos {self.arbeidsgiver}.")

a3 = Ansatt("Fredrik", 46, "Oslo", "NRK", "Programleder")
a3.ansattpresentasjon() # output: Fredrik er 46 år og jobber som Programleder hos NRK.
```

I `ansattpresentasjon`-funksjonen bruker man egenskaper som både er definert for Menneske og Ansatt.

## Innkapsling
Innkapsling er en programmeringsteknikk i objektorientert programmering som har som formål å hindre direkte tilgang til tilstanden til et objekt fra objekter av andre klasser. Dette vil man gjøre for å være sikker på at tilstanden til objektet er gyldig og at man har kontroll på hvilke endringer som blir gjort.

Uten at feltene er innkapslet, så er det for eksempel veldig lett å endre på instansen `m1`:
```python
m1.går() # output: Vibeke går
m1.navn = 123
m1.går() # output: 123 går
```

For å hindre at man kan gjøre dette, så bruker man private attributter for å definere at de ikke skal kunne brukes på utsiden av objektet. For Menneske-klassen vil det se slik ut:

```python
class Menneske:
    def __init__(self, navn, alder):
        self.__navn = navn
        self.__alder = alder

    def get_navn(self):
        return self.__navn

    def set_navn(self, navn):
        if isinstance(navn, str) and len(navn) > 0:
            self.__navn = navn

    def get_alder(self):
        return self.__alder

    def set_alder(self, alder):
        if isinstance(alder, int) and 0 <= alder <= 150:
            self.__alder = alder
```

Ved å legge til to understreker foran attributtene __navn og __alder, gjør vi dem private, slik at de ikke kan nås direkte fra utsiden av klassen. Vi gir deretter tilgang til dem gjennom getter- og settermetoder, som også gir oss mulighet til å legge til validering. Ved å gjøre dette lager vi et brukergrensesnitt ut til brukere av klassen som vil gjøre det lettere å gjøre endringer internt i klassen på et senere tidspunkt.

Slik vil bruken av Menneske-objektet se ut:
```python
m3 = Menneske("Harald", 86)
m3.set_navn(123)
print(m3.get_navn()) # output: Harald
```

**Oppgave:** _Implementer innkapsling for `Kanal`-klassen. Sørg for at listen over programmer ikke kan endres direkte, men tilby en metode for å legge til et program i listen._

## Internmetoder
Vi har allerede lært om internmetoden `__init__` som brukes for å lage instanser av en klasse. Vi har også flere internmetoder som for eksempel `__eq__` som brukes når man sammenligner objekter. Hvis vi for eksempel sammenligner to instanser som er laget av en klasse som ikke implementerer en egen `__eq__`-funksjon vil man få `False` på om instansene er like siden de refererer til to forskjellige objekter, men i noen tilfeller vil man definere hva som gjør to instanser av en klasse like. 


```python
class Rektangel:
    def __init__(self, høyde, bredde):
        self.høyde = høyde
        self.bredde = bredde

    def __eq__(self, other):
        return (self.høyde == other.bredde) and (self.bredde == other.bredde)

r1 = Rektangel(1,2)
r2 = Rektangel(1,2)
print(r1 == r2) # output: True
```

En `Rektangel`-klasse uten `__eq__` ville gitt `False`.

En annen internmetode som det kan være greit å ha kjennskap til er `__str__`. Den brukes når man for eksempel bruker print() og str(). Hvis du ikke definerer denne metoden for en klasse, vil Python bruke en standard representasjon, som ofte ikke er særlig brukervennlig. Her flytter vi ansattrepresentasjon-koden inn i `__str__` i stedet for å ha det i en egen metode. 

```python
class Ansatt(Menneske):
    ...
    def __str__(self):
        return f"{self.navn} er {self.alder} år og jobber som {self.stilling} hos {self.arbeidsgiver}."


print(m1) # output: <__main__.Menneske object at 0x107e4bd30>
print(a1) # output: Fredrik er 46 år og jobber som Programleder hos NRK.
```

**Oppgave:** _Legg til `__eq__`- og `__str__`-funksjoner for klassen `Kanal`_
