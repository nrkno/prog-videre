Feilhåndtering (Heidi)
==============

**💡 Læringsmål:** _I dette avsnittet lærer du hvordan du kan håndtere feil som oppstår når programmet kjører, og dermed unngå at programmet kræsjer uventet._

## Prøv og feil

I program kan det ganske lett oppstå feilsituasjoner som gjør at programmet kræsjer og avslutter, dette kalles unntak, eller `exception` på engelsk. Kanskje har du alt opplevd det selv i dette kurset. 

Noen ganger kan det være riktig at programmet avslutter seg selv, mens andre ganger vil vi redde inn situasjonen slik at programmet kan forsette selv om det skjedde noe feil eller uventet. En forutsetning for at vi skal kunne klare å redde inn feil når de oppstår er at vi har en formening om hva programmet bør gjøre istedet for det programmet forsøkte å gjøre. Feil som brukere gjør når de interagerer med programmet er en type feil som programmet bør håndtere på en god måte. Vi nå se på et slikt eksempel. 

La oss starte med et lite program som tar inn to tall, `a` og `b`, som input fra brukeren, og printer ut resultatet av `a/b`.

kopier følgende program i en `.py`-fil, og kjør programmet. 

```python
while True: 
    a = float(input("Tall a: "))
    b = float(input("Tall b: "))
    resultat = a/b
    print(f"a/b er {resultat}")
```

Dette er visst en evig dele-maskin. Test ut programmet med ulike input. Hva skjer om du skriver inn bokstaver eller om du angir at b skal være tallet 0?

Forhåpentligvis fikk du programmet til å avslutte uventet fordi det oppsto et unntak. Kanskje ble det skrevet ut noe tekst i terminalen ala dette?

```
ZeroDivisionError: float division by zero
```

```
ValueError: could not convert string to float: 'hallo'
```


 I stedet for at programmet brått avslutter kan vi håndtere feilene og gå videre. Det fins en egen type konstruksjon for dette, der nøkkelordene `try` og `except` brukes. Den vanligste og mest grunnleggende bruksmåten er som følgende:
```python
try:
    # her er koden det kan skje unntak i
except Exception:
    # her kan vi gi beskjed til brukeren om unntaket og eventuelt gjøre det som trengs for at programmet kan fortsette
```
Koden vi vil sikre er inni `try`-blokka, og håndtering av feil skjer i `except`-blokka. Koden man skriver i `except`-blokka vil bare bli kjørt om det faktisk skjer et unntak.

La oss starte med det enkleste vi kan gjøre for redde programmet vårt fra å kræsje. Da setter vi all kode som kan kræsje inni en `try`-blokk, og skriver ut en feilmelding til brukeren i `except`-blokka: 

```python
while True: 
    try:
        a = float(input("Tall a: "))
        b = float(input("Tall b: "))
        resultat = a/b
        print(f"a/b er {resultat}")
    except Exception:
        print("Det skjedde noe feil, prøv igjen!")
```

Test ut denne endringen i programmet. Hva skjer nå om man deler på 0 eller skriver inn noe som ikke er tall?

Hva som er riktig å gjøre når det oppstår unntak vil avhenge av hva programmet gjør, og hva slags type feil det gjelder. Program som interagerer med brukere bør prøve å gi brukere hjelpsom informasjon om hva som har skjedd og mulighet for å fortsette programmet. Programmet vårt kræsjer ikke lenger, men vi kan gjøre mer for å hjelpe brukeren med å forstå hva som er feil. I blokka `except Exception` fanges alle slags typer unntak, og vi kan ikke fortelle brukeren noe mer om akkurat hva som gikk galt. Men ut fra det som ble skrevet ut i terminalen da vi testet ut feil tidligere, ser vi at vi har noe som heter `ZeroDivisionError` og `ValueError` som er undertyper av typen `Exception`. I tillegg til fange `Exception` kan vi også fange undertyper, ved å ha flere `except`-linjer.

