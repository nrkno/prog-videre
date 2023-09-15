Ting du kan gjøre med interaktiv Python
=======================================

Ved å starte `python`-programmet uten noe argument bak, får du opp en interaktiv Python-sesjon.
Her kan du skrive den samme Python-koden som du skriver i `.py`-filer, men du får umiddelbar respons på det du skriver.

Når Python-fortolkeren venter på at du skal skrive ei kodelinje, står det `>>>` i starten av ei blank linje.
Når du har skrevet ei linje og trykker `[ENTER]`, vil fortolkeren kjøre linja og skrive resultatet til terminalen.
Med andre ord trenger du ikke bruke `print(...)` for å se hva verdien til ulike variabler eller uttrykk er.

Se [kapittel 1.1 for en introduksjon til interaktiv Python](../kap1/1_kjøre_pythonprogram.md).

Her får du noen tips om andre ting du kan gjøre i en interaktiv Python-sesjon.

## Teste ut ting

Har du fått en idé som du har lyst til å prøve ut?
Med en interaktiv Python-sesjon kan du teste ut ulike ting og få umiddelbar respons på hvordan det virker.
Det kan ofte være nyttig å teste litt ut i en interaktiv Python-sesjon først, før du deretter lager den samme koden i ei Python-fil.


## Interaktiv hjelp

Du kan slå opp dokumentasjon når du er i interaktiv modus!
I det aller første eksemplet i kurset, `print("Hallo, verden")`, kjørte vi en funksjon (kodesnutt) som het `print`.
Hvis du vil vite hva `print` gjør for noe, kan du slå opp dokumentasjonen ved å skrive `help(print)` og trykke `[ENTER]`.

<details>
<summary>Resultatet av <code>help(print)</code></summary>

```
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

</details>

Avhengig av hvor mye dokumentasjon det er, kan du bli tatt til en egen visning.

* På Linux og MacOS får du opp en egen visning der du kan bruke piltastene til å bla.
  Trykk på tasten `Q` for å lukke dokumentasjonen og gå tilbake til interaktiv Python.
* På Windows blir hele dokumentasjonen skrevet til terminalen hvis det er plass, ellers står det `-- More --` i bunnen.
  Så lenge det står `-- More --` i bunnen kan du trykke på `[MELLOMROM]`-tasten for å bla en hel side ned,
  `[ENTER]` for å bla én linje, eller `Q` for å avbryte lesingen og gå tilbake til Python-fortolkeren.

Merk at dette oppslaget bare er ment for utviklere som allerede er kjent med ulike tekniske begreper og Python-syntaksen.
Det er ikke forventa at du forstår hva den prøver å si når du akkurat har begynt å lære Python 🙂


## Morsomheter

Python har noen morsomheter inkludert.
Disse er teknisk sett ikke eksklusive for interaktiv Python, men det er jo et ypperlig sted å prøve dem ut:

* `import this`
* `import antigravity` (merk: `print "Hello, world!"` er gammel syntaks og er erstatta av `print("Hello, world!")` i Python 3)
* For deg som har programmert i Java, JavaScript eller tilsvarende språk som bruker "braces" (`{` og `}`) til å markere starten og slutten på kodeblokker, og ønsker deg dette i stedet for innrykk i Python:

  `from __future__ import braces`

  (`from __future__ import ...` brukes vanligvis til å aktivere frivillig funksjonalitet som kan komme til å bli standard i en seinere Python-versjon)
