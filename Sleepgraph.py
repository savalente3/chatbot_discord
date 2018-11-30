import pandas as pd
import matplotlib.pyplot as plt

def sleepanalysis():
    sleeptimes = [0]
    sleepask = input("Would you like to just check your sleep times or add?")
    sleepask = sleepask.lower()
    if sleepask == "check":
        sleepgraph(sleeptimes)
    elif sleepask == "add":
        sleepadd = int(input("Alright, how many hours did you sleep?"))
        sleeptimes.append(sleepadd)
        sleepgraph(sleeptimes)


def sleepgraph(sleeptimes):
    
    table = pd.DataFrame(sleeptimes)
    ax = table.plot()
    fig = ax.get_figure()
    fig.savefig('sleepchart.png')


sleepanalysis()