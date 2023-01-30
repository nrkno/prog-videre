Kommentarer
===========
**💡 Læringsmål:** _I dette avsnittet skal du lære deg å skrive forklaringer som kan ligge sammen med koden._

Korte kommentarer
-----------------
Kommentarer er kode som ikke gjør noe annet enn å være forklarende tekst til den som leser koden. Teksten i kommentarene kjøres ikke som en del av dataprogrammet, men er kodelinjer som Python "hopper over".

For å skrive en kommentar på en linje i et Python-program, starter man linjen med et nummertegn (`#`). Da vil Python forstå at resten av teksten på linjen er en kommentar, og ikke programkode.

```python
# Dette er en kommentar
```

✍️ **Oppgave:** _Kan du skrive en kommentar på hva du prøver å få til med en `print`-linje i `hallo_verden.py`_

Lange kommentarer
-----------------
Når man trenger å skrive lange kommentarer, kan det være nyttig å dele de opp over flere linjer. En måte å få til dette på, er å legge inn nummertegn i starten av alle linjene.

```python
# Når du har mye på hjertet,
# kan det være nyttig
# å dele opp kommentaren over flere linjer.
```

Et annet alternativ er å bruke tre anførselstegn (`"""`) på en linje før og etter kommentaren. Da trenger man ikke å legge til noe i starten av hver linje.

```python
"""
Når du har mye på hjertet,
kan det være nyttig
å dele opp kommentaren over flere linjer.
"""
```

Kommentere ut kode
------------------
I tillegg til å være forklaringer, kan man bruke kommentarer til å fjerne deler av koden mens man utvikler et program. Dette kan være nyttig når man kjapt vil sjekke hva som skjer hvis bare deler av koden kjører. Når man bruker kommentarer på denne måten, sier man gjerne at man "kommenterer ut kode".

```python
# print("Denne koden er kommentert ut")
```

✍️ **Oppgave:** _Kan du kommentere ut en `print`-linje i `hallo_verden.py`, og observere hva som da skjer når du kjører programmet?_
