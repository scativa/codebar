# https://stackoverflow.com/questions/11059390/parsing-a-tab-separated-file-in-python

import csv

with open("table.txt") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.
        print(line)

with open("table.txt") as tsv:
    for column in zip(*[line for line in csv.reader(tsv, dialect="excel-tab")]):
        print(line)
