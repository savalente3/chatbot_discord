import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
# Importing all the functions from files created
from database_con import db_con
from Account import Account
from game import summonerbyname, mastery1, mastery2, matchList, regions_list, region_name, regions_list, summoner_ID, account_ID
menu_options = ["1 - Check LOL stats", "2 - Do Sleep Analysis", "3 - Bla bla bla"]

bot = commands.Bot(command_prefix='#') 

@bot.event
async def on_ready():
    print("Have no fear, GHP is here!")
    print("My bot user name is: " + bot.user.name)
    print("My user id is: " + bot.user.id)

@bot.event
async def on_message(message):
    if "Hello" in message.content:
        await bot.send_message(message.channel, "Hello, my name is GHP. What is your name?")
        user_name_msg = await bot.wait_for_message(author = message.author)
        user_name = user_name_msg.content
        await bot.send_message(message.channel, "Well, " + user_name + ", what can I do for you today? Choose from the options listed bellow: ")
        menu_display = discord.Embed(
            title = "Menu",
            description = "Choose from one of the options by writing the number of the corresponding option"
        )
        for count, option in enumerate(menu_options):
            menu_display.add_field(name = "Option {}".format(count+1), value = option, inline = False ) 
        
        await bot.send_message(message.channel, embed = menu_display)
        option_msg = await bot.wait_for_message(author = message.author)
        menu_option = option_msg.content
        menu_option = int(menu_option)

        if menu_option == 1:
            await bot.send_message(message.channel, "Please give me your summoner name.")
            summoner_name_msg = await bot.wait_for_message(author = message.author)
            summoner_name = summoner_name_msg.content
            print(summoner_name)
            await bot.send_message(message.channel, summoner_name + " can you please, tell me your region?")
            regions_display = discord.Embed(
                title = 'Regions',
                description = 'Choose one of the Regions listed bellow:'
            )
        
            for count,region in enumerate(regions_list):
                regions_display.add_field(name="Region {}".format(count+1), value=region, inline=False)

            await bot.send_message(message.channel, embed = regions_display)

            region = await bot.wait_for_message(author = message.author)

            # verifies if the message has been sent by the user
            # regionname is the variable that will hold the value of region inserted by the user 
            if region:
                if region.content not in regions_list:
                    await bot.send_message(message.channel, "That is not a valid region.")
                    await bot.send_message(message.channel, embed = regions_display)
                    region = await bot.wait_for_message(author = message.author)

                for i in range(len(regions_list)):
                    if region.content == regions_list[i]:
                        region_name = region.content
                        print(region_name)
                        await bot.send_message(message.channel, """Thank you for inserting your region's value""")
                    i += 1
            summonerbyname(summoner_name, region_name)

        elif menu_option == 2:
            print("Option  2")

        elif menu_option == 3:
            print("Option 3")

bot.run("NTA2OTgzMDY1NTUwMzIzNzIy.DsEzyg.WzxYWzRFJxxxnuABTNU8Vo8tmLk")