# imports
from typing import List

import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# loading token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# intents festlegen
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

#welcome message new
@bot.event
async def on_ready():
    print("Entwickelt von: SvH - Bot-Version: 0.0.1")
    print("Bot angemeldet und aktiv, warte auf Befehle.")

#simple test command, new structure -
@bot.command()
async def ping(ctx):
    await ctx.send("test")

#some facts about mns.
@bot.command()
async def nordhanar(ctx):
    await ctx.send("Staatsform: parlamentarische Monarchie")
    await ctx.send("Hauptstadt: Syffia")
    await ctx.send("Staatsoberhaupt: Benedikt I.")

bot.run(TOKEN)