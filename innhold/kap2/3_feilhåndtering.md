Feilhåndtering (Heidi)
==============

**💡 Læringsmål:** _I dette avsnittet lærer du hvordan du kan håndtere feil som oppstår i programmet og dermed unngå at programmet kræsjer._

I program kan det ganske lett oppstå feilsituasjoner som gjør at programmet kræsjer og avslutter, dette kalles unntak, eller `exception` på engelsk. Kanskje har du alt opplevd det selv i dette kurset. 

Noen ganger kan det være riktig at programmet avslutter seg selv, mens andre ganger vil vi redde inn situasjonen slik at programmet kan forsette selv om det skjedde noe feil eller uventet. En forutsetning for at vi skal kunne klare å redde inn feil når de oppstår er at vi vet hva programmet bør gjøre istedet for det det forsøkte å gjøre.

La oss starte med et lite program som tar inn to tall, `a` og `b`, som input fra brukeren, og printer ut resultatet av `a/b`.

kopier følgende program i en `.py`-fil, og kjør programmet. 

```python
while True: 
    a = float(input("Tall a: "))
    b = float(input("Tall b: "))
    resultat = a/b
    print(f"a/b er {resultat}")

```

Dette er visst en evig dele-maskin. Test ut programmet med ulike input. Hva skjer om du skriver inn bokstaver eller om du setter b til å være tallet 0?

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

La oss starte med det enkleste vi kan gjøre for redde programmet vårt fra å kræsje. Da setter vi all kode som kan kræsje inni en `try`-blokk, og skrive ut en feilmelding til brukeren i `except`-blokka: 

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

Hva som er riktig å gjøre når det oppstår unntak vil avhenge av hva programmet gjør og hva slags type feil det Program som interagerer med brukere bør prøve å gi brukere hjelpsom informasjon om hva som har skjedd og mulighet for å fortsette programmet. Programmet vårt kræsjer ikke lenger, men vi kan gjøre mer for å hjelpe brukeren med å forstå hva som er feil. I blokka `except Exception` fanges nå alle slags typer unntak, og vi kan fortelle brukeren noe mer om akkurat hva som gikk galt. 



- Hva gjør vi hvis det ikke finnes en fil?
    - Hva kan gå feil: fila finnes ikke, feil filnavn, feil tillatelser, et annet program holder i filhåndtaket.
- Unntak (exceptions), try/except/finally, raise.
- Situasjoner hvor man returnerer to verdier, men én av indikerer en feil.
    - _Kun hvis det er plass til dette_
- Skrive ut med print(file=sys.stderr)

_Tips. `with` som vi akkurat har lært om, er egentlig bare en snedig variant av try/except/finally._
