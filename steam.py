import discord
from discord.ext import commands
import asyncio
import logging
import requests

client = discord.Client()

######## Function to check if the bot is working and if we is on discord ########

@client.event
async def on_ready():
   print(client.user.name , " in the House!!!")

######## Function on_message to work with the messages of the bot and the ones that is receiving ########

@client.event
async def on_message():
    ######### To keep track of the messages on the text channel ########
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}.")

    steamKey = "C8E7DA1D73AF27DE1CB79495398C374C"
    personal_ID = 76561198118741950


    if "steam account" in message.content:
       url_account = " http: // api.steampowered.com / ISteamUser / GetPlayerSummaries / v0002 /?key =" + steamKey +  "& steamids =" + personal_ID
       data_account = requests.get(url_account)
       read_account = data_account.json()
       await message.channel.send("City: " + format(read["players"]["personaname"]))

    if "My game list" in message.content:
        url_myGameList = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" , steamKey , "&steamid=" , personal_ID , "&format=json"





client.run("NTA2NjIyNzQyOTk3NDk5OTA1.DrpTpQ.aMorEgRf0L2l4gECK5YVGGGfFPE")
