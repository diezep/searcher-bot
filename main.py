#!/usr/bin/python3

import datetime
import os
from urllib import parse

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from dotenv import load_dotenv

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

@bot.command()
async def google(ctx, *, search):
    page_name = 'Google'
    url ='https://www.google.com/search?'
    url_param = 'q'
    
    await ctx.send(f'Searching in {page_name} for: {search}...')
    print_log(page_name, search, ctx.author)

    embed = discord.Embed(
        title=f"{page_name} [Search Bot]",
        description=f'Search for "{search}".',
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue()
    )

    query = parse.urlencode({url_param: search})
    url_query = url + query

    res = requests.get(url_query, headers=headers, allow_redirects=False)
    html_content = res.content
    soup = BeautifulSoup(html_content, 'html.parser')

    results = soup.select("div.g > div.rc")
    if len(results) > 0:
        for result in results:
            link = result.find("a").attrs['href']
            tittle = result.find("h3").text
            description = result.find("span", attrs={"class": "st"}).text
            embed.add_field(name=tittle, value=f"{description} \n{link}", inline=False)

    embed.set_thumbnail(url="https://rotulosmatesanz.com/wp-content/uploads/2017/09/2000px-Google_G_Logo.svg_.png")

    await ctx.send(embed=embed)

# Stardew Valley command and functions.
bot.add_cog(StardewValley(bot, headers))

# Terraria command and functions.
bot.add_cog(Terraria(bot, headers))

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)