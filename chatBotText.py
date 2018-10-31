# WHAT YOU CAN IMPORT FROM
#from Account import Account
#from sleepGoals import sleepGoals
#from sleepAnalysis import sleepAnalysis
#from dailyRepor import dailyRepor
#from exercise import exercise
#from exerciseAnalysis import exerciseAnalysis
#from food import food
#from foodAnalysis import foodAnalysis
#from playTime import playTime
#from playTimeAnalysis import playTimeAnalysis



print("Hello!")
print("My name is GHP")
print ("Do you want to go to your Account or the Menu? ")

x = input ()

""" colect data from user and make a Profile (Account) - linked to Account file """

if x == "Account" or x == "account":
    #imports all of the data from account file and collects the user info, creats variables to be used
    from Account import Account




""" the Menu List option """

if x == "Menu" or x == "menu":
    print ("Chose from the Menu: ")
    s = "Sleep"
    p = "PlayTime"
    f = "Food"
    e = "Exercise" 
    d = "DailyRepor"
    print (s.center (50))
    print (p.center (50))
    print (f.center (50))
    print (e.center (50))
    print (d.center (50))
    y = input ()     
    
###### Sleep option: sleepGoals and sleepAnalysis ######
    
    if y == "sleep" or y == "Sleep":
        Goals = input ("Do you want to set a new goal? ")
        
        if Goals == "yes" or Goals == "Yes":
            z = input (" A bedtime Goal or a Wake up Goal? ")
            a = input ()
            
            if a == "bedtime" or a == "BedTime":
                #imports the bedtime goals for the user to personalize
                from sleepGoals import sleepGoals
            
            elif a == "Wake up" or a == "wake up":
                #imports wake up goals for the user to set up
                from sleepGoals import sleepGoals
        else:
            print ("This is your sleep analysis for the past week")
            from sleepAnalysis import sleepAnalysis
    
    
    
###### PlayTime option: hours of playtime, hours of play time by game, recomendations and analysis ######

    if y == "PlayTime" or y == "playtime":
        print (" Do you want to know your playtime for today or your playtime for each game? ")
        a = input ()
        words1 = "today"
        words2 = "each game"
        
        
        if a.count(words1) == True:
            #taken from programming and algorithms module week 4 CountPython.py doc
            #checks if the word "today" is in the input given by the user 
            print ("ok, I will pull the hours you've spent playing today,", name)
            from playtime import playtime
            
        elif a.count(words2) == True:
            #checks if the words "each game" are in the input given by the user 
            print ("ok, I will pull the hours you've spent playing each game ")
            from playtime import playtime
            
        else:
            print ("These is you playtime analysis for the past week")
            from playTimeAnalysis import playTimeAnalysis            

###### Food option: lets teh user add what he is going to eat and check the calories, recomendations for healthier foods and analysis ######
    
    if y == "Food" or y == "food":
        
        print ("Are you going to eat or just want to check your daily calorie consumption? ")
        a = input ()
        words1 = "eat"
        words2 = "calorie"
        
        if a.count (words1) == True:
            #checks if there is the word eat in user input and imports data from food file
            print ("What are you think about eating?")
            a = input ()
            print ("You can eat healthier...")
            from food import food
        
        elif a.count (words2) == True:
            #checks if word calories is in user input and imports data from food file
            print ("These are the calories you have consume today!")
            from food import food
            
        else:
            #imports data analysis from foodAnalysis file
            print("Here is the calory analysis for the week")
            from foodAnalysis import foodAnalysis
            
###### Exercise option: based on the activity and duration of exercise and food, gives an analysis and recomendations for goals created ######        
   
    if y == "exercise" or y == "Exercise":
        
        