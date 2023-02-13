import dataclasses
import sys
import json

@dataclasses.dataclass
class Category:
    id: str
    displayValue: str
    is_tv_category: bool
    is_radio_category: bool

@dataclasses.dataclass
class Program:
    kanalnavn: str
    kanalid: str
    medium: int
    kategoriid: str
    tittel: str
    varighet: str

filnavn = "epg.json"
forenkla_epg_liste = []

with open(filnavn, "r", encoding="utf-8") as json_file:
    epg_liste = json.load(json_file)

for json_epg in epg_liste:
    epg = {}
    epg["id"] = json_epg["id"]
    json_channel = json_epg["channel"]
    channel = {}
    channel["id"] = json_channel["id"]
    channel["title"] =json_channel["title"]
    channel["sourceMedium"] = json_channel["sourceMedium"]
    channel["isLive"] = json_channel["isLive"]
    channel["hasEpg"] = json_channel["hasEpg"]
    channel["isOndemandChannel"] = json_channel["isOndemandChannel"]
    channel["isDistrictChannel"] = json_channel["isDistrictChannel"]
    channel["hasDistrictChannels"] = json_channel["hasDistrictChannels"]
    channel["priority"] = json_channel["priority"]
    epg["channel"] = channel
    forenkla_epg_liste.append(epg)
    print("Append epg")
    
with open("json-simple.json", "w", encoding="utf-8") as out_file:
    json.dump(forenkla_epg_liste, fp=out_file)



    
