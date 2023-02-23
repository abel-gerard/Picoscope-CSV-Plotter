import csv
import numpy as np

def readPicoCSV(pathToCSV):
    with open(pathToCSV, "r") as csvFile:
        reader = csv.DictReader(csvFile, delimiter=";")
        read = list(reader)[1:]

    T  = np.array([float(row["Time"].replace(",",".")) for row in read])
    VA = np.array([float(row["Channel A"].replace(",",".")) for row in read])
    VB = np.array([float(row.get("Channel B", "0.0").replace(",",".")) for row in read])

    return T, VA, VB
