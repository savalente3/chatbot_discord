import pandas as pd
import matplotlib.pyplot as plt

def exanalysis():
    extimes = [0]
    exask = input("Would you like to just check your exercise times or add?")
    exask = exask.lower()
    if exask == "check":
        exgraph(extimes)
    elif exask == "add":
        exadd = int(input("Alright, how many hours did you exercise?"))
        extimes.append(exadd)
        exgraph(extimes)


def exgraph(extimes):
    
    table = pd.DataFrame(extimes)
    ax = table.plot()
    fig = ax.get_figure()
    fig.savefig('exchart.png')


exanalysis()