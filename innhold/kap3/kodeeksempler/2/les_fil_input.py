filnavn = input("Hvilken fil? ")
with open(filnavn) as fil:
    for linje in fil:
        print(linje, end="")
