def Account():
    
    name = input("Tell me about yourself, what is your name? ")
    def intro(name):
        print("Well hello " + str(name) + "!")
        intro.str_age = float(input("Tell me " + str(name) + " more about you, how old are you? "))
        while 0>intro.str_age>110:
            print("Pretty sure that is not possible " + str(name) + " haha")
            intro.str_age = float(input("Try giving me your actual age "))      

        print("Ok, I know your age " , name)
    
        intro.str_height = float(input("How about your height in centimeters? "))
        while intro.str_height<0:
            intro.str_height = float(input("Pretty sure that is not possible " + str(name) + ". Try again!")) 
            print("Alright, your height is " , intro.str_height )
    
        intro.str_weight = float(input("Lastly I need your weight, no need to have shame, Im a bot, I won't judge... "))
        while intro.str_weight<0:
            intro.str_weight = float(input("Thats not possible, " + name + ". Try again!"))
    
        print("Alright, I think I have everything I need! Thank you! ")
        
   #Calling function#                 
    intro(name)
    
    
    valuesconclusion = str("Is this right? " + name + str(intro.str_height) + str(intro.str_weight))
    conclusion = input(valuesconclusion)
    if conclusion =="Yes" or conclusion == "yes":
        print("Perfect, that's all I need")
    else:
        finalconclusion = input("Uh oh, we have to start over,is that ok?")
    
    if finalconclusion == "yes" or finalconclusion == "Yes" or finalconclusion == "OK" or finalconclusion == "Ok" or finalconclusion == "ok":
        
        intro(name)
    else:
        print("I didnt love you anyway, you have no friends, good bye.")

Account ()    
