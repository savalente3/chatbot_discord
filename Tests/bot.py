import discord 
from discord.ext.commands import Bot
import asyncio 
import logging 
import requests  

BOT_PREFIX = ("/")
client = Bot(command_prefix=BOT_PREFIX)

@client.event 
async def on_ready():     
    print("I'm in boooooyyyyyy")     
    print(client.user.name)  


@client.command(pass_context=True)
async def hi(context):
    blah = 'hi sophia'
    await client.say(blah)

    

client.run("NTA5NTA5MzgxOTkwMjUyNTQ0.DsRo4Q.uoTSlmungMtdVKpBXNidEUK6REg")




