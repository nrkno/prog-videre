
import datetime

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
