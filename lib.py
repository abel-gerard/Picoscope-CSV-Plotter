import csv
import numpy as np

def readPicoCSV(pathToCSV, language="EN"):
    '''
    Fournir le path du csv à ouvrir et la langue du csv ("EN" ou "FR") par défaut à "EN" .
    Retourne les instants et les tensions des deux canaux VA et VB.
    '''
    
    languageToKeywords = {
        "EN": ("Time", "Channel A", "Channel B"),
        "FR": ("Temps", "Canal A", "Canal B")
    }
    
    with open(pathToCSV, "r") as csvFile:
        reader = csv.DictReader(csvFile, delimiter=";")
        read = list(reader)[1:]

    T, VA, VB = np.zeros(len(read)), np.zeros(len(read)), np.zeros(len(read))
    data = np.array([T, VA, VB]).T
    for i, row in enumerate(read):
        for j, key in enumerate(languageToKeywords.get(language, "EN")):
            data[i, j] = float(row.get(key, "0.0").replace(",", ".")) 

    return data[:, 0], data[:, 1], data[:, 2]
