Funksjoner (Heidi)
==========
**💡 Læringsmål:** _I dette avsnittet skal du lære å lage funksjoner slik at du kan dele opp koden i mindre biter og kan bruke samme kodebit flere steder._

## Hva er en funksjon?

Funksjoner i programmering ligner mistenkelig på funksjoner man lærte om i matematikken på skolen. Som eksempelet i tabellen under viser, tar matematiske funksjoner inn en verdi og gir en verdi tilbake. 

| `x`     | `f(x) = x - 2` |
| ------- | -------------- |
| `4`     | `4 - 2 = 2`    |
| `2`     | `2 - 2 = 0`    |
| `0`     | `0 - 2 = -2`   |

I programmering brukes funksjoner til å abstrahere vekk detaljer slik at man i lange programmer ikke behøver å forholde seg til alle ting hele tiden. I stedet kan man dele koden opp mindre deler, funksjoner, og man trenger bare å  vite navnet på funksjonen og verdiene den eventuelt trenger som input, på det stedet der man vi bruke funksjonen. Det er litt på samme måte som i en matoppskrift, det er ikke alle detaljer som forklares hele tiden. Om det for eksempel står "kok opp 2 liter vann" i oppskriften er det vanligvis ikke forklart hvordan man koker vann.

Funksjoner gjør også at man ikke trenger å gjenta kodelinjer som skal gjøre (neste) det samme. Det er bedre å ha denne samme funksjonaliteten ett sted i koden. Da er det bare ett sted det er nødvendig å forsikre seg om at funksjonaliteten er kodet riktig, og om man trenger å endre funksjonaliteten senere en gang, er det bare ett sted man trenger å oppdatere.

## Funksjoner i Python

En funksjon i Python ser ut på følgende måte:

```python
def lag_hilsen(navn):
    hilsen = f"Hei {navn}!"
    return hilsen
```
Første linje i funksjonen består av nøkkelordet `def` som angir at her starter definisjonen av funksjonen. Teksten som kommer etterpå er navnet på selve funksjonen, deretter kommer parametrene inni parentesen, før linja avsluttes med `:`. Hvis funksjonen ikke skal ta inn noen verdier er det tomt mellom parentesene `()`, hvis funksjonen har flere parametre er de separert med med komma `(fornavn, etternavn)`. Parametrene brukes som variable inni funksjonen og en parameter vil inneholde verdien som angis når man bruker funksjonen, det som sendes inn som argument til funksjonen.

Selve innholdet i funksjonen kommer på linja etter `:`, og alt som skal være inni funksjonen må ha et innrykk. Til sist i funksjonen returneres verdien man vi ha tilbake fra funksjonen ved å skrive `return` etterfulgt av det man vil returnere. Funksjoner i Python må ikke ha en eksplisitt returverdi, om det ikke er noen linje med `return` til slutt, vil funksjonen implisitt returnere verdien `None`.

Lag en ny Python-fil, f.eks med navn `funksjoner.py`, og kopier funksjonen over inn i fila. Deretter kan du i fila kalle funksjonen og lagre resultatet i en variabel, og så printe resultatet:

```python
hilsen = lag_hilsen("Jens")
print(hilsen)
```

Bytt ut navnet med ditt eget navn, og prøve å kalle funksjonen flere ganger med forskjellige navn. 

Når man skal sende inn argument til en funksjon kan man eksplitt navngi parameteren. Det er spesielt nyttig når man har flere argumenter, så man er sikker på at riktig parameter får riktig verdi. I eksempelet kan man derfor skrive:

```python
hilsen = lag_hilsen(navn = "Jens")
```

I eksempelet er  `navn` parameter og `Jens` argument for funksjonen `lag_hilsen`.

Test å legge til eller endre noe i funksjonen du har i skriptet. Klarer du å endre funksjonen så programmet feiler når du kjører det? Hvorfor feiler det?

✍️ **Oppgave:** _Lag en funksjon som skriver ut hjelp til terminalen_

1. Lag funksjonen `print_hjelp()` som ikke tar inn noe argument og som ikke returnerer noen verdi. Bruk `print()`-funksjonen til å skrive ut en valgfri setning om hjelp til terminal.
2. Kall funksjonen i programmet, og se at hjelpeteksten skrives ut når programmet kjører.
3. Lagre returnverdien fra funksjonen i en variabel, for eksempel `hjelp = print_hjelp()`, og print ut denne variabelen. Hva skrives ut?
4. Prøv å legge inn en eksplisitt `return None` i slutten av programmet, hva skrives ut fra variabelen nå?

✍️ **Oppgave:** _Lag en funksjon som lager bærer fra programkode og type_
 Tv- og radioprogram har en programkode (eller programid) består av fire bokstaver og åtte tall, for eksempel `KMNO10010922`. En type bærer består av to bokstaver, for eksempel `AH`, og et program sin bærer består av programkoden til programmet satt sammen med bærertypen, `KMNO10010922AH`.

1. Lag funksjonen `lag_bærer(programkode, bærertype)`. Denne har to parametere, `programkode` og `bærertype`, og skal returnere en streng der programkode og bærertype er satt sammen.
2. Kall funksjonen i programmet og se at verdien som returneres er som du forventer.

✍️ **Oppgave:** _Lag en funksjon som splitter opp bæreren_

1. Lag funksjonen  `del_opp_bærer(bærer)` som er motsatt av `lag_bærer(programkode, bærertype)`. Den skal ta inn en bærer, og dele denne opp i `programkode` og `bærertype`, og returnere disse to verdiene. Funksjoner kan bare returnere én ting, så en måte å returnere flere ting på er å sette de sammen til et tuppel.
2. Kall funksjonen i programmet og se at verdien som returneres er som du forventer.
3. Prøv å kombinere de to bærer-funksjonene, kall først `lag_bærer` og  bruk resultatet herfra som argument til `del_opp_bærer`, og motsatt, kall `del_opp_bærer` og  bruk resultatet herfra som argument til `lag_bærer`. Hvordan forventer du at disse funksjonene fungerer sammen?

✍️ **Oppgave:** _Rydd opp i programmet_

Rydd opp i programmet slik at man unngår at samme funksjonalitet kodes på ulik måte, og ikke har funksjonalitet duplisert i koden. Bruk minst én av bærer-funksjonene over, du kan også lage nye funksjoner der du synes det passer.

```python
program1_kode = "DVFJ60000121"
program1_bærertype = "AH"
program1_bærer = program1_kode + program1_bærertype

program2_kode = "ODRP20002101"
program2_bærertype = "AB"
program2_bærer = "ODRP20002101AB"

program3_kode = program1_kode
program3_bærer = program3_kode + "AA"

programmer = [
    {
        "kode": program1_kode,
        "bærertype": program1_bærertype,
        "bærer": program1_bærer
    },
     {
        "kode": program2_kode,
        "bærertype": program2_bærertype,
        "bærer": program2_bærer
    },
     {
        "kode": program3_kode,
        "bærertype": program3_bærer[-2:],
        "bærer": program3_bærer
    }
]

print(programmer)
```
