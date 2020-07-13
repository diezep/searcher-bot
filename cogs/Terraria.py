import datetime
from urllib import parse

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

from utils import print_log


class Terraria(commands.Cog):

    page_name = 'Terraria Wiki'
    url = 'https://terraria.fandom.com/es/wiki/Especial:Buscar'
    url_param = 'search'
    embed_image = 'https://i.dlpng.com/static/png/6654190_preview.png'

    def __init__(self, bot, headers):
        self.bot = bot
        self.headers = headers

    @commands.command()
    async def terraria(self, ctx, *, search):
        size = 0

        def get_size(_size, _str):
            _size += len(_str)
            return _size

        await ctx.send(f'Searching in {self.page_name} for: {search}...')
        print_log(self.page_name, search, ctx.author)

        query = parse.urlencode({self.url_param: search})
        url_query = self.url + "?" + query

        res = requests.get(url_query, headers=self.headers, allow_redirects=True)
        html_content = res.content

        soup = BeautifulSoup(html_content, 'html.parser')

        embed = discord.Embed(
            title=f"{self.page_name} [Search Bot]",
            description=f'Search "{search}" in Terraria Wiki.',
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.dark_blue(),
            url=url_query
        )
        embed.set_thumbnail(url=self.embed_image)

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


            # Check size of embed message before add.
            size = get_size(size, result_data)
            if size > 5950:
                break

            embed.add_field(name = tittle, value = f"{details} \n{_url}", inline = False)

        await ctx.send(embed=embed)
