import random
import json
import requests
from discord.ext.commands import Bot
from urllib3 import request

BOT_PREFIX = ("/")
TOKEN = 'NTA2ODQ5MDgyNjgyMjQ1MTIy.DsH7Xw.kIgqiISbnyugNVUmx5SKo4_jpj0'

client = Bot(command_prefix=BOT_PREFIX)
players = {}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


'''picks advice at random to give to the user upon request'''
@client.command(pass_context=True)
async def advice(context):
    possible_responses = [
        'Try to cut out carbs from your diet and start eatign healthy fats, this will help you lose weight.',
        'If your tyring to gain weight dont just eat whatever, make sure it has low sugar.',
        'Remember to always workout atleast 5 times a week, leaving two days for rest.',
        'Bring a friend to the gym if youre having trouble with motivation.',
        'Remember to warm up properly before workouts.',
        'Always read the contents of whatever youre eating, some companies can be very deceiving.']
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


'''answers users questions randomly using yes or no'''

@client.event
async def any_question(message):
    if message.content.endswith("?"):
        z = ["Yes.",
             "No, you imbecile"]
        await client.send_message(message.channel, random.choice(z))

'''spoonacular.com/food-api'''
''' uses api to give client a diet plan for a given amount of time'''
@client.command(pass_context=True)
async def diet(message):
    duration = input("For how long do you want the plan for?")
    not_wanted = input("What foods do you not want?")
    diet_type = input("What type of diet do you want? e.g. vegan, paleo...")
    calories = input("What's your target calorie intake?")
    url =  ('https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/mealplans/generate?diet=' + diet_type + '&exclude=' + not_wanted + '&targetCalories=' + calories + '&timeFrame=' + duration + api_key)
    response = requests.get(url).json()

    await client.say((response) + ", " +  message.author.mention)


#answers natural language questions about nutrition through api

@client.command(pass_context=True)
async def nat(message):
    foodtalk = input(client.send_message(message.channel, "Ok what food what would you like"))
    user_input = {eMW9KxpoKoUmshQSIApQ4c0AxPvRup1mdr73jsnzZuOH9Xy8ecv: foodtalk}
    response = requests.post("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/detect", params = user_input)

    await client.say((response + ", " + message.author.mention))


#enters the channel
@client.command(pass_context=True)
async def join(mate):
    channel = mate.message.auther.voice.voice_channel
    await client.join_voice_channel(channel)

#leaves the channel
@client.command(pass_context=True)
async def leave(rgb):
    server = rgb.message.server
    voice_client = client.voice_client_in(server)
    awair voice_client.disconnect()


#plays music
@client.command(pass_context=True)
async def play(ctx,url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players = [server.id] = player
    player.start()


client.run(TOKEN)
