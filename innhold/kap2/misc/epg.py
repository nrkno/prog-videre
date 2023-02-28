# lære json
import json
import enum
import dataclasses
import datetime
import sys


class Medium(enum.Enum):
    TV = 1
    RADIO = 2


@dataclasses.dataclass
class Program:
    kanalnavn: str
    kanalid: str
    medium: Medium
    kategoriid: str
    tittel: str
    varighet: datetime.timedelta


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

filnavn = sys.argv[1]
with open(filnavn, "r", encoding="utf-8") as jsonFile:
    epg_liste = json.load(jsonFile)
    uthenta_program = []

    for epg in epg_liste:
        kanalnavn = epg["channel"]["title"]
        kanalid = epg["channel"]["id"]
        medium = Medium(epg["sourceMedium"])

        for json_program in epg["entries"]:
            kategori = json_program.get("category")

            if kategori is not None:
                kategoriid = json_program["category"]["id"]
            else:
                kategoriid = "Ingen kategori"

            tittel = json_program["title"]
            varighet = to_timedelta(json_program["duration"])

            program = Program(kanalnavn, kanalid, medium, kategoriid, tittel, varighet)
            uthenta_program.append(program)

antall_pr_kategori = {}

for program in uthenta_program:
    kategori = program.kategoriid
    if kategori in antall_pr_kategori:
        antall_pr_kategori[kategori] += 1
    else:
        antall_pr_kategori[kategori] = 1

antall_pr_kategori_par = list(antall_pr_kategori.items())
kategorier_med_flest = sorted(antall_pr_kategori_par, key=lambda par: par[1], reverse=True)
for kategori, antall in kategorier_med_flest:
    print(f"{kategori.capitalize()}: {antall}")
