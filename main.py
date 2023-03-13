from lib import*
from matplotlib import pyplot as plt

def plotCSV(T, VS, boundary=None):
    '''
    Fournir : 
        -les "instants"
        -les tensions des canaux
        -[FACULTATIVEMENT] l'instant initial et final qui délimitent le plot, forme : (t_initial, t_final)
    
    Plot le graphe des tensions en fonction du temps.
    '''
    
    fig = plt.figure()
    ax = fig.subplots()

    plt.title("Oscilloscope", fontsize=16)
    plt.xlabel(r"Time ($\mu s$)", fontsize=14)
    plt.ylabel(r"Channel Voltage ($V$)", fontsize=14)

    if boundary == None:
        boundary = (T[0], T[-1])
    plt.xlim(boundary)

    lines = ('-b', '-r', '-g', '-y')
    for j, channel in enumerate(('A', 'B', 'C', 'D')):
        if any(VS[:, j]):
            userInput = input(f"Que représente le canal {channel} ? ")
            if not userInput: userInput = f"Channel {channel}" 
            
            ax.plot(T, VS[:, j], lines[j], label=userInput)

    plt.legend(loc="lower left")
    
    plt.grid()
    plt.show()
 
plotCSV(*readPicoCSV("test.csv", "FR"))
