#Defining function Account#

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print("Have no fear, Chappie is here!")
    print("My user name is " + bot.user.name)
    print("My bot user id is " + bot.user.id)

@bot.event
async def on_message(message):
    if "hello" in message.content:
        await bot.send_message(message.channel, "Hello, my name is GHP. Tell me more about yourself, what is your name?")
        name  = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, "How old are you?")
        age = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, "What is your height in centimeters?")
        height = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, """Lastly I need your weight, no need to have shame, I'm a bot, I won't judge... """)
        weight = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, "Alright, I think I have everything I need! Thank you!")

def Account():
    name = str(input("Tell me about yourself, what is your name? "))
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
    
    
    valuesconclusion = "Is this right? " + name + " " + str(intro.str_age) + " " + str(intro.str_height) + " " + str(intro.str_weight)
   
    conclusion = print(valuesconclusion)
    conclusion = input()
    conclusion = conclusion.lower()
    
        
    if conclusion == "yes":
        print("Perfect, that's all I need")
    else:
        finalconclusion = print("Uh oh, we have to start over,is that ok?")
        finalconclusion = input()
        finalconclusion = finalconclusion.lower()
        if finalconclusion == "yes" or finalconclusion == "ok" or finalconclusion == "sure":
            intro(name)
        else:
            print("I didnt love you anyway, you have no friends, good bye.")

Account ()    

