import datetime
from urllib import parse

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

from utils.log import print_log
from utils.strings import compare_strings
from utils.webss import WebSS


class Terraria(commands.Cog):

    page_name = 'Terraria Wiki'
    url = 'https://terraria.fandom.com/es/wiki/Especial:Buscar'
    url_param = 'search'
    embed_image = 'https://i.dlpng.com/static/png/6654190_preview.png'

    def __init__(self, bot, headers):
        self.bot = bot
        self.headers = headers
    
    @commands.command(aliases="Terraria")
    async def terraria(self, ctx, *, search):

        await ctx.send(f'Searching in {self.page_name} for: {search}...')
        print_log(self.page_name, search, ctx.author)

        query = parse.urlencode({self.url_param: search})
        url_query = self.url + "?" + query

        res = requests.get(url_query, headers=self.headers, allow_redirects=True)
        html_content = res.content

        soup = BeautifulSoup(html_content, 'html.parser')

        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.dark_blue(),
        )
        embed.set_thumbnail(url=self.embed_image)
        embed.set_author(name = f"{self.page_name} [Search Bot]")
       
        first_result = soup.select_one('a.result-link').text
        image = None
        if compare_strings(search, first_result):

            _url = soup.select_one("a.result-link").attrs["href"]
            _res = requests.get(_url, headers = self.headers, allow_redirects = True)
            _html_content = _res.content

            _soup = BeautifulSoup(_html_content, 'html.parser')

            embed.url = _res.url

            title = _soup.find("h1", attrs={"class":"page-header__title"}).text
            description = _soup.select_one("#mw-content-text > p:first-of-type").text

            embed.title = title
            embed.description = description

            if len(_soup.select("#mw-content-text > aside")) > 0 :
                webss = WebSS(url=_res.url)
                image = webss.ofElement('//*[@id="mw-content-text"]/aside/figure/a/img')
                embed.set_image(url="attachment://image.png")
                webss.close()

        else:

            embed.url = url_query
            embed.title=f"Search results for {search}"
            embed.description=f'Search "{search}" in Terraria Wiki.'
            i = 0
            results =  soup.select('ul.Results > li[class="result"]')
            # Load list of results
            for result in results:

                title = result.select_one("h1 > a").text
                _url = result.select_one("ul > li > a").attrs["href"]

                result.h1.decompose()
                result.ul.decompose()
                details = result.article.get_text().replace('\n', '').replace('\t', '')

                embed.add_field(name = title, value = f"{details} \n{_url}", inline = False)

                # Show only first 5 options.
                i += 1

                if i == 5:
                    break
            
        await ctx.send(embed=embed, file=image)
