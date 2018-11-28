import pandas as pd
import matplotlib.pyplot as plt

def foodanalysis():
    foodintake = [0]
    foodask = input("Would you like to just check your food intakes or add?")
    foodask = sleepask.lower()
    if foodask == "check":
        foodgraph(foodintake)
    elif foodask == "add":
        foodadd = int(input("Alright, how many calories did you ingest"))
        foodintake.append(foodadd)
        foodgraph(foodintake)


def foodgraph(sleeptimes):
    
    table = pd.DataFrame(foodintake)
    ax = table.plot()
    fig = ax.get_figure()
    fig.savefig('foodchart.png')


foodanalysis()