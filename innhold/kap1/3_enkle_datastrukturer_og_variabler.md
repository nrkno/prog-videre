Enkle datastrukturer og variabler
=================================
**💡 Læringsmål:** _I dette kapitlet skal du lære deg å bruke enkle datastrukturer som tall, tekst og boolske verdier. I tillegg skal vi se litt på variabler._

Når vi snakker om datastrukturer, snakker vi i grove trekk om mekanismene vi bruker for å organiserer data i et dataprogram. Ofte skiller vi mellom enkle datastrukturer, som typisk er bygget inn i programmeringsspråket, og mer avanserte datastrukturer, hvor programmereren selv bygger datastrukturen basert på egendefinerte klasser, objekter og funksjoner.

I dette kapitlet skal vi se på enkle datastrukturer som tall, strenger (tekst) og boolske verdier (sant og falskt). I tillegg skal vi se på variabler, som lar oss referere til dataverdier med navn.

_**Tips:** Når du går gjennom dette kapittelet, kan det være lurt å lage en kodefil som heter `datastrukturer.py` i mappen `kurs/`, og bruke denne til å teste ut de forskjellige kodesnuttene du støter på._

Tall
----
Python har [innebygget støtte for å jobbe med tall](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex). De to viktigste typene tall er heltall (integers på engelsk, eller `int` i kode) og flyttall (floating-point numbers på engelsk, eller `float` i kode).

