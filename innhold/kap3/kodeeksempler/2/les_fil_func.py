def les_fil(filnavn):
    with open(filnavn) as fil:
        for linje in fil:
            print(linje, end="")

les_fil("ksjefer.txt")
