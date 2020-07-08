import discord
from discord.ext import commands


token =  open('token.txt','r')
print(token)

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('NzMwMjI4NDU2MDY2OTA4MTkx.XwUh_g.y-fxHROB_aar3okhI2-XuSBdtlg')
