import sys

with open(sys.argv[1]) as fil:
    for linje in fil:
        print(linje, end="")
