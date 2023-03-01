import csv
import numpy as np

def readPicoCSV(pathToCSV, language="EN"):
    '''
    Fournir le path du csv à ouvrir et la langue du csv ("EN" ou "FR") par défaut à "EN" .
    Retourne les instants et les tensions des canaux.
    '''
    
    languageToKeywords = {
        "EN": ("Time", "Channel A", "Channel B", "Channel C", "Channel D"),
        "FR": ("Temps", "Canal A", "Canal B", "Canal C", "Canal D")
    }
    
    with open(pathToCSV, "r") as csvFile:
        reader = csv.DictReader(csvFile, delimiter=";")
        read = list(reader)[1:]

    T, VS = np.zeros((len(read), 1)), np.zeros((len(read), 4))
    data = np.concatenate((T, VS), axis=1)
    for i, row in enumerate(read):
        for j, key in enumerate(languageToKeywords.get(language, "EN")):
            data[i, j] = float(row.get(key, "0.0").replace(",", ".")) 

    return data[:, 0], data[:, 1:]
