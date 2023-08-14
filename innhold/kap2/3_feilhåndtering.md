Feilhåndtering (Heidi)
==============

**💡 Læringsmål:** _I dette avsnittet lærer du hvordan du kan håndtere feil som oppstår når programmet kjører, og dermed unngå at programmet kræsjer uventet._

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

✍️ **Oppgave** Erstatt feilhåndteringen i programmet med koden over, og lag passende feilhåndtering for ugyldig verdi og deling på 0. 

🧠 **Visste du?** `with`-uttrykket som vi lærte i avsnittene om å lese/skrive til fil er bare en forkledd `try`-`with`-`finally`.

- Hva gjør vi hvis det ikke finnes en fil?
    - Hva kan gå feil: fila finnes ikke, feil filnavn, feil tillatelser, et annet program holder i filhåndtaket.
- Unntak (exceptions), try/except/finally, raise.
- Situasjoner hvor man returnerer to verdier, men én av indikerer en feil.
    - _Kun hvis det er plass til dette_
- Skrive ut med print(file=sys.stderr)

## Les mer

[Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
