import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.all()

token = os.getenv("Toeknddddddd")

client = commands.Bot(command_prefix="tut!",intents=intents)

@client.command()
async def greet(ctx):
    await ctx.send(f"Hi, {ctx.author.mention}!")

keep_alive()
client.run(token)
