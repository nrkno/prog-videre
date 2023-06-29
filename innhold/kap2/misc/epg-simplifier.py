import json
import requests
import datetime

# def json_from_file():
#     filnavn = "epg.json"
#     with open(filnavn, "r", encoding="utf-8") as json_file:
#         epg_liste = json.load(json_file)
#     return epg_liste

def json_from_api():
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    day = today.day
    print(f"Fetching api for date {year}-{month}-{day}")
    url = f"https://psapi.nrk.no/epg/nrk1,nrk2,nrk3,nrksuper,p1,p2,p3/?date={year}-{month}-{day}"
    request = requests.get(url)
    return request.json()

epg_liste = json_from_api()

epg_simple_keys = ["id"]

channel_simple_keys = [
    "id", 
    "title", 
    "sourceMedium", 
    "isLive", 
    "hasEpg",
    "isOndemandChannel",
    "isDistrictChannel",
    "hasDistrictChannels",
    "priority"
]

entry_simple_keys = [
    "programId",
    "seriesId",
    "category",
    "legalAge",
    "title",
    "description",
    "duration"
]

forenkla_epg_liste = []

for json_epg in epg_liste:
    epg = {}
    for key in epg_simple_keys:
        epg[key] = json_epg[key]
    
    json_channel = json_epg["channel"]
    channel = {}
    for key in channel_simple_keys:
        channel[key] = json_channel[key]
    epg["channel"] = channel
    
    entries = []
    for json_entry in json_epg["entries"]:
        entry = {}
        if "programId" in json_entry:
            for key in entry_simple_keys:
                entry[key] = json_entry[key]
        entries.append(entry)
        epg["entries"] = entries

    forenkla_epg_liste.append(epg)

with open("epg.json", "w", encoding="utf-8") as out_file:
    json.dump(forenkla_epg_liste, fp=out_file, ensure_ascii=False, indent=4)
    out_file.write("\n")
