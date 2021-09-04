import discord
from discord.ext import commands

token = 'INSERT TOKEN'
prefix = "d!"
client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print('\033[94m'+'BOT ONLINE'+'\033[0;0m')

@client.command()
async def test(ctx):
    await ctx.send("Tested")

client.run(token)
