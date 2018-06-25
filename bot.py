#Import discord's libraries
import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="$")
token = "PUT YOUR BOT TOKEN HERE"
chatFilter = ["fuck", "bitch", "nigga", "nigger"]

@bot.event
#When the bot is ready to go
async def on_ready():
    print("aSimpleBot v1.0")
    print("Ready and connected")
    #discord.py version
    print("discord.py version: " + discord.__version__)
    #Playing ....
    await bot.change_presence(game=discord.Game(name='aSimpleBot'))

@bot.event
async def on_message(message):
    #Word Filter
    contents = message.content.split(" ")
    for words in contents:
        if word.lower() in contents:
            try:
                await bot.delete_message(message)
                await bot.send_message(message.channel, "Hey, <@%s>! You cannot say that!" % (message.author.id))
            except discord.errors.NotFound:
                return
    #Cookie
    if message.content.lower().startswith("!cookie"):
        await bot.send_message(message.channel, ":cookie:")
    #Say stuff
    if message.content.lower().startswith("!say"):
        args = message.content.split(" ")
        await bot.send_message(message.channel, " ".join(args[1:]))


bot.run(token)
