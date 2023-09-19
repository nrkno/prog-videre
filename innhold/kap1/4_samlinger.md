Samlinger
=========
**💡 Læringsmål:** _I dette kapitlet skal du lære deg å bruke datastrukturer som samler flere elementer til et sett med informasjon._

Datastrukturer regnes som noe av det mest grunnleggende innenfor programmering. Man samler data i en spesifikk struktur, derav selve beskrivelsen. 
Mye av styrken kommer av mulighetene man har til å utføre bestemte operasjoner på den lagrede dataen, på en veldig effektiv måte; _gjør X operasjon på alle elementene i lista_
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
kanaler.remove("nrk2")          # remove() fjerner det første elementet som matcher den valgte verdien

del kanaler[0]                  # del() fjerner elementet på den valgte indeksen

slettet_kanal = kanaler.pop()   # pop() fjerner det siste elementet i lista og lar deg «ta vare på verdien»
                                # pop(index) fjerner elementet på en bestemt indeks
```


## Tupler

Tupler er også en samling av elementer i en bestemt rekkefølge, men skiller seg fra lister ved å være «immutable». Man kan altså ikke endre elementene, fjerne eller legge til nye.

En tuple defineres slik:

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

✍️ **Oppgave** _Lister og tupler_

Lag følgende liste og tuppel i en Python-fil:

```python
tv_serier = ["Side om Side", "Nytt på Nytt", "Stjernekamp", "Pørni"]
podcaster = ("Etikketaten", "Kongerekka", "Oppdatert", "Drivkraft")
```

Bruk det du har lært om lister til å:
* Slette _Nytt på nytt_ ved bruke `del` med riktig indeks
* Slette _Stjernekamp_ ved å bruke `remove`
* Legge til en ny serie i først i lista
* Legge til en ny serie til sist i lista

Skriv ut lista underveis så du vet hva lista inneholder mellom hvert steg.

Prøv å slette eller en legge til en podcast i tuppelen med podcaster. Hva skjer? Hvorfor?

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
kanaler["nrk3"] = "13. mai 1843" # Historieforfalskning...?
```

For å slette et element benytter man, ja du gjetter riktig, nøkkelen:

```python
del kanaler["nrk3"]
```

⚠️ Samlinger kan inneholder andre samlinger! Man kan altså ha en liste av lister, eller oppslagstabeller som inneholder oppslagstabeller. Dette kalles å «neste» - man får da nestede lister eller nestede oppslagstabeller.

✍️ **Oppgave** Lag en oppslagstabell der hver verdi er en annen samling. Du bestemmer selv hva slags nøkler og samlinger du benytter.
F.eks. kan man ta utgangspunkt i eksemplene over der kanal er nøkkel - kanskje verdiene kan være en liste av tv-programmer som sendes på kanalene?

## Innebygde funksjoner for samlinger
Python har en rekke innebygde funksjoner som kan benyttes for å utføre diverse handlinger på samlinger. Det er verdt å merke seg at en streng også er en type samling, så de fleste av funksjonene under fungerer også for strenger.

Funksjonen `list()` kan benyttes for å lage en liste av f.eks, en streng. Hvert tegn i strengen blir et element i lista.
```python
kanal = "NRK1"
kanal_ord_liste = list(kanal)
print(kanal_ord_liste)
# ['N', 'R', 'K', '1']
```

Funksjonen `sorted()` benyttes for å sortere en samling, for eksempel en liste av tall eller strenger.
```python
episoder_for_planlegging = [1, 2, 8, 5, 10, 4, 22, 11]
sorterte_episoder = sorted(episoder_for_planlegging)
print(sorterte_episoder)
# [1, 2, 4, 5, 8, 10, 11, 22]
```

Funksjonen `reverse()` benyttes for å reversere en gitt sekvens eller samling
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

✍️ **Oppgave** Samle inn postnumrene til de som sitter rundt deg, og legg de inn i en samling. Bruk `min` og `max` til å finne høyeste og laveste postnummer.

For å vite om et element er inneholdt i en samling kan man bruke `in`, vi skal se at dette nøkkelordet vil være nyttig i flere sammenhenger, blant annet når vi kommer til løkker.

```python
tv_serier = ["Side om Side", "Nytt på Nytt", "Stjernekamp", "Pørni"]
inneholder_pompel_og_pilt= "Pompel og Pilt" in tv_serier
print(inneholder_pompel_og_pilt)
```

✍️ **Oppgave** Bruk `in` til å teste ut om `Pørni` er del av lista `tv_serier`. Hva med `pørni`?

Vi har alt sett at man kan hente ut et bestemt element på en gitt indeks, for eksempel vil `tv_serier[1]` gi `Side om Side`. Python har også veldig nyttig funksjonalitet for å hente ut en del av en samling med det som kalles "slicing" på godt norsk. Prinsippet er at man i stedet for `tv_serier[index]` kan angi flere ting i klammeparentesene, `tv_serier[start:stopp:steg]`. Start er indeksen man vil starte fra, stopp er indeksen man vi slutte ved, merk at selve stopp indeksen ikke er inkludert. Steg lar deg justere om du vil ha hvert element fra start til stopp, annethvert element, hvert tredje element etc. Default-verdien på steg er 1, så steg angis ikke med mindre man skal ha noe annet enn 1. 

La oss se på et eksempel med en streng, det vil fungere tilsvarende for andre samlinger. Unntaket er oppslagstabeller som ikke støtter oppsplitting på denne måten.

```python
nrk_plakat_paragraf_12 = "NRK skal ha som formål å oppfylle demokratiske, sosiale og kulturelle behov i samfunnet."
```

Eksperimenter med linjene under, og se hva som skrives ut om du justerer på indeksene.

```python
print(f"'{nrk_plakat_paragraf_12[16:22]}'") # Henter ut elementer fra og med indeks 16 til, men uten, indeks 22, skriver ut "formål"
print(f"'{nrk_plakat_paragraf_12[:3]}'") # Hvis man vi hente elementer fra starten kan man droppe å skrive 0, [:3] er det samme som [0:3], skriver ut NRK
print(f"'{nrk_plakat_paragraf_12[78:]}'") # Det samme gjelder for slutten, hvis du vil ha med alle elementer på slutten trenger man ikke ha med sluttindeksen. Skriver ut "samfunnet."
print(f"'{nrk_plakat_paragraf_12[-10:]}'") # Det er upraktisk å telle helt til indeks 78. Ved å bruke negativ index i starten får man de x siste elementene, i dette tilfellet de 10 siste bokstavene. "samfunnet." skrives ut
print(f"'{nrk_plakat_paragraf_12[:-10]}'") # Hvis man har negativ indeks i slutten vil man ikke skrive ut de x siste tegnene. Her skrives alt unntatt "samfunnet." ut.
```

✍️ **Oppgave** Ta utgangspunkt i lista `tall`, og bruk slicing til å lage listene `partall` og `oddetall`, som skal inneholde henholdsvis bare partallene og oddetallene fra `tall`.
```python
tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```