```python
except ValueError:
    # Håndtere ugyldig input verdi
except ZeroDivisionError:
    # håndtere deling på 0
except Exception:
    print("Det skjedde noe feil, prøv igjen!")
```
Det er viktig å merke seg at rekkefølge på `except`-linjene har betydning, for håndteringen vil stoppe ved den første uttrykket som matcher. Så hvis `except Exception` er først i lista vil alle unntak fanges opp der, fordi de to andre er undertyper av denne.

//todo skrive om faren med å fange alt

✍️ **Oppgave** Erstatt feilhåndteringen i programmet med koden over, og lag passende feilhåndtering for ugyldig verdi og deling på 0. 

## Kaste feil

Unntak oppstår fordi de har blitt "kastet" et sted i kode som kjører, ofte fra biblioteker og kode man ikke selv har skrevet. Men man kan også selv kaste unntak med nøkkelordet `raise`. 

La oss se på et nytt lite program. Kopier følgende linjer i en ny Python-fil og test ut programmet. 

```python
ferdig = False
while not ferdig:
    try:
        fødselsår = input("Hvilket år er du født? >")
        print(f"Du er født i {fødselsår}")
        ferdig = True
    except:
        print("Du har angitt et ugyldig fødselsår, prøv igjen!")
```

Her er det en `try`-`except`-blokk, men foreløpig er det ikke noe som gjør at koden i `except`-blokka kjøres, alle mulige ting man kan skrive godtas som fødselsår. Men det skal vi forbedre. 

Først kan vi starte med å kreve at fødselsår skal være et heltall. Det kan vi fikse ved å forsøke å konvertere fødselsåret til et heltall. Legg inn følgende linje i koden:

```python
fødselsår_tall = int(fødselsår)
```

Kjør programmet og se at det nå vil be deg prøve på nytt om du skriver noe som ikke er et heltall, hvis du derimot skriver et gyldig tall vil programmet avsluttes. Hva er det som skjer i koden når blir bedt om å prøve på nytt?

Vi kan gjøre valideringen enda bedre, for ikke alle heltall er noe kan være et gyldig fødselsår for en person som bruker programmet i dag. Så la oss legge til en litt naiv sjekk på at hvis årstallet er større enn i år eller mindre enn la oss si år 1900 så vil vi også kaste et `ValueError`-unntak. Legg til følgende linjer og sjekk hvordan programmet nå oppfører seg med ulik inndata, store og små tall.

```python
if fødselsår_tall < 1900 or fødselsår_tall > 2023:
    raise ValueError()
```

🤔 _Ser du noen problemer med denne valideringskoden? Er det noe du ville gjort annerledes?_

Det går også an å lage sine helt egne unntakstyper istedet for å bruke de som finnes innebygd i Python, slik som `ValueError`. For å lage et unntak kan du bruke følgende linje. 

```python
class UgyldigÅrError(Exception): pass
```
Her er det nok litt rar og ukjent syntaks som vi skal lære mer om senere i kurset når vi kommer til objektorientering. Men det koden gjør er å  definere en ny type, en klasse som heter `UgyldigÅrError`, som arver av klassen `Exception`. Det betyr at Python vil gjenkjenne den som et unntak, og man får lov til å kaste den med `raise`. 

For å kaste unntaket, lager vi en ny instans av klassen med uttrykket `UgyldigÅrError()`, som vi så kaster med `raise`:

```python
raise UgyldigÅrError()
```

## Endelig

Endelig nærmer vi oss sluttet på dette kapittelet, men først skal vi se på hvordan og hvorfor `try`-`except` kan bygges ut med en `finally`. 

Noen ganger ønsker vi å sikre oss at en kodesnutt blir kjørt, enten koden inni `try`-blokka feilet eller ikke. Typisk eksempler er filer eller databasetilkoblinger som man gjerne vil lukke pent etter seg når man er ferdig med å bruke dem. 

Se på følgende eksempel, her åpner vi en fil, vi forsøker å skrive til den, og etter at vi er ferdig med fila ønsker vi å lukke den.

