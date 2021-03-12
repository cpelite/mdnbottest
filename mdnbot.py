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
    print("Entwickelt von: SvH - Bot-Version: 0.1")
    print("Bot angemeldet und aktiv, warte auf Befehle.")

#some facts about different nations
@bot.command()
async def nordhanar(ctx):
    embed = discord.Embed(title="Fakten über Nordhanar")
    embed.add_field(name="Name des Staates", value = "Vereinigtes Kaiserthum von Nordhanar")
    embed.add_field(name="Staatsform", value = "parlamentarische Monarchie")
    embed.add_field(name="Staatsoberhaupt", value = "Benedikt I.")
    embed.add_field(name="Einwohner", value = "ca. 49. Mio")
    await ctx.send(embed=embed)

@bot.command()
async def ratelon(ctx):
    embed = discord.Embed(title="Fakten über die Demokratische Union Ratelon")
    embed.add_field(name="Name des Staates", value = "Demokratische Union Ratelon")
    embed.add_field(name="Staatsform", value = "Republik")
    embed.add_field(name="Staatsoberhaupt", value = "Heinz Lüneburg")
    embed.add_field(name="Einwohner", value = "ca. 154. Mio")
    await ctx.send(embed=embed)

@bot.command()
async def ratelon(ctx):
    embed = discord.Embed(title="Fakten über das Kaiserreich Dreibürgen")
    embed.add_field(name="Name des Staates", value = "Kaiserreich Dreibürgen")
    embed.add_field(name="Staatsform", value = "konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value = "Friedrich Wilhelm I.")
    embed.add_field(name="Einwohner", value = "ca. 319. Mio")
    await ctx.send(embed=embed)


bot.run(TOKEN)