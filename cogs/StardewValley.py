import datetime
from urllib import parse

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

from utils import print_log


class StardewValley(commands.Cog):

    page_name = 'Stardew Valley Wiki'
    url = 'https://es.stardewvalleywiki.com'
    url_param = 'search'
    embed_image = "https://stardewvalleywiki.com/mediawiki/skins/Vector/stardewimages/site_logo_sm.png"

    def __init__(self, bot, headers):
        self.bot = bot
        self.headers =  headers

    @commands.command(aliases=['stardew', 'valley', 'stardewvalley', 'stardewv'])
    async def StardewValley(self, ctx, *, search):

        await ctx.send(f'Searching in {self.page_name} for: {search}...')
        print_log(self.page_name, search, ctx.author)

        query = parse.urlencode({self.url_param: search})
        url_query = self.url + "?" + query

        res = requests.get(url_query, headers=self.headers, allow_redirects=True)
        html_content = res.content

        soup = BeautifulSoup(html_content, 'html.parser')

        if len(res.history) == 1:

            embed = discord.Embed(
                title=f"{self.page_name}[Search Bot]",
                description=f'Page "{search}" found directly.',
                timestamp=datetime.datetime.utcnow(),
                color=discord.Color.dark_blue(),
                url=url_query
            )
            embed.set_thumbnail(
                url="https://stardewvalleywiki.com/mediawiki/skins/Vector/stardewimages/site_logo_sm.png")
            # TODO: Get page information directly
            # Burst!

            await ctx.send(embed=embed)

        else:
            names_results = ["Results by tittle of page.. ", "Results by text in page.. "]
            page_results = soup.select("ul.mw-search-results")

            i_page = 0
            i_res = 0
            for page_result in page_results:

                embed = discord.Embed(
                    title=f"{self.page_name} [Search Bot]",
                    description=names_results[i_page],
                    timestamp=datetime.datetime.utcnow(),
                    color=discord.Color.dark_blue(),
                    url=url_query,

                )
                embed.set_thumbnail(url=self.embed_image)

                results = page_result.find_all('li')
                for result in results:
                    tittle = result.select_one("div.mw-search-result-heading > a").text
                    details = result.select_one("div.searchresult").text.replace('{', '').replace('}', '').replace('[','').replace(']', '')
                    data = result.select_one("div.mw-search-result-data").text
                    result_url = self.url + result.select_one("div.mw-search-result-heading > a").attrs['href']

                    embed.add_field(name=tittle, value=f"{details} \n{result_url} \n{data}", inline=False)
                    i_res += 1

                    # Show only 5 results in both result pages.
                    if i_res == 5 or i_res == 10:
                        break

                i_page += 1

                await ctx.send(embed=embed)
