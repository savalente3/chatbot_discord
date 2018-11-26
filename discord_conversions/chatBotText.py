import discord
from discord.ext import commands
import asyncio
import game

menu_options = ["1 - Check LOL stats", "2 - Do Sleep analysis", "3 - test"]
#regions_list = ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'tr1', 'ru']
regions_list = game.regions_list
bot = commands.Bot(command_prefix = '#')

@bot.event
async def on_ready():
    print("The BOT IS READY!")
    print(bot.user.name)
    print(bot.user.id)

@bot.event
async def on_message(message):
    if "hello" in message.content:
        await bot.send_message(message.channel, "Hello, my name is Chappie! What is your name?")
        user_name_msg = await bot.wait_for_message(author = message.author)
        user_name = user_name_msg.content
        await bot.send_message(message.channel, "Well, " + user_name + ", what can I do for you today?")
        menu_display = discord.Embed(
            title = "Menu",
            description = """Choose an option by writing it's corresponding number"""
        )

        
        for count, option in enumerate(menu_options):
            menu_display.add_field(name = "Option{}".format(count+1), value = option, inline =False)
        
        await bot.send_message(message.channel, embed = menu_display)
        option_msg = await bot.wait_for_message(author = message.author)
        menu_option = option_msg.content
        menu_option = int(menu_option)

        if menu_option == 1:
            print("You chose option 1")
            await bot.send_message(message.channel, "Please give me your summoner name.")
            summoner_name_msg = await bot.wait_for_message(author = message.author)
            summoner_name = summoner_name_msg.content
            print(summoner_name)
            await bot.send_message(message.channel, "Can you tell me your region?")
            regions_display = discord.Embed(
                title = "Regions",
                description = "Choose one of the regions listed bellow:"
            )

            for count, region in enumerate(regions_list):
                regions_display.add_field(name= "Region {}".format(count+1), value = region, inline = False)
            
            await bot.send_message(message.channel, embed = regions_display)
            region = await bot.wait_for_message(author = message.author)

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
            
            game.summonerbyname(summoner_name, region_name)
            summoner_ID = game.summonerbyname.summoner_ID
            account_ID = game.summonerbyname.account_ID
            summoner_ID = str(summoner_ID)
            account_ID = str(account_ID)
            await bot.send_message(message.channel, "Here are your LOL stats:")
            await bot.send_message(message.channel, "Your summoner ID is " + summoner_ID)
            await bot.send_message(message.channel, "Your account ID is " + account_ID)
            game.mastery1(summoner_ID, region_name)
            game.mastery2(summoner_ID, region_name)

            print("end of option 1")
            

        elif menu_option == 2:
            print("You have chosen option 2")

        elif menu_option == 3:
            print("You have chosen option 3")


bot.run("NTA2OTgzMDY1NTUwMzIzNzIy.DsEzyg.WzxYWzRFJxxxnuABTNU8Vo8tmLk")