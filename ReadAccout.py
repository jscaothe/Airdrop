import csv


def readAccout():
    with open('accout.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data