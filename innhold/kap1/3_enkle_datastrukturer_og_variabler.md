Enkle datastrukturer og variabler (Teodor)
=================================
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke enkle datastrukturer som tall, tekst og boolske verdier. I tillegg skal vi se litt på variabler._

Når vi snakker om datastrukturer, snakker vi i grove trekk om mekanismene vi bruker for å organiserer data i et dataprogram. Ofte skiller vi mellom enkle datastrukturer, som typisk er bygget inn i programmeringsspråket, og mer avanserte datastrukturer, hvor programmereren selv bygger datastrukturen basert på egendefinerte klasser, objekter og funksjoner.

I dette avsnittet skal vi se på enkle datastrukturer som tall, strenger (tekst) og boolske verdier (sant og falskt). I tillegg skal vi se på variabler, som lar oss referere til dataverdier med navn.

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

Funksjonene over, fungerer både med heltall og flyttall, og returnerer heltall eller flyttall, avhengig om svaret på utregningen er et desimaltall, eller om man brukte et flyttall for å regne ut svaret.

✍️ **Oppgave:** _Kan du skrive litt kode i `datastrukturer.py` som bruker de fire innebygde matematiske funksjonene over?_

### Vanlige og spesielle matematiske funksjoner
Mange matematiske funksjonene finnes både som "vanlige" Python-funksjoner og som "spesielle" funksjoner som man skriver mellom to tall. Et eksempel på dette er `pow(...)`-funksjonen, som regner ut potensen til et tall. Dette kan også gjøres med den "spesielle" funksjonen `**`.

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

# Regner ut roten av 9
print(math.sqrt(9))
```

### Regnerekkefølge
De matematiske funksjonene i Python, evalueres i utgangspunktet i [en bestemt rekkefølge](https://docs.python.org/3/reference/expressions.html#operator-precedence). Dette er grunnen til at `3 + 2 * 6` blir `15` (`2 * 6` blir `12`, og legger men til `3` får man `15`).

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
* `round(...)` runner av tallet, så `round(1.2)` blir til `1` og `round(1.8)` blir til `2`. Man kan også sende inn et ekstra tall til `round(...)`, hvis man ønsker å ta vare på et spesielt antall desimaler  `round(1.333333333333333333, 2)` blir til `1.33`.
* `//` er nyttig hvis man skal dele to tall, og bare ønske å få tilbake tallene før komma. Eksempelvis blir `2 // 3` til `0`, og `5 // 3` blir til `1`. Man kan med andre ord tenke på `//` som en funksjon som først deler tallene med `/`, og deretter kutter av desimalene med `int(...)`.

### Enda flere matematiske funksjoner
[Modulus](https://no.wikipedia.org/wiki/Modulus) er noe vi kanskje ikke bruker så mye i det daglige, men som har en tendens til å dukke opp i programmering tidt og ofte. Kort fortalt er dette hvor mye som er igjen av et tall, hvis vi forsøker å dele det med et annet. I Python kan vi finne denne med å bruke funksjonen `%`. Eksempelvis blir `5 % 2` til `1`, fordi man kan trekke `2` fra `5` to hele ganger, og så ender man opp med en rest på `1`. `10 % 6` blir til `4`, fordi man kan trekke `6` fra `10` en gang, og da ender man opp med en rest på `4`.

Modulus er nyttig for å f.eks. finne ut om et tall er et partall. Vi vet at partall kan deles på 2, så derfor må er partall sin `% 2` være lik `0`.

En annen funksjon som stadig vekk er nyttig når man programmerer, er `abs(...)`, som finner [absoluttverdien](https://no.wikipedia.org/wiki/Absoluttverdi) til et tall. Absoluttverdien er kort fortalt hvor stort tallet er, hvis vi ser bort ifra om det er positivt eller negativt. Eksempelvis er både `abs(3)` og `abs(-3)` tallet `3`.


Variabler
---------
- Tilegne verdier til en variabel
- Gyldige variabelnavn
  - Inkludert æøå?
- gode variabel navn `sesong_nummer = 4`
    - tips om finne gode variabelnavn ved å se det variabelen skal brukes til
- Bruke en variabel
- `i = 2` `i +=1 `

```python
i = 14
print(i)
i = 45
print(i)
a = 2
b = 3
c = a + b
```

Strenger
--------
- Hvordan lager du de? `"`
- Kunne escape enkelte tegn
- Multiline-strenger `'''`
- Hvordan gjør
- `contains`, `split`, `in`
- Bruke programID som eksempel
- Bruke medvirkende som eksempel
    - Sørge for stor forbokstav osv.
- Vise hvordan man bruker f-strenger
    - _Du kan også bruke `+` for å konkatinere strenger, men f-strenger er anbefalt_
- https://docs.python.org/3/library/string.html

Boolske verdier
---------------
- `True`, `False`, and or not, hvordan parenteser kan påvirke ting

| `a`     | `b`     | `a and b` |
| ------- | ------- | --------- |
| `True`  | `False` | `False`   |
| `False` | `True`  | `False`   |
| `False` | `False` | `False`   |
| `True`  | `True`  | `True`    |

| `a`     | `b`     | `a or b` |
| ------- | ------- | -------- |
| `True`  | `False` | `True`   |
| `False` | `True`  | `True`   |
| `False` | `False` | `False`  |
| `True`  | `True`  | `True`   |

| `a`     | `not a` |
| ------- | ------- |
| `True`  | `False` |
| `False` | `True`  |

- Falske og sanne verdier f.eks. `not 0`
- Kortslutning av boolske uttrykk

```python
a = True
c = a or b
print(c)
```

```python
a = ""
b = "hei igjen"
c = a or b
```
