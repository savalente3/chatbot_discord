

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='WA')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)



Bot.run ("iYk67T-Bjh0JL7Nw7DWK5z7nQfSKbkbx")
