# Import of discord's API
import discord
from discord.ext import commands
import asyncio
# Import of files containing LOL API and database connection code 
import game
import database_con

menu_options = ["1 - Update your data", "2 - Check LOL stats", "3 - Do Sleep analysis", "3 - Check"]
regions_list = game.regions_list
bot = commands.Bot(command_prefix = '#')

@bot.event
async def on_ready():
    print("The BOT IS READY!")
    print(bot.user.name)
    print(bot.user.id)

@bot.event
async def on_message(message):
    user_id = message.author.id
    if "hello" in message.content:
        #here a check is done in the database to see if the user already exists
        database_con.db_search(user_id)
        if database_con.db_search.existing_user == True:
            user_name = str(database_con.db_search.name)
            await bot.send_message(message.channel, "Hello " + user_name + ". What can I do for you today ?")
            menu_display = discord.Embed(
                title = "Menu",
                description = """Choose an option by writing it's corresponding number"""
            )

            for count, option in enumerate(menu_options):
                menu_display.add_field(name ="Option{}".format(count+1), value = option, inline=False)

            await bot.send_message(message.channel, embed = menu_display)
            option_msg = await bot.wait_for_message(author = message.author)
            menu_option = option_msg.content
            menu_option = int(menu_option)

            if menu_option == 1:
                print("You chose to update your data")
                await bot.send_message(message.channel, "What is your new name?")
                user_name_msg = await bot.wait_for_message(author = message.author)
                user_name = user_name_msg.content
                await bot.send_message(message.channel, user_name + ", let's update your information")
                await bot.send_message(message.channel, "How old are you now?")
                user_age_msg = await bot.wait_for_message(author = message.author)
                user_age = user_age_msg.content
                print(user_age)
                await bot.send_message(message.channel, "What is your height in centimeters?")
                user_height_msg = await bot.wait_for_message(author = message.author)
                user_height = user_height_msg.content
                print(user_height)
                await bot.send_message(message.channel, """Lastly I need your weight, no need to have shame, I'm a bot, I won't judge... """)
                user_weight_msg = await bot.wait_for_message(author = message.author)
                user_weight = user_weight_msg.content
                print(user_weight)
                # user's new values are inserted into database
                database_con.db_update(user_id, user_name, user_age, user_height, user_weight)
                await bot.send_message(message.channel, "Your data has been updated")

            if menu_option == 2:
                print("You chose option 2")
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
                game.mastery1(summoner_ID, region_name)
                game.mastery2(summoner_ID, region_name)
                game.matchList(account_ID, region_name)
                mastery2 = game.mastery2.result
                matchList_result = game.matchList.total_games
                await bot.send_message(message.channel, "Here are your LOL stats:")
                await bot.send_message(message.channel, "Your summoner ID is " + summoner_ID)
                await bot.send_message(message.channel, "Your account ID is " + account_ID)
                # here in the future it will print the table from mastery 1 function in image format
                await bot.send_message(message.channel, mastery2)
                # here in the future it will print the table from matchList function in image format
                await bot.send_message(message.channel, matchList_result )
                
                print("end of option 2")
                

            elif menu_option == 3:
                print("You have chosen option 3")

            elif menu_option == 4:
                print("You have chosen option 4")
        

        else:
            await bot.send_message(message.channel, """Hello, my name is Chappie! It seems like it's the first time we meet... What is your name?""")
            user_name_msg = await bot.wait_for_message(author = message.author)
            user_name = user_name_msg.content
            await bot.send_message(message.channel, "Well, " + user_name + """ I am going to need some information, so you can enjoy all of the features. Don't worry my last name is not Zuckerberg, I won't sell your data""")
            await bot.send_message(message.channel, "How old are you?")
            user_age_msg = await bot.wait_for_message(author = message.author)
            user_age = user_age_msg.content
            print(user_age)
            await bot.send_message(message.channel, "What is your height in centimeters?")
            user_height_msg = await bot.wait_for_message(author = message.author)
            user_height = user_height_msg.content
            print(user_height)
            await bot.send_message(message.channel, """Lastly I need your weight, no need to have shame, I'm a bot, I won't judge... """)
            user_weight_msg = await bot.wait_for_message(author = message.author)
            user_weight = user_weight_msg.content
            print(user_weight)
            await bot.send_message(message.channel, "Alright, I think I have everything I need! Thank you!")
            # user's data get's inserted into database
            database_con.db_insert(user_id, user_name, user_age, user_height, user_weight)

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
                print("You chose to update your data")
                await bot.send_message(message.channel, "What is your new name?")
                user_name_msg = await bot.wait_for_message(author = message.author)
                user_name = user_name_msg.content
                await bot.send_message(message.channel, user_name + ", let's update your information")
                await bot.send_message(message.channel, "How old are you now?")
                user_age_msg = await bot.wait_for_message(author = message.author)
                user_age = user_age_msg.content
                print(user_age)
                await bot.send_message(message.channel, "What is your height in centimeters?")
                user_height_msg = await bot.wait_for_message(author = message.author)
                user_height = user_height_msg.content
                print(user_height)
                await bot.send_message(message.channel, """Lastly I need your weight, no need to have shame, I'm a bot, I won't judge... """)
                user_weight_msg = await bot.wait_for_message(author = message.author)
                user_weight = user_weight_msg.content
                print(user_weight)
                database_con.db_update(user_id, user_name, user_age, user_height, user_weight)
                await bot.send_message(message.channel, "Your data has been updated")

            if menu_option == 2:
                print("You chose option 2")
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
                game.mastery1(summoner_ID, region_name)
                game.mastery2(summoner_ID, region_name)
                game.matchList(account_ID, region_name)
                mastery2 = game.mastery2.result
                matchList_result = game.matchList.total_games
                await bot.send_message(message.channel, "Here are your LOL stats:")
                await bot.send_message(message.channel, "Your summoner ID is " + summoner_ID)
                await bot.send_message(message.channel, "Your account ID is " + account_ID)
                #here print the table from mastery 1 function in image format
                await bot.send_message(message.channel, mastery2)
                #here print the table from matchList function in image format
                await bot.send_message(message.channel, matchList_result )
                
                


                print("end of option 2")
                

            elif menu_option == 3:
                print("You have chosen option 3")

            elif menu_option == 4:
                print("You have chosen option 4")


bot.run("NTA2OTgzMDY1NTUwMzIzNzIy.DsEzyg.WzxYWzRFJxxxnuABTNU8Vo8tmLk")