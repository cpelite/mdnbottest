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
    print("Entwickelt von: SvH - Bot-Version: 0.2")
    print("Bot angemeldet und aktiv, warte auf Befehle.")

#some facts about different nations
@bot.command()
async def astor(ctx):
    embed = discord.Embed(title="Fakten über Astor")
    embed.add_field(name="Name des Staates", value="United States of Astor")
    embed.add_field(name="Staatsform", value="präsidiale Republik")
    embed.add_field(name="Staatsoberhaupt", value="Sarah Jones")
    embed.add_field(name="Einwohner", value="107.767.700")
    embed.add_field(name="Kontinent", value="Astor")
    embed.add_field(name="Hauptstadt", value="Astoria")
    await ctx.send(embed=embed)

@bot.command()
async def albernia(ctx):
    embed = discord.Embed(title="Fakten über Albernia")
    embed.add_field(name="Name des Staates", value="Kingdom of Albernia")
    embed.add_field(name="Staatsform", value="parlamentarische Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Jane II.")
    embed.add_field(name="Einwohner", value="75.000.000")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Aldenroth")
    await ctx.send(embed=embed)

@bot.command()
async def alsztyna(ctx):
    embed = discord.Embed(title="Fakten über Alsztyna")
    embed.add_field(name="Name des Staates", value="Freie Hansestadt Alsztyna")
    embed.add_field(name="Staatsform", value="Demokratie")
    embed.add_field(name="Staatsoberhaupt", value="Jouwe MacDubs")
    embed.add_field(name="Einwohner", value="715.143")
    embed.add_field(name="Kontinent", value="Harnar")
    embed.add_field(name="Hauptstadt", value="Alsztyna-Stadt")
    await ctx.send(embed=embed)

@bot.command()
async def aquatropolis(ctx):
    embed = discord.Embed(title="Fakten über Aquatropolis")
    embed.add_field(name="Name des Staates", value="Seereich Aquatropolis")
    embed.add_field(name="Staatsform", value="Diktatur")
    embed.add_field(name="Staatsoberhaupt", value="Jeanne Duchamp")
    embed.add_field(name="Einwohner", value="1.800.000")
    embed.add_field(name="Kontinent", value="nicht bekannt.")
    embed.add_field(name="Hauptstadt", value="Aquatropolis City")
    await ctx.send(embed=embed)

@bot.command()
async def andro(ctx):
    embed = discord.Embed(title="Fakten über Andro")
    embed.add_field(name="Name des Staates", value="Föderale Republik Andro")
    embed.add_field(name="Staatsform", value="föderale Demokratie")
    embed.add_field(name="Staatsoberhaupt", value="Georgi Reingoldowitsch Raschnikow")
    embed.add_field(name="Einwohner", value="142.754.206")
    embed.add_field(name="Kontinent", value="Renzia")
    embed.add_field(name="Hauptstadt", value="Koskow")
    await ctx.send(embed=embed)

@bot.command()
async def barnstorvia(ctx):
    embed = discord.Embed(title="Fakten über Barnstorvia")
    embed.add_field(name="Name des Staates", value="Royaume de Barnstorvia")
    embed.add_field(name="Staatsform", value="konst. Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Louis XXI.")
    embed.add_field(name="Einwohner", value="142.754.206")
    embed.add_field(name="Kontinent", value="Renzia")
    embed.add_field(name="Hauptstadt", value="Brissac")
    await ctx.send(embed=embed)

@bot.command()
async def bengali(ctx):
    embed = discord.Embed(title="Fakten über Bengali")
    embed.add_field(name="Name des Staates", value="Bengali")
    embed.add_field(name="Staatsform", value="absolute Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Muawatalli Aliwata")
    embed.add_field(name="Einwohner", value="nicht bekannt")
    embed.add_field(name="Kontinent", value="Salvagiti")
    embed.add_field(name="Hauptstadt", value="Radeshasa")
    await ctx.send(embed=embed)

@bot.command()
async def bergen(ctx):
    embed = discord.Embed(title="Fakten über Bergen")
    embed.add_field(name="Name des Staates", value="Bergen")
    embed.add_field(name="Staatsform", value="parlamentarische Republik")
    embed.add_field(name="Staatsoberhaupt", value="Willem Stroh")
    embed.add_field(name="Einwohner", value="25.061.321")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Freie Stadt Bergen")
    await ctx.send(embed=embed)

@bot.command()
async def chinopien(ctx):
    embed = discord.Embed(title="Fakten über Chinopien")
    embed.add_field(name="Name des Staates", value="Kaiserreich Chinopien")
    embed.add_field(name="Staatsform", value="absolute Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Te Mai")
    embed.add_field(name="Einwohner", value="657.420.400")
    embed.add_field(name="Kontinent", value="Renzia")
    embed.add_field(name="Hauptstadt", value="Qianlongjjing")
    await ctx.send(embed=embed)

@bot.command()
async def cranberra(ctx):
    embed = discord.Embed(title="Fakten über Cranberra")
    embed.add_field(name="Name des Staates", value="Dominion of Cranberra")
    embed.add_field(name="Staatsform", value="parl. Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Jane II.")
    embed.add_field(name="Einwohner", value="10.300.000")
    embed.add_field(name="Kontinent", value="Astor")
    embed.add_field(name="Hauptstadt", value="Oustburgh")
    await ctx.send(embed=embed)

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
async def dreibürgen(ctx):
    embed = discord.Embed(title="Fakten über das Kaiserreich Dreibürgen")
    embed.add_field(name="Name des Staates", value = "Kaiserreich Dreibürgen")
    embed.add_field(name="Staatsform", value = "konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value = "Friedrich Wilhelm I.")
    embed.add_field(name="Einwohner", value = "ca. 319. Mio")
    await ctx.send(embed=embed)

#falls command nicht existiert.
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        await bot.send_message(ctx.message.channel, "Tut mir leid, aber dieser Befehl existiert nicht.")
    else:
        raise error

bot.run(TOKEN)