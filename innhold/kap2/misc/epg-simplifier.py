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
    url = f"https://psapi.nrk.no/tv/epg/nrk1,nrk2,nrk3,nrksuper/?date={year}-{month}-{day}"
    request = requests.get(url)
    return request.json()

epg_liste = json_from_api()

channel_keys = [
    "channelId",
    "title", 
]

entry_keys = [
    "programId",
    "seriesId",
    "category",
    "legalAge",
    "title",
    "description",
    "duration"
]

valid_item_types = [
    "program",
    "episode"
]

duration_key = "iso8601"

simplified_epg = []

for json_channel in epg_liste:
    channel = {}
    for key in channel_keys:
        channel[key] = json_channel[key]
    
    entries = []
    for transmission_group in json_channel["transmissionGroups"]:
        for json_entry in transmission_group["entries"]:
            if json_entry["itemType"] in valid_item_types:
                entry = {}
                for key in entry_keys:
                    value = json_entry.get(key)
                    if(value):
                        if key == "duration":
                            entry[key] = value[duration_key]
                        else:     
                            entry[key] = value
                entries.append(entry)
    channel["entries"] = entries

    simplified_epg.append(channel)

with open("epg.json", "w", encoding="utf-8") as out_file:
    json.dump(simplified_epg, fp=out_file, ensure_ascii=False, indent=4)
    out_file.write("\n")
