import discord, sqlite3
from discord.ext import commands

token = 'NzU5MDU3MzcwOTY0ODE5OTk4.X239Qw.LYafFdCkzbJwwovVQ4P3XNJUyIk'
prefix = "d!"
client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print('\033[94m'+'BOT CONECTADO'+'\033[0;0m')

@client.command()
async def test(ctx):
    await ctx.send("Tested")

client.run(token)
