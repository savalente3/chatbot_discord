#Sleep Analysis Function

def sleepanalysis():

    import pygal

    sleeptimes = []
    sleepask = input("Would you like to add or just check your last graph?")
        if sleepask == "add": 
            sleepadd = int(input("Alright, how many hours did you sleep?"))
            sleeptimes.append(sleepadd)
        elif sleepask == "check":
            exchart(extimes)


    #Sleep Graph
    def sleepchart(sleeptimes):
    
        sleepchart = pygal.Line()
        sleepchart.title = 'Your Sleep Times'
        sleepchart.x_labels = map(str, range(1, 32))
        sleepchart.add('Hours you have slept', extimes)

        return sleepchart.render_to_png("/tmp/sleepchart.png")
    

    sleepchart(sleeptimes)


sleepanalysis()