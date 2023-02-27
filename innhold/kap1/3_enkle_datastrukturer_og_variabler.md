Enkle datastrukturer og variabler (Teodor)
=================================
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å bruke enkle datastrukturer som tall, tekst og boolske verdier. I tillegg skal vi se litt på variabler._

Når vi snakker om datastrukturer, snakker vi i grove trekk om mekanismene vi bruker for å organiserer data i et dataprogram. Ofte skiller vi mellom enkle datastrukturer, som typisk er bygget inn i programmeringsspråket, og mer avanserte datastrukturer, hvor programmereren selv bygger datastrukturen basert på egendefinerte klasser, objekter og funksjoner.

I dette avsnittet skal vi se på enkle datastrukturer som tall, strenger (tekst) og boolske verdier (sant og falskt). I tillegg skal vi se på variabler, som lar oss referere til dataverdier med navn.

Tall
----
Tall er fine ting som man kan bruke til å regne med. Her skal vi gå igjennom tall sånn som Python ser de.

Tall skriver man enkelt og greit som tall:
```python
print(33)
```

Man kan gjøre mange ting med tall:
```python
print(1 + 1)
print(5 - 2)
print(2 * 3)
print(3 / 2)
print(3 // 2)
```

- Operasjoner som `+`, `-`, `*`, `%`, `**`, `/` og `//`.
- Typer tall `int`, `float`.

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
