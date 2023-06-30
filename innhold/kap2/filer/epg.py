import datetime
  
def varighet_i_minutter(duration):
    """Returnerer varighet i antall hele minutter

    Funksjonen er ikke helt nøyaktig, den bryr seg kun om timer og minutter i den opprinnelige varigheten, og dropper sekundene.
    Eksempel:  varighet_i_minutter("PT2H49M52.12S") returnerer heltallet 169
    """
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

    delta = datetime.timedelta(hours=hours, minutes=minutes)
    return int(delta.total_seconds()/60)

