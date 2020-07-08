import os

import discord
from discord.ext import commands
import datetime

from urllib import parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from dotenv import load_dotenv

print("-- Initializing Environment Variables --")
load_dotenv()

print("-- Initializing bot --")
bot = commands.Bot(command_prefix='$')



@bot.command()
async def ping(ctx):
    print("-- Ping function called --")
    await ctx.send('pong\n'*40)

@bot.event
async def on_ready():
    game = discord.Game('Buscando la felicidad')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('My Ready is Body')
    
@bot.command()
async def google(ctx, *, search):
    embed = discord.Embed(
        title="Google Search Bot", 
        description=f'Google search for "{search}".',
        timestamp=datetime.datetime.utcnow(), 
        color=discord.Color.blue()
    )

    query_string = parse.urlencode({'q': search})
    url = 'https://www.google.com/search?' + query_string
    agent_user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    req = Request(url, headers={'User-Agent': agent_user})
    html_content = urlopen(req).read()
    soup = BeautifulSoup(html_content, 'html.parser')

    google_results = soup.select("div.g > div.rc")
    if len(google_results) > 0:
        for result in google_results:
            link = result.find("a").attrs['href']
            tittle = result.find("h3").text
            description = result.find("span",attrs={"class" : "st"}).text

            embed.add_field(name=tittle, value=f"{description} \n{link}", inline=False)

    print(f"Function GOOGLE called: {search}")

    """ 
    youtube_results = soup.select("div.P94G9b")
    if(len(youtube_results)>0):
        for result in youtube_results:
            print(result.prettify(), end="\n---------------")
    """

    # embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}",inline=False )
    # embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    # embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://rotulosmatesanz.com/wp-content/uploads/2017/09/2000px-Google_G_Logo.svg_.png")
    await ctx.send(embed=embed)

token = os.getenv("DISCORD_TOKEN")
bot.run(token)


