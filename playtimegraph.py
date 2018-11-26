import pygal

pttimes = []
ptaskask = input("would you like to add or just check your last graph?")
    if ptask == "add": 
        ptadd = int(input("Alright, how many hours did you play"))
        pttimes.append(ptadd)
    elif ptask == "check":
        ptchart(pttimes)



def ptchart(pttimes):
    
    ptchart = pygal.Line()
    ptchart.title = 'Your Playtime!'
    ptchart.x_labels = map(str, range(1, 32))
    ptchart.add('Hours you have played', pttimes)

    return ptchart.render_to_png("/tmp/ptcharta.png")
    

ptchart(pttimes) 