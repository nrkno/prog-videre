Samlinger
=========
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke datastrukturer som samler flere elementer til et sett med informasjon._

Datastrukturer regnes som noe av det mest grunnleggende innenfor programmering. Man samler data i en spesifikk struktur, derav selve beskrivelsen. 
Mye av styrken kommer av mulighetene man har til å utføre bestemte opreasjoner på den lagrede dataen, på en veldig effektiv måte; _gjør X operasjon på alle elementene i lista_
Det finnes en rekke datastrukturer hvor alle har egne regler, styrker og begrensninger. I denne korte introduksjonen skal vi se på tre datastrukturer som alle er mye brukt i Python.

## Lister

Lister er en samling av elementer i en bestemt rekkefølge. Lister kan inneholde «hva som helst»; strenger, tall, variabler, eller til og med andre datastrukturer.
Det er heller ingen krav om at elementene i lista har en viss tilhørighet til de andre elementene.
Lister i Python er det man på fagspråket kaller muterbare (på engelsk «mutable»). Elementene i lista kan endres og erstattes, fjernes og nye kan bli lagt til.

En liste defineres på følgende måte:

```python
liste = []
```

Elementer man legger i lista skilles med komma:

```python
kanaler = ["nrk1", "nrk2", "nrk3"]
```

Siden lister følger en bestemt rekkefølge kan man hente ut elementer basert på indeks. Lister i Python starter alltid på indeks 0:

```python
print(kanaler[0])
print(kanaler[-1])              # Negativ indeks går «bakover» i lista. -1 vil hente ut det siste elementet
```

For å modifisere en liste kan man sette elementet på en bestemt indeks til å være noe annet:

```python
kanaler[0] = "nrk11"
```

For å legge til elementer i en liste kan man bruke følgende operasjoner:

```python
kanaler.append("nrk super")     # append() legger til et element i lista. Elementet blir lagt til helt sist i lista

kanaler.insert(1, "nrk tv")     # insert() legger til et element på den valgte indeksen.
                                # Alle andre elmenter på indekser over valgte indeks flyttes «ett steg til høyre»
```

For å fjerne elementer fra en lista kan man bruke følgende operasjoner:
```python
kanaler.remove("nrk2")          # remove() fjerner det første elmenetet som matcher den valgte verdien

del kanaler[0]                  # del() fjerner elementet på den valgte indeksen

slettet_kanal = kanaler.pop()   # pop() fjerner det siste elementet i lista og lar deg «ta vare på verdien»
                                # pop(index) fjerner elementet på en bestemt indeks
```


## Tupler

Tupler er også en samling av elementer i en bestemt rekkefølge, men skiller seg fra lister ved å være «immutable». Man kan altså ikke endre elementene, fjerne eller legge til nye.

En tuple definerers slik:

```python
tuple = ()
```

På samme måte som ved lister skilles elementer ved hjelp av komma:

```python
kanaler = ("nrk1", "nrk2", "nrk3")
```

For å hente ut elementer fra en tuppel benytter man indeks:

```python
print(kanaler[0])
```

## Innebygde funksjoner for samlinger
Python har en rekke innebygde funksjoner som kan benyttes for å utføre diverse handlinger på samlinger.

Funksjonen `list()` kan benyttes for å lage en liste av f.eks, en streng. Hvert tegn i strengen blir et element i lista.
```python
kanal = "NRK1"
kanal_ord_liste = list(kanal)
print(kanal_ord_liste)
# ['N', 'R', 'K', '1']
```

Funksjonen `sorted()` benyttes for å sortere en samling bestående av tall
```python
episoder_for_planlegging = [1, 2, 8, 5, 10, 4, 22, 11]
sorterte_episoder = sorted(episoder_for_planlegging)
print(sorterte_episoder)
# [1, 2, 4, 5, 8, 10, 11, 22]
```

Funksjonen `reversed()` benyttes for å reversere en gitt sekvens eller samling
```python
episoder_for_planlegging = [1, 2, 8, 5, 10, 4, 22, 11]
episoder_for_planlegging.reverse()
print(episoder_for_planlegging)
# [11, 22, 4, 10, 5, 8, 2, 1]
```

Funksjonene `min()`, `max()` og `len()` returnerer henholdsvis den minste og største tilfellet i en samling, og lengden av samlingen.
```python
episoder_for_planlegging = [1, 2, 8, 5, 10, 4, 22, 11]
print(min(episoder_for_planlegging))
print(max(episoder_for_planlegging))
print(len(episoder_for_planlegging))
# 1
# 22
# 8
```

## Oppslagstabeller

Oppslagstabeller, eller _dictionaries_ er en datastruktur som baserer seg på nøkler med bestemte verdier, istedet for en indeks. 

En oppslagstabell definerers slik:

```python
dict = {}
```

Oppslagstabeller benytter også komma for å skille mellom elementene, men legg merke til at hvert element består av en nøkkel med en tilhørende verdi som er skilt med kolon:

```python
kanaler = {"nrk1" : "20. august 1960", "nrk2" : "1. september 1996", "nrk3" : "3. september 2007"}
```

Man benytter den bestemte nøkkelen for å hente ut tilhørende verdi:

```python
print(kanaler["nrk1"])          # Dette vil skrive ut verdien '20. august 1960'
```

Men hva skjer dersom man forsøker å hente ut en verdi med en nøkkel som ikke finnes?

```python
print(kanaler["tv2"])
```

Eksemplet over vil føre til en KeyError fordi nøkkelen ikke finnes i oppslagstabellen.
Man kan bruke operasjonen `get()` for å omgå dette problemet:

```python
print(kanaler.get("tv2"))
```

Dette vil da gi deg «verdien» 'None' i stedet for en error. 'None' betyr at det ikke eksisterer noen verdi og er ikke en error i seg selv, men heller bare for å påpeke at (for oppslagstabeller spesifikt) denne nøkkel-verdi kombinasjonen ikke eksisterer.
Dersom man ønsker en spesifikk tilbakemelding og ikke bare 'None' kan man legge til et nytt argument i get() operasjonen:

```python
print(kanaler.get("tv2", "Kanalen du forsøker å hente finnes ikke i oppslagstabellen"))
```

For å legge til et nytt element i oppslagstabellen definerer man en ny nøkkel og gir den en verdi:

```python
kanaler["nrk super"] = "1. desember 2007"
```

For å modifisere et bestemt element benytter man også nøkkelen og gir den en ny verdi:

```python
kanaler["nrk"] = "13. mai 1843" # Historieforfalskning...?
```

For å slette et element benytter man, ja du gjetter riktig, nøkkelen:

```python
del kanaler["nrk3"]
```

⚠️ Samlinger kan inneholder andre samlinger! Man kan altså ha en liste av lister, eller oppslagstabeller som inneholder oppslagstabeller. Dette kalles å «neste» - man får da nestede lister eller nestede oppslagstabeller.

✍️ **Oppgave** Lag en oppslagstabell hvor hver verdi er en annen samling. Du bestemmer selv hva slags nøkler og samlinger du benytter.
F.eks. kan man ta utganspunkt i eksemplene over hvor kanal er nøkkel - kanskje verdiene kan være en liste av tv-programmer som sendes på kanalene?
