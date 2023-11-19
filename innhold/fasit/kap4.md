Kapittel 4
==========

<!-- toc -->

### 4.1 Objektorientert programmering i Python
#### Oppgave 1
```python
class Kanal:
    def __init__(self, navn, programmer):
        self.navn = navn
        self.programmer = programmer

    def vis_programmer(self):
        print(f"Programmer på {self.navn}:")
        for program in self.programmer:
            print(program)
```

#### Oppgave 2
```python
nrksuper = Kanal("nrksuper", ["Supernytt", "Minibarna", "Fantus og maskinene"])
nrk2 = Kanal("nrk2", ["Filmavisen", "Med hjartet på rette staden"])
```

#### Oppgave 3
```python
print(type(nrksuper))
print(type(nrk2))
```

#### Oppgave 4
```python
class Kanal:
    def __init__(self, navn, programmer):
        self.__navn = navn
        self.__programmer = programmer

    def legg_til_program(self, program):
        self.__programmer.append(program)

    def vis_programmer(self):
        print(f"Programmer på {self.navn}:")
        for program in self.__programmer:
            print(program)
```

#### Oppgave 5
```python
class Kanal:
    ...
    def __eq__(self, other):
            if not isinstance(other, Kanal):
                return False
            return self.__navn == other.__navn and self.__programmer == other.__programmer

    def __str__(self):
        return f"Kanal: {self.__navn}, Programmer: {', '.join(self.__programmer)}"
```

### 4.2 Dataklasser
#### Oppgave 1

```python
from dataclasses import dataclass

@dataclass
class Kanal:
    navn: str
    programmer: list

    def legg_til_program(self, program):
        self.programmer.append(program)
```

#### Oppgave 2

```python
from dataclasses import dataclass

@dataclass
class Kanal:
    ...
    def __post_init__(self):
        if self.navn == "" or len(self.programmer) == 0:
```