import datetime
from urllib import parse

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

from utils.log import print_log


class Google(commands.Cog):

    page_name = 'Google'
    url = 'https://www.google.com/search?'
    url_param = 'q'
    embed_image = 'https://i.dlpng.com/static/png/6654190_preview.png'

    def __init__(self, bot, headers):
        self.bot = bot
        self.headers = headers

    @commands.command()
    async def google(self, ctx, *, search):

        await ctx.send(f'Searching in {self.page_name} for: {search}...')
        print_log(self.page_name, search, ctx.author)

        embed = discord.Embed(
            title=f"{self.page_name} [Search Bot]",
            description=f'Search for "{search}".',
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.blue()
        )

        query = parse.urlencode({self.url_param: search})
        url_query = self.url + query

        res = requests.get(url_query, headers=self.headers, allow_redirects=False)
        html_content = res.content
        soup = BeautifulSoup(html_content, 'html.parser')

        results = soup.select("div.g > div.rc")
        i = 0
        if len(results) > 0:
            for result in results:
                link = result.find("a").attrs['href']
                tittle = result.find("h3").text
                description = result.find("span", attrs={"class": "st"}).text
                embed.add_field(name=tittle, value=f"{description} \n{link}", inline=False)


        embed.set_thumbnail(url=self.embed_image)

        await ctx.send(embed=embed)
