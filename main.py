import discord
from discord.ext import commands
import os
token = os.getenv("TOKENDSAAAAAAAAAAAAAA")
intents = discord.Intents.all()
client = commands.Bot(command_prefix="tut!",intents=intents)
from keep_alive import keep_alive

@client.command()
async def greet(ctx):
    await ctx.send(f"Hi, {ctx.author.mention}!")
@client.command()
async def wave(ctx):
    await ctx.send(":wave:")
@client.command()
async def yippie(ctx):
    await ctx.send("https://tenor.com/view/yippee-happy-celebration-joy-confetti-gif-25557730")

keep_alive()
client.run(token)