Både heltall og flyttall skriver man rett i koden som tall. Som [desimaltegn](https://no.wikipedia.org/wiki/Desimaltegn) bruker man punktum (`.`).
```python
# Skriver ut heltallet 3 (tre)
print(3)

# Skriver ut flyttallet 4,5 (fire og en halv)
print(4.5)
```

For å skrive negative tall, skriver man et minustegn (`-`) før tallet.
```python
# Skriver ut det negative heltallet -5 (minus fem)
print(-5)

# Skriver ut det negative flyttallet -7,2 (minus syv komma 2)
print(-7.2)
```

### Vi regner med tall
Python har flere innebygde funksjoner for å regne med tall:
* `+` lar oss legge sammen to tall. `1 + 1` blir eksempelvis `2`.
* `-` lar oss trekke et tall fra et annet. `3.4 - 2` blir eksempelvis `1.4`.
* `*` lar oss multiplisere to tall. `4 * 3` blir eksempelvis `12`.
* `/` lar oss dele ett tall på et annet. `2 / 1.5` blir eksempelvis `1.3333333333333333`.

I motsetning til funksjonene vi har blitt kjent med fra før, skriver man de vanligste matematiske funksjonene mellom de to tallene man regner på. Dette er forskjellig fra hvordan man bruker funksjoner ellers i Python, men er noe man har gjort for at matematiske uttrykk skal ligne mer på det man er vant til fra annen matematikk.

Funksjonene over fungerer både med heltall og flyttall, og returnerer heltall eller flyttall, avhengig av om svaret på utregningen er et desimaltall, eller om man brukte et flyttall for å regne ut svaret.

✍️ **Oppgave:** _Kan du skrive litt kode i `datastrukturer.py` som bruker de fire innebygde matematiske funksjonene over?_

### Vanlige og spesielle matematiske funksjoner
Mange matematiske funksjoner finnes både som "vanlige" Python-funksjoner og som "spesielle" funksjoner som man skriver mellom to tall. Et eksempel på dette er `pow(...)`-funksjonen, som regner ut potensen til et tall. Dette kan også gjøres med den "spesielle" funksjonen `**`.

```python
# Regner ut 2 opphøyd i 3. potens med pow-funksjonen
print(pow(2, 3))

# Regner ut 2 opphøyd i 3. potens med **
print(2 ** 3)
```

Noen matematiske funksjoner finnes bare som "vanlige" Python-funksjoner. Et eksempel på dette er `math.sqrt(...)`, som regner ut kvadratroten til et tall.

```python
# Importerer biblioteket math, som inneholder flere matematiske funksjoner
# Import av biblioteker er noe vi ikke skal gå inn på nå, men som forklares i senere kapitler
import math

# Regner ut kvadratroten av 9
print(math.sqrt(9))
```

### Regnerekkefølge
De matematiske funksjonene i Python, evalueres i utgangspunktet i [en bestemt rekkefølge](https://docs.python.org/3/reference/expressions.html#operator-precedence). Dette er grunnen til at `3 + 2 * 6` blir `15` (`2 * 6` blir `12`, og legger man til `3` får man `15`).

For å styre rekkefølgen uttrykk evalueres i, kan man bruke parenteser (`(` og `)`). Da kan man eksempelvis skrive `(3 + 2) * 6`, sånn at tallene `3` og `2` legges sammen først, før man multipliserer med `6`.

Noen ganger kan det være lurt å legge til parenteser, selv om uttrykket evaluerer i den rekkefølgen man ønsker i utgangspunktet. Eksempelvis blir både `3 + 2 * 6` og `3 + (2 * 6)` evaluert til `15`, men i det andre uttrykket kan det være enklere å se at multiplikasjonen evalueres først.

### Oversette mellom heltall og flyttall
Ofte er det ikke viktig om man bruker heltall eller flyttall når man regner, men noen ganger gjør det hele forskjellen. Et eksempel på dette kan være at man skal slå opp noe på en spesifikk plass i en liste, noe vi kommer til senere i kurset.

Hvis man skal oversette et heltall til et flyttall, kan man bruke funksjonen `float(...)`.
```python
# Oversetter heltallet 3 til flyttallet 3.0
print(float(3))
```

Når man skal oversette et flyttall til et heltall, er det flere funksjoner som er vanlige å bruke:
* `int(...)` kutter av alle desimalene, så både `int(1.2)` og `int(1.8)` blir til `1`.
* `round(...)` runder av tallet, så `round(1.2)` blir til `1` og `round(1.8)` blir til `2`. Man kan også sende inn et ekstra tall til `round(...)`, hvis man ønsker å ta vare på et spesielt antall desimaler  `round(1.333333333333333333, 2)` blir til `1.33`.
* `//` er nyttig hvis man skal dele to tall, og bare ønske å få tilbake tallene før komma. Eksempelvis blir `2 // 3` til `0`, og `5 // 3` blir til `1`. Man kan med andre ord tenke på `//` som en funksjon som først deler tallene med `/`, og deretter kutter av desimalene med `int(...)`.

### Enda flere matematiske funksjoner
[Modulus](https://no.wikipedia.org/wiki/Modulus) er noe vi kanskje ikke bruker så mye i det daglige, men som har en tendens til å dukke opp i programmering titt og ofte. Kort fortalt er dette hvor mye som er igjen av et tall, hvis vi forsøker å dele det med et annet. I Python kan vi finne denne med å bruke funksjonen `%`. Eksempelvis blir `5 % 2` til `1`, fordi man kan trekke `2` fra `5` to hele ganger, og så ender man opp med en rest på `1`. `10 % 6` blir til `4`, fordi man kan trekke `6` fra `10` en gang, og da ender man opp med en rest på `4`.

Modulus er nyttig for å f.eks. finne ut om et tall er et partall. Vi vet at partall kan deles på 2, så derfor må et partall sin `% 2` være lik `0`.

En annen funksjon som stadig vekk er nyttig når man programmerer, er `abs(...)`, som finner [absoluttverdien](https://no.wikipedia.org/wiki/Absoluttverdi) til et tall. Absoluttverdien er kort fortalt hvor stort tallet er, hvis vi ser bort ifra om det er positivt eller negativt. Eksempelvis er både `abs(3)` og `abs(-3)` tallet `3`.

Variabler
---------
Når man programmerer, skiller man gjerne mellom variabler og verdier. Verdier er ofte det som representerer data i et program, og er gjerne noe spesifikt, som tallet `3`, eller teksten `"hei alle sammen"`. Når vi lærte om tall i seksjonen over, var alle tallene vi brukte eksempel på verdier.

Variabler lar oss gi verdier et navn. Ved å gi verdier navn, kan vi bedre kommunisere hva en verdi representerer. Med variabler kan vi skrive kode som regner med `antall_epler` og `antall_appelsiner`, i stedet for tall som `3` og `5`. Da slipper vi å huske hva hvert tall representerer.

Variabler gir oss også muligheten til å skrive kode som fungerer for mange forskjellige verdier. Man kan f.eks. lage to variabler, `et_tall` og `et_annet_tall`, som inneholder to tallverdier som en bruker har skrevet inn. Så kan man bruke disse variablene til å printe ut summen av tallene med `print(et_tall + et_annet_tall)`. Denne koden vil da fungere uansett hvilke tall brukeren har skrevet inn.

### Livet til en variabel
Livet til en variabel består av fire faser:
1. Variabelen oppstår når vi gir den et navn.
2. Når variabelen har et navn, kan vi gi den en verdi.
3. Når variabelen har en verdi, kan vi bruke variabelnavnet til å hente verdien i koden vår.
4. Når det ikke lenger er behov for variabelen, kan programmet fjerne den.

#### Variabelen oppstår og får sin første verdi
I Python gjennomgår variabler alltid livets to første faser samtidig. Det betyr at vi alltid må gi variabler en verdi samtidig som vi gir de navn. Dette gjør vi ved å skrive navnet på variabelen vi ønsker å lage, et likhetstegn `=`, etterfulgt av verdien vi vil at variabelen skal ha. Kodelinjen `en_variabel = 3` forteller dermed Python at vi ønsker å opprette en variabel med navnet `en_variabel`, og at vi ønsker at den skal få verdien `3`.
```python
en_variabel = 3
print(en_variabel)
```

_**Hvorfor kan jeg ikke lage en variabel uten en verdi i Python?** Variabler er stort sett bare nyttig når de inneholder en verdi. Derfor krever Python at man gir en variabel en verdi når man lager den. Dette gjør at en del feil er litt mindre vanlige i Python, enn i andre programmeringsspråk hvor man kan lage variabler som ikke inneholder verdier._

Som variabelnavn kan man bruke kombinasjoner av små og store bokstaver, tall og understrek (`_`). Det eneste begrensningen er at eventuelle tall ikke kan være det første tegnet i variabelnavnet. Hvis man har variabelnavn som består av flere ord, bruker man gjerne understrek for å skille hvert ord, f.eks. `et_stort_tall`. Tall brukes gjerne der man har flere variabler med lignende navn, som f.eks. `heltall_1` og `heltall_2`.

✍️ **Oppgave:** _Hvilke variabelnavn er gyldige? Under er det en liste med variabelnavn. Klarer du å finne ut av hvilke variabelnavn som er gyldige i Python? Hvis du er i tvil, kan du skrive litt kode i `datastrukturer.py` som forsøker å lage en variabel med det variabelnavnet du lurer på er gyldig._

Variabelnavn:
- `en_annen_variabel`
- `en-variabel`
- `3_variabler`
- `variabel_3`
- `enVariabel`
- `EnVariabel`
- `en variabel`
- `nå_er_det_nok`

#### Vi bruker variabelen
Når man har laget en variabel, og gitt den en verdi, kan man bruke variabelen akkurat som om den var verdien. Det betyr at hvis man har to variabler som inneholder tall-verdier, så kan man bruke de variablene akkurat som om de var tall.
```python
print(3 + 7)

et_tall = 3
et_annet_tall = 7
print(et_tall + et_annet_tall)
```

Man kan også gi variabler en verdi som er hentet fra andre variabler, eller er resultatet av en funksjon som bruker andre variabler eller verdier.
```python
et_tall = 3
et_annet_tall = 7
summen_av_to_tall = et_tall + et_annet_tall
print(summen_av_to_tall)
```

✍️ **Oppgave:** _Kan du skrive litt kode i `datastrukturer.py` som bruker de matematiske funksjonene vi har lært om, men bruker variabler til å ta vare på de tallene man regner med, og resultatene man får?_

#### Kan variabler endre verdi?
I Python kan man gi en variabel en verdi flere ganger. Det betyr at en variabel kan starte med å inneholde tallet `3`, og senere i koden kan inneholde et annet tall som `7`.

```python
en_variabel = 3
print(en_variabel)

en_variabel = 7
print(en_variabel)
```

En variabel kan også inneholde helt forskjellige typer verdier. Man kan f.eks. starte med å la variabelen inneholde et tall `3`, og så la den inneholde teksten `"hei igjen"`.

```python
en_variabel = 3
print(en_variabel)

en_variabel = "hei igjen"
print(en_variabel)
```

Selv om det kan være nyttig å endre verdien til en variabel, kan det også være veldig forvirrende. Spesielt forvirrende kan det være om man lar variabelen endre seg fra helt to forskjellige typer verdier. Derfor kan det være lurt å ha disse to tommelfingerreglene i bakhodet:
1. Hvis det ikke er en spesiell grunn til å endre verdien på en variabel, bruk heller to eller flere variabler.
2. Hvis man må endre på verdien til en variabel, forsøk å skriv koden sånn at man ikke trenger å endre på hvilken type verdi variabelen inneholder.

_**Tips:** Alle regler er til for å brytes, og reglene over er intet unntak. Det finnes mange tilfeller hvor det kan være nyttig å endre verdien til en variabel, og du kommer til å støte på flere eksempler på kode som gjøre det i dette kurset._

#### Når det ikke lenger er behov for en variabel
Python er et eksempel på et programmeringsspråk hvor man i liten grad trenger å skrive kode som forteller programmet at det ikke lenger er behov for en variabel. Dette klarer Python i stor grad å finne ut selv.

Grunnen til at det er viktig for programmeringsspråk å vite at variabler ikke lenger er i bruk, er fordi det lar programmet rydde opp mens det kjører. Da kan programmet f.eks. slutte å bruke minne til å huske på et stort tall, eller "låse opp" en fil, sånn at andre deler av programmet kan skrive til den.

Når man starter å programmere, er det ikke så viktig å tenke på at ting ryddes opp, men etter hvert som man skriver mer avanserte programmer, som f.eks. skal jobbe med filer som er større enn RAM-minnet til datamaskinen, må man i større grad ta hensyn til sånne ting.

I senere kapitler, kommer du også til å bli kjent med Python-kode hvor man forteller Python hvor lenge det er behov for en variabel. Da bruker man typisk syntaksen `with verdi as variabelnavn:`, som forteller Python at denne variabelen bare skal leve innenfor skopet til den blokken `with`-uttrykket omfavner. Ikke fortvil om dette ikke gir så mye mening nå, vi kommer til å jobbe mer med det senere.

Strenger
--------
Skal man jobbe med tekst, er [strenger](https://docs.python.org/3/library/string.html) en fin datastruktur. Kort forklart er en streng en sekvens av tegn (bokstaver eller andre skrifttegn som punktum og komma).

Den enkleste måten å lage en streng på, er ofte å bruke anførselstegn (`"`) eller apostrof (`'`):

```python
en_streng = "Hallo verden"
print(en_streng)

en_annen_streng = 'Hei igjen'
print(en_annen_streng)
```

### Anførselstegn og apostrof
Når man lager en streng på denne måten, er det viktig at teksten man omslutter med anførselstegn eller apostrof, ikke selv inneholder anførselstegn eller apostrof. Hvis man gjør det, blir Python forvirret og tror at teksten slutter før den egentlig gjør det.

```python
# Dette fungerer ikke
funker_ikke = 'Snurp igjen smella di, du maser jo som et lok'motiv'
funker_heller_ikke = "Fra filmen "Lasse & Geir" av Wam og Vennerød"
```

For å få til dette, kan man passe på at man omslutter tekst som inneholder anførselstegn med apostrof, og vice versa.

```python
# Dette fungerer helt fint
funker_fint = "Snurp igjen smella di, du maser jo som et lok'motiv"
funker_også_fint = 'Fra filmen "Lasse & Geir" av Wam og Vennerød'
```

Hvis det ikke holder å bytte mellom anførselstegn og apostrof, kan man også bruke bakstrek (`\`) for å fortelle Python at et enkelt tegn skal tolkes som en del av strengen.

```python
# Her bruker vi bakstrek (\) som rømningskarakter (escape character)
funker_fint = "Snurp igjen smella di, du maser jo som et lok\'motiv. Fra filmen \"Lasse & Geir\" av Wam og Vennerød"
```

### Strenger med flere linjer tekst
Noen ganger har man lyst på en tekst som inneholder linjeskift. For å få til dette, må man legge inn et eget tegn for linjeskift (`\n`) der man ønsker det i teksten.

```python
flere_linjer = "Hva brast så høyt der?\nNorge av di hand, konge."
print(flere_linjer)
```

Et annet alternativ er å omslutte teksten med tre apostrofer (`'''`). Da kan man skrive inn linjeskift som vanlig i teksten.

```python
flere_linjer = '''Hva brast så høyt der?
Norge av di hand, konge.'''
print(flere_linjer)
```

### Formaterte strenger
Strenger i seg selv er ganske nyttig, men de blir enda nyttigere når vi fyller de med data fra andre variabler. Den mest praktiske måten å gjøre dette på, er å bruke [formaterte strenger](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals).

Formaterte strenger, eller f-strenger som de ofte kalles, skiller seg fra vanlige strenger på to måter:
1. De starter med bokstaven `f` før det første anførselstegnet eller apostrofen.
2. Inne i strengen kan man bruke krøllparenteser (`{` og `}`) for å omslutte variabler eller kode som man vil flette inn verdien av.

```python
et_tall = 3
et_annet_tall = 7
svar = f"Summen av {et_tall} og {et_annet_tall} er {et_tall + et_annet_tall}"
print(svar)
```

✍️ **Oppgave:** _Kan lage en egen formatert streng i `datastrukturer.py` som setter sammen noen variabler og printer de til terminalen?_

Når man fletter inn en verdi eller variabel i en formatert streng, vil Python forsøke å gjøre om verdien man fletter inn til en streng. For enkle datastrukturer som tall, vil man typisk få en passende streng ut av boksen, men for mer avanserte datastrukturer, kan det være man må gjøre konverteringen selv, eller bruke en av [konverteringsfunksjonene](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals) som er bygget inn i f-strenger.

_Formaterte strenger er litt nyere funksjonalitet i Python. Før dette var tilgjengelig, brukte man gjerne funksjonen `+` for å slå sammen strenger og verdier. Dette er typisk litt mer kronglete enn å bruke f-strenger, men kommer du over gammel kode, kan det være du ser denne måten å bygge strenger på._


### Andre nyttige streng-funksjoner
Det finnes veldig [mange nyttige funksjoner](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) som kan brukes til å behandle strenger i Python. Vi rekker ikke å dekke alle her, men lurer du på hvordan man kan gjøre noe spesielt med en streng, er det ofte verdt å ta en titt i dokumentasjonen. Under har vi trukket frem tre funksjoner som er nyttig å vite om.

Noen ganger lurer man på om en streng inneholder en spesiell tekst. For å finne ut av dette, kan man bruke funksjonene `in` og `not in`.

```python
en_streng = "Hallo verden"
print("Hallo" in en_streng) # Skriver ut True
print("Hei" in en_streng) # Skriver ut False
print("Hei" not in en_streng) # Skriver ut True
```

For funksjonene `in` og `not in`, gjør store og små bokstaver en forskjell. Ordet `Hallo` er f.eks. ikke det samme som `hallo`.

```python
en_streng = "Hallo verden"
print("hallo" in en_streng) # Skriver ut False
```

Hvis man ønsker å se bort ifra store og små bokstaver når man sammenligner strenger, kan man bruke funksjonen [casefold](https://docs.python.org/3/library/stdtypes.html#str.casefold). Denne gjør om bokstavene i strengen til små bokstaver, så man kan sammenligne den med andre strenger uten å tenke på om den inneholder store og små bokstaver.

```python
en_streng = "Hallo verden"
print("hallo" in en_streng.casefold()) # Skriver ut True
```

_Verdiene `True` og `False` i koden over, er eksempler på boolske verdier. Dette skal vi lære om i neste seksjon._

Det kan også være nyttig å dele opp en streng i flere biter. For å gjøre dette, kan man bruke funksjonen [split](https://docs.python.org/3/library/stdtypes.html#str.split).

```python
en_streng = "Hallo verden"
print(en_streng.split()) # Skriver ut ['Hallo', 'verden']
```

I grove trekk, deler split opp strengen basert på mellomrom. Dette kan ofte være et greit utgangspunkt hvis man forsøker å dele en tekst opp i flere ord.

Hvis man heller ønsker å dele opp strengen basert på et annet tegn, kan man gjøre dette ved å sende tegnet inn som et argument til split-funksjonen.

```python
en_streng = "Hallo verden"
print(en_streng.split("r")) # Skriver ut ['Hallo ve', 'den']
```

_**Tips:** Strenger er en veldig nyttig og fleksibel datastruktur, men siden den kan brukes til nesten hva som helst, er den også lett å misbruke. Ender du opp med å gjøre mange avanserte operasjoner på strenger, kan det være lurt å tenke på om man heller skulle brukt en annen datatype._

Boolske verdier
---------------
Boolske verdier, er verdier som enten kan være sanne (`True`) eller falske (`False`). De brukes gjerne der man ønsker at et dataprogram skal velge mellom å gjøre to forskjellige ting. Hvordan man får programmer til å velge mellom forskjellige ting, basert på en boolsk verdi, er noe vi skal se på i et senere kapittel. I første omgang skal vi bare se litt på hva boolske verdier er, og hvordan man kan bruke ulike boolske funksjoner til å lage boolske uttrykk, som igjen regner ut nye boolske verdier.

### Sant og falskt
En boolsk verdi kan bare være en av to ting. Enten er den sann (`True`), eller så er den falsk (`False`).

```python
sant = True
falskt = False
print(f"Noen ting er {sant} og noen ting er {falskt}")
```

Dette kan virke ganske begrenset, men som vi skal se senere i kurset, er det overraskende mange ting man kan få til med en verdi som bare kan være `True` eller `False`.

### Ikke
Hvis man ønsker å "snu om" på en boolsk verdi, kan man bruke funksjonen `not`. Denne funksjonen tar inn en boolsk verdi, og gir tilbake det motsatte.

For å forstå hvordan `not` fungerer, kan vi sette opp en [sannhetstabell](https://no.wikipedia.org/wiki/Sannhetstabell). Denne tabellen har forskjellige kolonner som inneholder forskjellige boolske verdier, og boolske uttrykk som bruker de forskjellige verdiene. Hver rad i tabellen viser hva det boolske uttrykket blir, hvis de boolske verdiene er satt til en spesiell kombinasjon av `True` eller `False`.

| `a`     | `not a` |
| ------- | ------- |
| `True`  | `False` |
| `False` | `True`  |

Tabellen over, viser at hvis variabelen `a` er satt til `False`, vil det boolske utrykket `not a` bli verdien `True`.

```python
sant = True
print(f"Noen ting er {sant} og noen ting er {not sant}")
```

### Og
Hvis man ønsker å finne ut av om to variabler er sanne samtidig, kan man bruke funksjonen `and`. Denne funksjonen tar inn to boolske verdier, og gir tilbake `True` hvis begge verdiene den tok inn er `True`.

| `a`     | `b`     | `a and b` |
| ------- | ------- | --------- |
| `True`  | `False` | `False`   |
| `False` | `True`  | `False`   |
| `False` | `False` | `False`   |
| `True`  | `True`  | `True`    |

```python
a = True
b = False
print(f"Kommer jeg til å bli sann eller falsk? {a and b}")
```

### Eller
Hvis man bare er opptatt av å finne ut om en av to variabler er sanne, kan man bruke funksjonen `or`. Denne funksjonen tar inn to boolske verdier, og gir tilbake `True` hvis en, eller begge, verdiene er `True`.

| `a`     | `b`     | `a or b` |
| ------- | ------- | -------- |
| `True`  | `False` | `True`   |
| `False` | `True`  | `True`   |
| `False` | `False` | `False`  |
| `True`  | `True`  | `True`   |

```python
a = True
b = False
print(f"Kommer jeg til å bli sann eller falsk? {a or b}")
```

### Gruppering av boolske uttrykk
Akkurat som det kan være vanskelig å finne ut hvilken del av et matematisk uttrykk som evalueres først, kan det være vanskelig å vite hvilken del av et boolsk uttrykk som evalueres først. For å gjøre dette tydeligere, kan man bruke parenteser (`(` og `)`) for å gruppere utrykket.

✍️ **Oppgave:** _Kan du skrive ned sannhetstabellen for uttrykket `a and (b or c)`? Det kan være en fordel å bruke en egen kolonne for del-uttrykket `b or c`. Kan du skrive litt kode som beregner dette boolske uttrykket?_
