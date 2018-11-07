from discord.ext import commands
import asyncio
import logging
import requests

client = discord.Client()
client1 = commands.Bot(command_prefix = "weather")
@client.event
async def on_ready():
    print("I'm in boooooyyyyyy")
    print(client.user.name)

@client.event
async  def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}.")

    if "Hi" in message.content:
        await client.send_message(message.channel, 'Hey There!! '
                                                   '\n Do you need something?')


    #if "weather"  in message.content:
        #await client.send_message(message.channel, "From what city?")

    if message.content.startswith('weather'):
        await client.send_message(message.channel, 'From what city?')
        city = await client.wait_for_message(author=message.author)
        url = "https://samples.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f7623f59a0958fabc02554d907333b31"
        data = requests.get(url)
        read = data.json()
        await client.send_message(message.channel,("City: " + format(read["name"])))
        print("Temperature: " + format(read["main"]["temp"]) + "F")
        print("Humidity: " + format(read["main"]["humidity"]))
        print("Pressure: " + format(read["main"]["pressure"]))
        print("Wind Speed: " + format(read["wind"]["speed"]))
        print("Description: " + format(read["weather"][0]["description"]))



client.run("NTA2NjIyNzQyOTk3NDk5OTA1.DrpTpQ.aMorEgRf0L2l4gECK5YVGGGfFPE")
