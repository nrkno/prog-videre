Kapittel 2
==========

<!-- toc -->

### 2.5 Et helt program

```python
import json
import datetime

medier = {
    1: "tv",
    2: "radio"
}


def to_timedelta(duration):
    timepart = duration[2:]
    hour_part = timepart.split("H")
    if len(hour_part) == 2:
        hours = int(hour_part[0])
    else:
        hours = 0
    minutes_part = hour_part[-1].split("M")
    if len(minutes_part) == 2:
        minutes = int(minutes_part[0])
    else:
        minutes = 0

    return datetime.timedelta(hours=hours, minutes=minutes)

filnavn = "epg.json"
with open(filnavn, "r", encoding="utf-8") as jsonFile:
    epg_liste = json.load(jsonFile)
    uthenta_program = []

    for epg in epg_liste:
        kanalnavn = epg["channel"]["title"]
        kanal_id = epg["channel"]["id"]
        medium = medier[epg["channel"]["sourceMedium"]]

        for json_program in epg["entries"]:
            kategori_id = json_program["category"]["id"]
            tittel = json_program["title"]
            varighet = to_timedelta(json_program["duration"])

            program = {
                "kanalnavn": kanalnavn, 
                "kanal_id": kanal_id,
                "medium": medium, 
                "kategori_id": kategori_id, 
                "tittel": tittel, 
                "varighet": varighet
                }
            uthenta_program.append(program)

antall_pr_kategori = {}

for program in uthenta_program:
    kategori = program["kategori_id"]
    if kategori in antall_pr_kategori:
        antall_pr_kategori[kategori] += 1
    else:
        antall_pr_kategori[kategori] = 1

antall_pr_kategori_par = list(antall_pr_kategori.items())
kategorier_med_flest = sorted(antall_pr_kategori_par, key=lambda par: par[1], reverse=True)
for kategori, antall in kategorier_med_flest:
    print(f"{kategori.capitalize()}: {antall}")
```