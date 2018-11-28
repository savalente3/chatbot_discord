import pandas as pd
import matplotlib.pyplot as plt

def ptanalysis():
    pttimes = [0]
    ptask = input("Would you like to just check your playtime or add?")
    ptask = ptask.lower()
    if ptask == "check":
        ptgraph(pttimes)
    elif ptask == "add":
        ptadd = int(input("Alright, how many hours did you play?"))
        pttimes.append(ptadd)
        ptgraph(pttimes)


def ptgraph(pttimes):
    
    table = pd.DataFrame(pttimes)
    ax = table.plot()
    fig = ax.get_figure()
    fig.savefig('ptchart.png')


ptanalysis()
