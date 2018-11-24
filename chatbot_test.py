import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from database_con import db_con


bot = commands.Bot(command_prefix = '*')
salute_list = ['Hello', 'hello', 'hi', 'Hi']
salute = False
name = ""
age = 0
height = 0
weight = 0


@bot.event
async def on_ready():
	print("Have no fear, Chappie is here!")
	print("My user name is " + bot.user.name)
	print("My bot user id is " + bot.user.id)




@bot.event
async def on_message(message):
    if "hello" in message.content:
        await bot.send_message(message.channel, "Hello, my name is GHP. I hope you are willing to share your information with me. What is your name?")
        name  = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, "What is your weight?")
        weight = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, "What is your height?")
        height = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, "How old are you?")
        age = await bot.wait_for_message(author = message.author)
        db_con(name, weight, height, age)

bot.run("NTA2OTgzMDY1NTUwMzIzNzIy.DsEzyg.WzxYWzRFJxxxnuABTNU8Vo8tmLk")