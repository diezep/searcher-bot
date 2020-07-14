import datetime
from urllib import parse

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

from utils.log import print_log
from utils.webss import WebSS
from utils.strings import compare_strings

class StardewValley(commands.Cog):

    page_name = 'Stardew Valley Wiki'
    url = 'https://es.stardewvalleywiki.com'
    url_param = 'search'
    embed_image = "https://stardewvalleywiki.com/mediawiki/skins/Vector/stardewimages/site_logo_sm.png"

    def __init__(self, bot, headers):
        self.bot = bot
        self.headers = headers

    @commands.command(aliases=['stardew', 'valley', 'stardewvalley', 'stardewv'])
    async def StardewValley(self, ctx, *, search):

        await ctx.send(f'Searching in {self.page_name} for: {search}...')
        print_log(self.page_name, search, ctx.author)

        query = parse.urlencode({self.url_param: search})
        url_query = self.url + "?" + query

        res = requests.get(url_query, headers=self.headers,
                           allow_redirects=True)
        html_content = res.content

        soup = BeautifulSoup(html_content, 'html.parser')

        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.dark_blue(),
        )
        embed.set_thumbnail(url=self.embed_image)
        embed.set_author(name=f"{self.page_name} [Searcher Bot]",)
        embed.url = res.url

        image = None


        if len(res.history) == 1:
            
            if len(soup.select('#infoboxborder')) == 1:
                webss = WebSS(url=res.url)
                image = webss.ofElement('//*[@id="infoboxborder"]')
                embed.set_image(url="attachment://image.png")
                webss.close()
            
            title = soup.select_one('#firstHeading').text
            embed.title = title
       
        else:
            names_results = ["Results by title of page.. ", "Results by text in page.. "]
            page_results = soup.select("ul.mw-search-results")

            i_page = 0
            i_res = 0
            for page_result in page_results:

                embed.title = names_results[i_page]

                results = page_result.find_all('li')
                for result in results:
                    title = result.select_one("div.mw-search-result-heading > a").text
                    details = result.select_one("div.searchresult").text.replace('{', '').replace('}', '').replace('[', '').replace(']', '')
                    data = result.select_one("div.mw-search-result-data").text
                    result_url = self.url + result.select_one("div.mw-search-result-heading > a").attrs['href']

                    embed.add_field(name=title, value=f"{details} \n{result_url} \n{data}", inline=False)
                    i_res += 1

                    # Show only 5 results in both result pages.
                    if i_res == 5 or i_res == 10:
                        break

                i_page += 1

        await ctx.send(embed=embed, file=image if image is not None else None)
