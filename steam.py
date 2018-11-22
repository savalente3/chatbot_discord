import discord
from discord.ext import commands
import asyncio
import logging
import requests
import idToName
from discord import Game
from discord.ext.commands import Bot


BOT_PREFIX = ("?", "!")

client = discord.client and Bot(command_prefix=BOT_PREFIX)



######## Function to check if the bot is working and if we is on discord ########
try:
    @client.event
    async def on_ready():
       print(client.user.name , " in the House!!!")
       await client.change_presence(game=Game(name="with humans"))

    ######## Function on_message to work with the messages of the bot and the ones that is receiving ########

    @client.event
    async def on_message(message):
        ######### To keep track of the messages on the text channel ########
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}.")

        steamKey = "C8E7DA1D73AF27DE1CB79495398C374C"
        personal_ID = "76561198118741950"


        if "steam account" in message.content:
           url_account = " http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + steamKey +  "&steamids=" + personal_ID
           data_account = requests.get(url_account)
           read_account = data_account.json()

           await client.send_message(message.channel(format(read_account,(["response"]["players"]["personaname"]))))

        if "My game list" in message.content:
            url_myGameList = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" +steamKey + "&steamid=" + personal_ID + "&format=json"
            data_myGameList= requests.get(url_myGameList)
            read_myGameList = data_myGameList.json()
            app_id_list = []

            for game in read_myGameList["response"]["games"]:
                #print(game)
                app_id_list.append(game["appid"])

            #await idToName.ip_to_name(message, app_id_list)
            for i in app_id_list:
                #print(i)
                url_name = ("http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key=C8E7DA1D73AF27DE1CB79495398C374C&appid=" + str(i))
                data_name = requests.get(url_name)
                read_name = data_name.json()

                if "gameName" in read_name["game"] and read_name["game"]["gameName"] and "ValveTest" not in read_name["game"]["gameName"]:
                    await client.send_message(message.channel, (format(read_name["game"]["gameName"])))


                else:
                    continue

    @client.command(name="bitcoin")
    async def bitcoin():
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        response = requests.get(url)
        value = response.json()
        await client.say("Bitcoin price is: $" + format(value['bpi']['USD']['rate']))

    @client.command()
    async def love(name1 , name2):
        response= requests.get("https://love-calculator.p.mashape.com/getPercentage?fname=" + name1 + "&sname=" + name2,
        headers={
        "X-Mashape-Key":"GNj7kOOzoJmshl7K9QyRhckoUOcPp1FU6aBjsnZJmun1r5oq4s",
        "Accept":"application/json"
        }
        )
        print (response.json())
        percentage = response.json()


except:

    @client.event
    async def error():
        await client.say("Lost internet connection")




client.run("NTA2NjIyNzQyOTk3NDk5OTA1.DrpTpQ.aMorEgRf0L2l4gECK5YVGGGfFPE")
