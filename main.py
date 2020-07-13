#!/usr/bin/python3

import datetime
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from cogs.Google import Google
from cogs.StardewValley import StardewValley
from cogs.Terraria import Terraria

print("-- Initializing variables --")
load_dotenv()

print("-- Initializing UserAgent --")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
headers = {'User-Agent': user_agent}

print("-- Initializing utils functions --")
print_log = lambda pageName, search, author : print(f"Function {pageName} called: \n Search: {search} \n By: {author} \n Timestamp: {datetime.datetime.utcnow()} ")
 

print("-- Initializing bot --")
bot = commands.Bot(command_prefix='_')

@bot.command()
async def ping(ctx):
    print("-- Ping function called --")
    await ctx.send('pong')

@bot.event
async def on_ready():
    game = discord.Game('Buscando la felicidad')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('-- Bot searcher ready --')

# Google command and functions.
bot.add_cog(Google(bot, headers))

# Stardew Valley command and functions.
bot.add_cog(StardewValley(bot, headers))

# Terraria command and functions.
bot.add_cog(Terraria(bot, headers))

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)