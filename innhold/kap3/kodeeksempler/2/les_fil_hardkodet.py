filnavn = "ksjefer.txt"
with open(filnavn) as fil:
    for linje in fil:
        print(linje, end="")
