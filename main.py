#!/usr/bin/python3

import os

import discord
from discord.ext import commands
import datetime

from urllib import parse
from urllib.request import Request, urlopen

import requests

from bs4 import BeautifulSoup

from dotenv import load_dotenv

import re
from unicodedata import normalize



print("-- Initializing variables --")
load_dotenv()

print("-- Initializing UserAgent --")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
headers = {'User-Agent': user_agent}

print("-- Initializing utils functions --")
print_log = lambda pageName, search, author : print(f"Function {pageName} called: \n Search: {search} \n By: {author} \n Timestamp: {datetime.datetime.utcnow()} ")
initial_message = lambda ctx, pageName, search : ctx.send(f'Searching in {pageName} for: {search}...') 

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
    
    initial_message(ctx, page_name, search)
    print_log(page_name, search, ctx.author)

    embed = discord.Embed(
        title=f"{page_name} |[Search Bot]",
        description=f'Search for "{search}".',
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue()
    )

    query = parse.urlencode({url_param: search})
    url_query = url + query

    html_content = requests.get(url_query, headers=headers, allow_redirects=False)
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

@bot.command()
async def stardewv(ctx, *, search):

    page_name = 'Stardew Valley Wiki'
    url = 'https://es.stardewvalleywiki.com'
    url_param = 'search'

    initial_message(ctx, page_name, search)
    print_log(page_name, search, ctx.author)

    query = parse.urlencode({url_param : search})
    url_query = url + "?" + query

    res = requests.get(url_query, headers=headers, allow_redirects=True)
    html_content = res.content

    soup = BeautifulSoup(html_content, 'html.parser')

    if len(res.history) == 1:

        embed = discord.Embed(
            title="Stardew Valley Wiki [Search Bot]",
            description=f'Page "{search}" found directly.',
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.dark_blue(),
            url=url_query
        )
        embed.set_thumbnail(url="https://stardewvalleywiki.com/mediawiki/skins/Vector/stardewimages/site_logo_sm.png")
        # TODO: Get page information directly
        # Burst!

        await ctx.send(embed=embed)

    else:
        names_results = ["Results by tittle of page.. ", "Results by text in page.. "]
        page_results = soup.select("ul.mw-search-results")

        i = 0

        for page_result in page_results:

            embed = discord.Embed(
                title       = "Stardew Valley Wiki [Search Bot]",
                description = names_results[i],
                timestamp   = datetime.datetime.utcnow(),
                color       = discord.Color.dark_blue(),
                url         = url_query,

            )
            embed.set_thumbnail(url="https://stardewvalleywiki.com/mediawiki/skins/Vector/stardewimages/site_logo_sm.png")

            results = page_result.find_all('li')
            for result in results:
                tittle = result.select_one("div.mw-search-result-heading > a").text
                details = result.select_one("div.searchresult").text.replace('{', '').replace('}', '').replace('[', '').replace(']', '')
                data = result.select_one("div.mw-search-result-data").text
                result_url = url + result.select_one("div.mw-search-result-heading > a").attrs['href']

                embed.add_field(name=tittle, value=f"{details} \n{data} \n{result_url}", inline=False)
            i += 1
            await ctx.send(embed=embed)

@bot.command()
async def terraria(ctx, *, search):
    page_name = 'Terraria Wiki'
    url = 'https://terraria.fandom.com/es/wiki/Especial:Buscar'
    url_param = 'search'

    size = 0

    def get_size(_size, _str):
         _size += len(_str)
         return _size

    initial_message(ctx, page_name, search)
    print_log(page_name, search, ctx.author)

    query = parse.urlencode({url_param: search})
    url_query = url + "?" + query

    res = requests.get(url_query, headers=headers, allow_redirects=True)
    html_content = res.content

    soup = BeautifulSoup(html_content, 'html.parser')

    embed = discord.Embed(
        title=f"{page_name} [Search Bot]",
        description=f'Search "{search}" in Terraria Wiki.',
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.dark_blue(),
        url=url_query
    )
    embed.set_thumbnail(url="https://i.dlpng.com/static/png/6654190_preview.png")

    results = soup.select('ul.Results > li[class="result"]')
    for result in results:
        result_data = ''

        tittle = result.select_one("h1 > a").text
        result_data += tittle

        _url = result.select_one("ul > li > a").attrs["href"]
        result_data += _url

        result.h1.decompose()
        result.ul.decompose()
        details = result.article.get_text().replace('\n', '').replace('\t', '')
        result_data += details


        # Check size of embebed message before add.
        size = get_size(size, result_data)
        if size > 5950:
            break

        embed.add_field(name = tittle, value = f"{details} \n{_url}", inline = False)

    await ctx.send(embed=embed)

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)