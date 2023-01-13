Vi skriver data til en fil (Heidi)
===========================

Å skrive til fil ligner mye på å lese fra fil, men når vi åpner fila må vi bruke riktig modus, enten `w` (_write_) eller `a` (_append_). Forskjellen på dem er at når fila åpnes med `w` vil det eksisterende innholdet i fila slettes, mens `a` beholder innholdet, slik at nye ting som skrives legges til på slutten. Og i stedet for å bruke `read()` for å lese fila, må vil bruke `write()` for å skrive.
```python
with open("adresser.txt", "w", encoding="utf-8") as fil:
    fil.write("NRK, Bjørnstjerne Bjørnsons plass 1, 0340 Oslo\n")
    fil.write("Slottet, Slottsplassen 1, 0010 Oslo\n")
```
Koden over åpner fila `adresser.txt` i skrivemodus og skriver to linjer til fila. For å få tekst på ny linje må man legge inn linjeskrift selv med `\n`. Legg til denne koden i programmet ditt og kjør programmet. Se at det opprettes en fil som heter `adresser.txt` og at denne fila inneholder to linjer, en for hver adresse. 

✍️ **Oppgave:** _Flere adresser_

1. Legg til en eller flere nye linjer med adresser, kjør programmet på nytt og se at adressene blir lagt til i fila.
2. Eksperimentèr med å bytte modus fra `w` til `a` og kjør programmet. Hva skjer?  

✍️ **Oppgave:** _Skrive serietittel til fil_

La oss gå tilbake til oppgaven vi gjorde over da vi leste fra fil; å printe ut alle serietitlene fra `serier.txt`. Men i stedet for å skrive ut serietitlene til terminalen skal du nå lagre de til en ny fil istedet, for eksempel i en fil som heter `titler.txt`, med èn tittel per linje.

Som vanlig er det flere veier til mål. En mulighet er å først lese fra `serier.txt` og istedet for å skrive ut titlene, legge de i en liste. Deretter i en ny `with`-blokk åpne fila du vil skrive til, gå gjennom lista, og for hvert element i lista skrive til fil. Et annet alternativ er å åpne begge filene samtidig, både den som skal leses fra og den som skal leses til, og for hver linje man leser fra seriefila skrive direkte til den andre fila med titler. Det går an å åpne flere filer i samme `with`-blokk ved å ha komma mellom `open`-kallene. Legg merke til navnene på filvariablene som må være ulike, og man må ha kontroll på hvilken fil man leser fra og hvilken man skal skrive til.
```python
with open("series.txt", "r", encoding="utf-8") as seriefil,  open("titler.txt", "w", encoding="utf-8") as tittelfil:
```
