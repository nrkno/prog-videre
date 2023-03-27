Simple GUI demo (Teodor)
===============

Enkelt prosjekt bare for å verifisere at man fått satt opp simplegui riktig

### Notater til innhold
Her kan det være gøy å få med at man kan bytte tema:
```python
sg.theme('DarkTeal6')
sg.theme_previewer()
```

Det kan også være gøy å få med at man kan lage et kantløst vindu.

Styrer mot et første program litt i retning av:
```python
import PySimpleGUI as sg

INPUT_NAME = "input-name"
BUTTON_SAY_GREETING = "button-say-greeting"
TEXT_GREETING = "text-greeting"

layout = [
    [sg.Text('Hva er navnet ditt?'), sg.InputText(key=INPUT_NAME)],
    [sg.Text(key=TEXT_GREETING)],
    [sg.Button(key=BUTTON_SAY_GREETING, button_text='Si hei til meg!')]
]

window = sg.Window('Hei PySimpleGUI!', layout)
running = True
while running:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        running = False
    elif event == BUTTON_SAY_GREETING:
        name = values[INPUT_NAME]
        greetingText = window[TEXT_GREETING]
        greetingText.update(value=f'Hei {name}!')

window.close()
```
