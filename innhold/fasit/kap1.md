Kapittel 1
==========

<!-- toc -->

### 1.7 Løkker

#### Oppgave 1

```python
navneliste = [
    "Vibeke",
    "Aisha",
    "Carlos",
    "Vibeke",
    "Lise",
    "Fatima",
    "Per",
    "Leyla",
    "Oliver",
    "Vibeke",
    "Henrik",
    "Anna",
]

antall_vibeker = 0
for navn in navneliste:
    if navn == "Vibeke":
        antall_vibeker += 1

print(f"Antall personer som heter Vibeke:", antall_vibeker)
```

#### Oppgave 2

```python
quiz = [
    {"spørsmål": "Hva er hovedstaden i Norge? ", "svar": "Oslo"},
    {"spørsmål": "Hva er hovedstaden i Sverige? ", "svar": "Stockholm"},
    {"spørsmål": "Hva er hovedstaden i Danmark? ", "svar": "København"},
]

antall_korrekte_svar = 0

for spørsmålssett in quiz:
    svar_fra_bruker = input(spørsmålssett["spørsmål"])
    if svar_fra_bruker == spørsmålssett["svar"]:
        antall_korrekte_svar += 1

print(f"Antall korrekte svar: ", antall_korrekte_svar)
```

#### Oppgave 3
```python
for i in range(1947, 2024, 4):
    print(i)
```

#### Oppgave 4
```python
handleliste = []

while True:
    vare = input("Legg til en vare i handlelisten (eller skriv 'AVSLUTT' for å avslutte): ")

    if vare.upper() == 'AVSLUTT':
        break
    else:
        handleliste.append(vare)

print("\nDin handleliste:")
for i, vare in enumerate(handleliste, 1):
    print(f"{i}. {vare}")
print(f"Totalt {len(handleliste)} varer i handlelisten.")
```