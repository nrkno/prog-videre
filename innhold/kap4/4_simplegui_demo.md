Mer om PySimpleGUI
==================

**💡 Læringsmål:** _I dette avsnittet lærer du mer om hvordan PySimpleGUI fungerer, ved å utvide brukergrensesnittet du laget i forrige seksjon med mer funksjonalitet._
​
## Vi lager en knapp som lukker vinduet
Knapper er en av de vanligste komponentene man bruker når man lager brukergrensesnitt. Man kan bruke knapper for å gi brukeren mulighet til å kjøre forskjellige deler av programmet, som å starte et søk, lagre en fil, eller åpne et bilde.

Den første knappen vi skal lage, skal bare hjelpe oss med å lukke vinduet i brukergrensesnittet vi laget i forrige seksjon.

For å legge til en knapp i brukergrensesnittet, må vi legge den til i layout-listen i starten av programmet, som vist under.

```python
layout = [
    [sg.Text('Hei GUI!')],
    [sg.Button('Lukk')]
]
```

Her bruker vi `sg.Button('Lukk')` for å lage en ny knapp nederst i grensesnittet, med teksten "Lukk".

Hvis du kjører programmet nå skal du få opp et skjermbildet med en knapp du kan trykke på. Når du trykker på knappen skjer det ingenting. Det er fordi vi ikke har skrevet noe kode som gjør noe når man trykker på knappen.

For å lukke vinduet når man trykker på knappen, kan vi se hva verdien av `event`-variabelen er. Når man trykker på knappen, vil denne variabelen få samme verdi som teksten på knappen. Det betyr at vi kan skrive litt kode som setter `running`-variabelen til false, og dermed avslutter programmet.

```python
running = True
while running:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        running = False
    elif event == 'Lukk':
        running = False
```

Prøv å kjøre programmet igjen når du har lagt til denne koden. Klarer du ​å lukke vinduet med knappen nå?
​
## Fargetemaer
Man kan endre hvordan komponentene i PySimpleGUI ser ut ved å endre fargetemaet. Du kan prøve dette ut ved å sette fargetemaet til "DarkTeal6" i starten av programmet.

```python
import PySimpleGUI as sg

sg.theme('DarkTeal6')
```
​
Kjører du programmet nå, skal det se litt annerledes ut enn sist.

Hvis du vil ha oversikt over alle de innebygde fargetemaene i PySimpleGUI, kan du bruke en innebygde forhåndsvisningen. Legg til kodelinjen under i starten av programmet, og se hva som skjer når du starter det.

```python
sg.theme_previewer()
```

I tillegg til å bruke innebygde fargetema, kan du også [endre på et eksisterende tema](https://www.pysimplegui.org/en/latest/cookbook/#recipe-modifying-an-existing-theme), eller [lage ditt eget tema](https://www.pysimplegui.org/en/latest/cookbook/#recipe-adding-your-own-color-theme).

## Printe tekst fra GUI
Når man skal debugge brukergrensesnitt, er de ikke alltid like lett å printe ut tekst. Dette har PySimpleGUI en egen funksjon for!
​
Under er tre eksempler på hvordan man skriver ut debug-tekst i PySimpleGUI. Legg de inn i programmet ditt og se hvs som skjer.

```python
sg.Print('Helt vanlig tekst')
sg.Print('Grønn tekst', text_color='green')
sg.Print('Hvit tekst på rød bakgrunn', text_color='white', background_color='red')
```

✍️ **Oppgave:** _Kan du bruke `sg.Print` til å skrive ut debug-tekst som viser når programmet starter, og når en bruker trykker på Lukk-knappen?_​
​
## Input-felter
På samme måte som det er nyttig å kunne lese inn kommandolinjeargumenter i kommandolineapplikasjoner, kan det være nyttig å lese inn input fra brukeren i applikasjoner med grafiske brukergrensesnitt.

En vanlig måte å få inn input fra brukeren, er ved å bruke et input-felt hvor brukeren kan skrive inn tekst, og i eksempelet under, skal vi oppdatere programmet vårt sånn at det kan lese inn navnet til brukeren, og si hei hvis brukeren trykker på en knapp.

Vi kan starte med å oppdatere `layout`-listen vår som vist under.

```python
layout = [
    [sg.Text('Hva er navnet ditt?'), sg.InputText(key='input-navn')],
    [sg.Text(key='text-svar')],
    [sg.Button(key='knapp-hei', button_text='Si hei til meg!')]
]
```

_Her bruker vi `key`-parameteren til å gi noen av komponentene en nøkkel, som gjør at vi kan slå de opp senere. Dette gjør det lettere å f.eks. lese ut navnet brukeren har skrevet inn._

Hvis vi kjører programmet nå, ser vi at vi har fått et brukergrensesnitt med tekst, et input-felt og en knapp, men igjen er det ingenting som skjer når vi trykker på knappen.

For å få programmet til å si hei til brukeren må vi:
1. Sjekke om brukeren har trykket på knappen, ved å se om `event`-variabelen er satt til `'knapp-hei'`.
2. Hvis dette er tilfelle, må vi først lese ut navnet fra input-feltet. Dette kan vi gjøre direkte fra `values`-variabelen.
3. Vi må så hente tekstfeltet vi skal skrive svaret til fra `window`-variabelen.
4. Til slutt må vi oppdatere tekstfeltet med svaret, ved å bruke `.update(...)` funksjonen til feltet.

Kodeutsnittet under viser hvordan vi kan få til disse fire tingene. Denne koden må skrives inne i den uendelige løkken som kjører mens vinduet er åpent.

```python
    elif event == 'knapp-hei':
        name = values['input-navn']
        greetingText = window['text-svar']
        greetingText.update(value=f'Hei {name}!')
```
​
## Hvor finner jeg mer informasjon om PySimpleGUI?
I denne seksjonen har vi sett litt på noen få komponenter i PySimpleGUI, men når du skal lage dine egne brukergrensesnitt, kan det fort være at du trenger mange flere.
Det betyr at du fort må grave litt rundt i dokumentasjonen til PySimpleGUI på egenhånd.
​
Noen ganger er det lettest å starte med et eksempel som ligner litt på det man ønsker å få til. PySimpleGUI har blant annet en [kokebok med eksempler på hvordan man gjør for skjellige ting](https://www.pysimplegui.org/en/latest/cookbook/), og det finnes en god del
[eksempler i GitHub repoet til prosjektet](https://github.com/PySimpleGUI/PySimpleGUI#educational-resources-).
​
Etter hvert kan det være at man trenger å finne alle detaljer om noen av de komponentene man bruker. Da er det gjerne nyttig å lese om komponenten i [referanse-dokumentasjonen](https://www.pysimplegui.org/en/latest/call%20reference/). Her finner man blant annet alle parametere man kan bruke for hver komponent.