```python
fil = open("adresser.txt", "r", encoding="utf-8")
text = fil.write("Ole Brumm,,Hundremeterskogen\n")
fil.close()
```

Men om linjene over kjøres, så vi programmet feilet, ser du hva som er galt?  Kjør programmet og se hva som skjer. 

Problemet her er at feilen oppstår i den midterste linja, så linja som sørger for at fila blir lukket vil ikke bli kjørt. Hvordan ville du fikset programmet for å sikre at `fil.close()` blir kjørt enten programmet kjørte uten feil eller om det oppstod feil?

En måte er å legge koden inn i en `try`-`except`, og så lukke fila både i `try`-en og i `except`-delen, så er man helt sikker på at fila blir lukket. Men det er kjedelig å måtte gjenta seg, det kan være lett å glemme å oppdatere det ene stedet, og hva om det skjer en feil som ikke blir fanget i `except`-delen? Selv om programmet kræsjer ønsker vi ikke å ødelegge den eksterne fila vi forsøker å lese. Det er her `finally` kan redde dagen for oss. Man kan nemlig legge til en tredje kodeblokk med kode man vi skal kjøres avhengig av hva som skjer i `try`-blokka. 

```python
try:
    # her er koden det kan skje unntak i
except Exception:
    # her kan vi gi beskjed til brukeren om unntaket og eventuelt gjøre det som trengs for at programmet kan fortsette
finally:
    # her er kode som kjøres uavhengig av hva som skjer i try-blokka, det er typisk kode for å rydde opp ressurser som har blitt brukt 
```

Man må ikke ha en `except`-blokk for å bruke `finally`, i en `try`-`finally` vil koden i `finally` alltid bli kjørt, før programmet eventuelt kræsjer om kode i `try`-delen gir unntak, fordi  unntaket vil bli kastet videre etter at koden i `finally` er kjørt.

✍️ **Oppgave:** _Fiks kodeeksempelet over med en `try`-`finally`, der finally-delen lukker fila. Skriv gjerne ut noe til terminalen så du kan verifisere at koden i `finally` faktisk blir kjørt._

🧠 **Visste du at?** `with`-uttrykket som vi lærte i avsnittene om å lese/skrive til fil egentlig er en slags avansert `try`-`with`-`finally`, den kjører en `finally` som lukker fila for oss. Det betyr at når vi bruker `with` så trenger vi ikke å tenke på å lukke fila, det gjør `with` for oss.

Det er verdt å merke seg at `finally` kan oppføre seg litt uventet, særlig i kombinasjon med `return`, `break` og `continue` i `try`-blokka, koden i `finally` vil nemlig kjøres før `return`, `break` og `continue` i `try`-blokka. En annen ting er at hvis både `try` og `finally` returnerer en verdi, er det `finally` sin return verdi som vinner, og blir returnert. Som vi også så over vil feil som ikke håndteres av `except` kastes videre etter `finally`, men hvis `finally` har en `return` vil ikke det skje.  

## Oppgaver

✍️ **Oppgave:** _Finally_

Noen av de litt rare tilfellene med `finally`kan du teste ut med følgende kodesnutter. Tenk gjennom hva som foregår i koden, og eksperimenter med å kommentere ut kode eller legge til nye kodelinjer. 

```python
def lag_feil():
    try:
        raise Exception("Det skjedde en feil")
    finally:
        print("finally")
        return True # kommenter ut linja og se hva som skjer
    
lag_feil()
```

```python
def hva_returneres():
    try:
        return False
    finally:
        return True

print(f"Resultatet er: {hva_returneres()}")
```

✍️ **Oppgave:** _Feilhåndtering i filbehandling_

Ta utgangspunkt i koden for lese til fil, og lag et program som tar inn filnavn som input fra brukeren, og skriver ut innholdet i fila i terminalen.

Hva skjer hvis brukeren skriver inn et filnavn som ikke finnes? Legg inn feilhåndtering så brukeren får tilbud om å prøve på nytt. 

Klarer du framprovosere feil i koden slik at innholdet i fila du leser går tapt?

## Les mer

[Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
