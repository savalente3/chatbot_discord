import pygal

foodcalories = []
foodask = input("would you like to add or just check your last graph?")
    if foodask == "add": 
        foodadd = int(input("Alright, how many calories did you eat"))
        foodcalories.append(foodcalories)
    elif foodask == "check":
        foodchart(foodcalories)



def foodchart(foodcalories):
    
    foodchart = pygal.Line()
    foodchart.title = 'This is how much you have eaten'
    foodchart.x_labels = map(str, range(1, 32))
    foodchart.add('Calories Ingested', foodcalories)

    return foodchart.render_to_png("/tmp/foodchart.png")
    

foodchart(foodcalories) 