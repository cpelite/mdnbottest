# imports
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

bot.load_extension("nationfacts")

#bot-start-up-message
@bot.event
async def on_ready():
    print("Entwickelt von: SvH - Bot-Version: 1.1")
    print("Bot angemeldet und aktiv, warte auf Befehle.")

#bot-version-infos
@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(Title="Informationen über den Bot")
    embed.add_field(name="Entwickelt von", value="Sebastian von Hammer")
    embed.add_field(name="Botversion", value="1.0 - Beta")
    embed.add_field(name="Verwendete Programmiersprache", value="Python 3.9")
    embed.add_field(name="Verwendete Bibliotheken", value="discord.py, os, dotenv")
    await ctx.send(embed=embed)

#falls command nicht existiert.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Sorry!")
        embed.add_field(name="Es tut mir leid..", value = "...aber diesen Befehl / diese MN kenne ich leider (noch) nicht.")
        await ctx.send(embed=embed)

bot.run(TOKEN)