import requests
import random
import json
import discord
from discord.ext.commands import Bot

BOT_PREFIX = ("/")
TOKEN = 'NTA2ODQ5MDgyNjgyMjQ1MTIy.DsH7Xw.kIgqiISbnyugNVUmx5SKo4_jpj0'

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


'''Yesterdays calorie counter
 @bot.command()
 async def calorie():
     input:
     await client.send_message(message.channel. 'How many  calories did I eat yesterday?'):
     input'''


# picks advice at random to give to the user upon request
@client.command
async def advice(context):
    possible_responses = [
        'Try to cut out carbs from your diet and start eatign healthy fats, this will help you lose weight.',
        'If your tyring to gain weight dont just eat whatever, make sure it has low sugar.',
        'Remember to always workout atleast 5 times a week, leaving two days for rest.',
        'Bring a friend to the gym if youre having trouble with motivation.',
        'Remember to warm up properly before workouts.',
        'Always read the contents of whatever youre eating, some companies can be very deceiving.']
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


# answers users questions randomly
@client.event
async def any_question(message):
    if message.content.endswith("?"):
        z = ["Yes.",
             "No, you imbecile"]
        await client.send_message(message.channel, random.choice(z))


def __get_meal_plan( duration, not_wanted, diet_type, calories_1):
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/mealplans/generate?diet=" + diet_type + "&exclude=" + not_wanted + "&targetCalories=" + calories_1 + "&timeFrame=" + duration,
                           headers={
                               "X-Mashape-Key": "MW9KxpoKoUmshQSIApQ4c0AxPvRup1mdr73jsnzZuOH9Xy8ecv",
                               "Accept": "application/json"
                           }
                           )
    return response

# uses api to give client a diet plan for a given amount of time
@client.command
async def diet(context):
    duration = input("For how long do you want the plan for?")
    not_wanted = input("What foods do you not want?")
    diet_type = input("What type of diet do you want?")
    calories_1 = input("What's your target calorie intake?")
    await client.say(  __get_meal_plan(duration,not_wanted, diet_type,calories_1))


# answers natural language questions about nutrition through api
@client.command
async def naturallang(message):
    foodtalk = message.content
    response = requests.post("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/food/detect",
                            headers={"X-Mashape-Key": "MW9KxpoKoUmshQSIApQ4c0AxPvRup1mdr73jsnzZuOH9Xy8ecv",
                                     "X-Mashape-Host": "spoonacular-recipe-food-nutrition-v1.p.mashape.com",
                                     "Content-Type": "application/x-www-form-urlencoded"}
#                            params={foodtalk}
                            )
    await client.say(response)



'''
@client.command
async def trivia(message)
response = unirest.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/food/trivia/random",
  headers={
    "X-Mashape-Key": "MW9KxpoKoUmshQSIApQ4c0AxPvRup1mdr73jsnzZuOH9Xy8ecv",
    "X-Mashape-Host": "spoonacular-recipe-food-nutrition-v1.p.mashape.com"
  }
)
'''



#client.run(TOKEN)

print( __get_meal_plan("day", "olives", "vegan", "1500") )
