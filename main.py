from lib import*
from matplotlib import pyplot as plt

def plotCSV(T, VA, VB):
    '''
    Fournir les instants dans T, les tensions des deux canaux de VA et VB.
    Plot le graphe des tensions en fonction du temps.
    '''
    
    fig = plt.figure()
    ax = fig.subplots()

    plt.title("Oscilloscope", fontsize=16)
    plt.xlabel(r"Time ($\mu s$)", fontsize=14)
    plt.ylabel(r"Channel Voltage ($V$)", fontsize=14)

    ax.plot(T, VA, '-b', label="Channel A")
    if any(VB): ax.plot(T, VB, '-r', label="Channel B")

    plt.legend(loc="lower left")

    plt.grid()
    plt.show()
 
plotCSV(*readPicoCSV("test1.csv"))
