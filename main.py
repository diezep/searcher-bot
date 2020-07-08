import discord
from discord.ext import commands


token = open('token.txt', 'r+').read()
print("Initializing bot")

bot = commands.Bot(command_prefix='_')

@bot.command()
async def ping(ctx):
    print("-- Ping function called --")
    await ctx.send('pong\n'*40)

bot.run(token)
