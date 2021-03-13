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

#bot-start-up-message
@bot.event
async def on_ready():
    print("Entwickelt von: SvH - Bot-Version: 1.0 - Beta")
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
async def daivan(ctx):
    embed = discord.Embed(title="Fakten über Daivan")
    embed.add_field(name="Name des Staates", value="Volksrepublik Daivan")
    embed.add_field(name="Staatsform", value="Volksrepublik")
    embed.add_field(name="Staatsoberhaupt", value="Nguyen Thuan Phong")
    embed.add_field(name="Einwohner", value="45.783.000")
    embed.add_field(name="Kontinent", value="Renzia")
    embed.add_field(name="Hauptstadt", value="Le Xuan")
    await ctx.send(embed=embed)


@bot.command()
async def ratelon(ctx):
    embed = discord.Embed(title="Fakten über die Demokratische Union Ratelon")
    embed.add_field(name="Name des Staates", value="Demokratische Union Ratelon")
    embed.add_field(name="Staatsform", value="föderale Republik")
    embed.add_field(name="Staatsoberhaupt", value="Heinz Lüneburg")
    embed.add_field(name="Einwohner", value="ca. 154.000.000")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Manuri")
    await ctx.send(embed=embed)

@bot.command()
async def dionysos(ctx):
    embed = discord.Embed(title="Fakten über Dionysos")
    embed.add_field(name="Name des Staates", value="Dionysos")
    embed.add_field(name="Staatsform", value="parlamentarische Demokratie")
    embed.add_field(name="Staatsoberhaupt", value="-")
    embed.add_field(name="Einwohner", value="11.735.430")
    embed.add_field(name="Kontinent", value="Harnar")
    embed.add_field(name="Hauptstadt", value="Klauth")
    await ctx.send(embed=embed)

@bot.command()
async def dreibürgen(ctx):
    embed = discord.Embed(title="Fakten über das Kaiserreich Dreibürgen")
    embed.add_field(name="Name des Staates", value="Kaiserreich Dreibürgen")
    embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Friedrich Wilhelm I.")
    embed.add_field(name="Einwohner", value="ca. 319. Mio")
    embed.add_field(name="Kontinent", value="Antica/Harnar")
    embed.add_field(name="Hauptstadt", value="Reichstal")
    await ctx.send(embed=embed)

@bot.command()
async def eldeyja(ctx):
    embed = discord.Embed(title="Fakten über Eldeyja")
    embed.add_field(name="Name des Staates", value="Eldeyja")
    embed.add_field(name="Staatsform", value="parlamentarische Demokratie")
    embed.add_field(name="Staatsoberhaupt", value="-")
    embed.add_field(name="Einwohner", value="565.000")
    embed.add_field(name="Kontinent", value="Insel im Nordanik")
    embed.add_field(name="Hauptstadt", value="Höfudfjördur")
    await ctx.send(embed=embed)

@bot.command()
async def flandrien(ctx):
    embed = discord.Embed(title="Fakten über Flandrien")
    embed.add_field(name="Name des Staates", value="Flandrien")
    embed.add_field(name="Staatsform", value="sozialistische Demokratie")
    embed.add_field(name="Staatsoberhaupt", value="-")
    embed.add_field(name="Einwohner", value="9.503.838")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Marksfurth")
    await ctx.send(embed=embed)

@bot.command()
async def freesland(ctx):
    embed = discord.Embed(title="Fakten über Freesland")
    embed.add_field(name="Name des Staates", value="Königreich Freesland")
    embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Annabelle I.")
    embed.add_field(name="Einwohner", value="16.500.000")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Blaakendam")
    await ctx.send(embed=embed)

@bot.command()
async def fuchsen(ctx):
    embed = discord.Embed(title="Fakten über Fuchsen")
    embed.add_field(name="Name des Staates", value="Freistaat Fuchsen")
    embed.add_field(name="Staatsform", value="basisdemokratische Republik")
    embed.add_field(name="Staatsoberhaupt", value="Henrik Wegland")
    embed.add_field(name="Einwohner", value="ca. 16.4 Millionen")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Klapsmühltal")
    await ctx.send(embed=embed)

@bot.command()
async def fuso(ctx):
    embed = discord.Embed(title="Fakten über Fuso")
    embed.add_field(name="Name des Staates", value="Fuso Teikoku")
    embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Hirohito")
    embed.add_field(name="Einwohner", value="54.568.829")
    embed.add_field(name="Kontinent", value="Renzia")
    embed.add_field(name="Hauptstadt", value="Saizu-miyako")
    await ctx.send(embed=embed)

@bot.command()
async def futuna(ctx):
    embed = discord.Embed(title="Fakten über Futuna")
    embed.add_field(name="Name des Staates", value="Futunische Hegemonie")
    embed.add_field(name="Staatsform", value="Verband der futunischen Zivilisation")
    embed.add_field(name="Staatsoberhaupt", value="Jaavid Lya Gried")
    embed.add_field(name="Einwohner", value="-")
    embed.add_field(name="Kontinent", value="Nerica")
    embed.add_field(name="Hauptstadt", value="Mehita")
    await ctx.send(embed=embed)

@bot.command()
async def grannovara(ctx):
    embed = discord.Embed(title="Fakten über Gran Novara")
    embed.add_field(name="Name des Staates", value="Regno di Gran Novara")
    embed.add_field(name="Staatsform", value="konstitutionell-ständische Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Francesco V.")
    embed.add_field(name="Einwohner", value="135.947.000")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="San Vincenzo")
    await ctx.send(embed=embed)

@bot.command()
async def heijan(ctx):
    embed = discord.Embed(title="Fakten über Heijan")
    embed.add_field(name="Name des Staates", value="Kaiserreich Heijan")
    embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Sadahito")
    embed.add_field(name="Einwohner", value="-")
    embed.add_field(name="Kontinent", value="Renzia")
    embed.add_field(name="Hauptstadt", value="Heijan-Kyo")
    await ctx.send(embed=embed)

@bot.command()
async def ladinien(ctx):
    embed = discord.Embed(title="Fakten über Ladinien")
    embed.add_field(name="Name des Staates", value="Imperium Ladinorum")
    embed.add_field(name="Staatsform", value="absolute Monarchie (Institutionelle Dyarchie)")
    embed.add_field(name="Staatsoberhaupt", value="Arcadius Flavius Aelianus und Honorius Flavius Julianus")
    embed.add_field(name="Einwohner", value="80.000.000")
    embed.add_field(name="Kontinent", value="Salvagiti")
    embed.add_field(name="Hauptstadt", value="Alba Longa und Justianopolis")
    await ctx.send(embed=embed)

@bot.command()
async def korland(ctx):
    embed = discord.Embed(title="Fakten über Korland")
    embed.add_field(name="Name des Staates", value="Freistaat Korland")
    embed.add_field(name="Staatsform", value="Ständestaat")
    embed.add_field(name="Staatsoberhaupt", value="Werner Balzer")
    embed.add_field(name="Einwohner", value="-")
    embed.add_field(name="Kontinent", value="Harnar")
    embed.add_field(name="Hauptstadt", value="Kaisersburg")
    await ctx.send(embed=embed)


@bot.command()
async def masowien(ctx):
    embed = discord.Embed(title="Fakten über Masowien")
    embed.add_field(name="Name des Staates", value="Demokratische Räterepublik Masowien-Baltonien")
    embed.add_field(name="Staatsform", value="demokratische Räterepublik")
    embed.add_field(name="Staatsoberhaupt", value="Gerdu Donk")
    embed.add_field(name="Einwohner", value="-")
    embed.add_field(name="Kontinent", value="Harnar")
    embed.add_field(name="Hauptstadt", value="Masowien-Stadt")
    await ctx.send(embed=embed)

@bot.command()
async def livornien(ctx):
    embed = discord.Embed(title="Fakten über Livornien")
    embed.add_field(name="Name des Staates", value="Königreich beider Archipele Livornien und Melba")
    embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Philipp V.")
    embed.add_field(name="Einwohner", value="ca. 35.855.000")
    embed.add_field(name="Kontinent", value="Insel vor Antica")
    embed.add_field(name="Hauptstadt", value="Altburg")
    await ctx.send(embed=embed)

@bot.command()
async def monikburg(ctx):
    embed = discord.Embed(title="Fakten über Münchberg")
    embed.add_field(name="Name des Staates", value="Monikberg")
    embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Willem IV.")
    embed.add_field(name="Einwohner", value="25.836.742")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Nicolaasburg")
    await ctx.send(embed=embed)


@bot.command()
async def naulakha(ctx):
    embed = discord.Embed(title="Fakten über Naulakha")
    embed.add_field(name="Name des Staates", value="Herzogtum Naulakha")
    embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Alois IV. von Dunkelstein")
    embed.add_field(name="Einwohner", value="30.785.500")
    embed.add_field(name="Kontinent", value="Renzia")
    embed.add_field(name="Hauptstadt", value="Mühlbucht")
    await ctx.send(embed=embed)

@bot.command()
async def nordhanar(ctx):
    embed = discord.Embed(title="Fakten über Nordhanar")
    embed.add_field(name="Name des Staates", value="Vereinigtes Kaiserthum von Nordhanar")
    embed.add_field(name="Staatsform", value="parlamentarische Wahlmonarchie")
    embed.add_field(name="Staatsoberhaupt", value="Benedikt I.")
    embed.add_field(name="Einwohner", value="ca. 47. Mio.")
    embed.add_field(name="Kontinent", value="Harnar")
    embed.add_field(name="Hauptstadt", value="Syffia")
    await ctx.send(embed=embed)

@bot.command()
async def nordmark(ctx):
    embed = discord.Embed(title="Fakten über Nordmark")
    embed.add_field(name="Name des Staates", value="Vereinigtes Königreich der Nordmark")
    embed.add_field(name="Staatsform", value="konstitutionelle Wahlmonarchie")
    embed.add_field(name="Staatsoberhaupt", value="Oskar I.")
    embed.add_field(name="Einwohner", value="21.367.985")
    embed.add_field(name="Kontinent", value="-")
    embed.add_field(name="Hauptstadt", value="Warudin")
    await ctx.send(embed=embed)

@bot.command()
async def pottyland(ctx):
    embed = discord.Embed(title="Fakten über Pottyland")
    embed.add_field(name="Name des Staates", value="Königreich Pottyland")
    embed.add_field(name="Staatsform", value="absolute Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="König Potty")
    embed.add_field(name="Einwohner", value="ca. 4.2 Mio.")
    embed.add_field(name="Kontinent", value="Insel im Medianik")
    embed.add_field(name="Hauptstadt", value="Potopia")
    await ctx.send(embed=embed)

@bot.command()
async def sancristobal(ctx):
    embed = discord.Embed(title="Fakten über San Cristobal")
    embed.add_field(name="Name des Staates", value="Republik San Cristobal")
    embed.add_field(name="Staatsform", value="Militärregierung")
    embed.add_field(name="Staatsoberhaupt", value="Gen. Raul Garcia")
    embed.add_field(name="Einwohner", value="39.085.590")
    embed.add_field(name="Kontinent", value="Salvagiti")
    embed.add_field(name="Hauptstadt", value="Puerto Rojo")
    await ctx.send(embed=embed)

@bot.command()
async def schwarzhahnland(ctx):
    embed = discord.Embed(title="Fakten über das Schwarzhahnland")
    embed.add_field(name="Name des Staates", value="Schwarzhahnland")
    embed.add_field(name="Staatsform", value="Militärregierung")
    embed.add_field(name="Staatsoberhaupt", value="Zwölferrat")
    embed.add_field(name="Einwohner", value="-")
    embed.add_field(name="Kontinent", value="Nerica")
    embed.add_field(name="Hauptstadt", value="-")
    await ctx.send(embed=embed)

@bot.command()
async def severanien(ctx):
    embed = discord.Embed(title="Fakten über Severanien")
    embed.add_field(name="Name des Staates", value="Bundesrepublik Severanien")
    embed.add_field(name="Staatsform", value="präsidiale Bundesrepublik")
    embed.add_field(name="Staatsoberhaupt", value="Alexander Cetkovic")
    embed.add_field(name="Einwohner", value="ca. 49.9 Mio.")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Vinasy")
    await ctx.send(embed=embed)


@bot.command()
async def slezsko(ctx):
    embed = discord.Embed(title="Fakten über Slezsko")
    embed.add_field(name="Name des Staates", value="Slezsko")
    embed.add_field(name="Staatsform", value="präsidiale Republik")
    embed.add_field(name="Staatsoberhaupt", value="Frantisek Hora")
    embed.add_field(name="Einwohner", value="ca. 6.49 Mio.")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Hradcany")
    await ctx.send(embed=embed)


@bot.command()
async def soleado(ctx):
    embed = discord.Embed(title="Fakten über Soleado")
    embed.add_field(name="Name des Staates", value="La Republica de Soleado")
    embed.add_field(name="Staatsform", value="präsidiale Republik")
    embed.add_field(name="Staatsoberhaupt", value="-")
    embed.add_field(name="Einwohner", value="3.983.833")
    embed.add_field(name="Kontinent", value="-")
    embed.add_field(name="Hauptstadt", value="Laguna")
    await ctx.send(embed=embed)

@bot.command()
async def targa(ctx):
    embed = discord.Embed(title="Fakten über Targa")
    embed.add_field(name="Name des Staates", value="Al Mamluka al Targa")
    embed.add_field(name="Staatsform", value="föderal-konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Meehregaan al Talib")
    embed.add_field(name="Einwohner", value="-")
    embed.add_field(name="Kontinent", value="Fezzan")
    embed.add_field(name="Hauptstadt", value="Nerica")
    await ctx.send(embed=embed)


@bot.command()
async def tirnanog(ctx):
    embed = discord.Embed(title="Fakten über Tir na nOg")
    embed.add_field(name="Name des Staates", value="Freie Republik Tir na nOg")
    embed.add_field(name="Staatsform", value="Räterepublik")
    embed.add_field(name="Staatsoberhaupt", value="Siddharta")
    embed.add_field(name="Einwohner", value="ca. 38.691 Mio.")
    embed.add_field(name="Kontinent", value="Insel vor Nerica")
    embed.add_field(name="Hauptstadt", value="Droch-Amsir")
    await ctx.send(embed=embed)

@bot.command()
async def tiszana(ctx):
    embed = discord.Embed(title="Fakten über Tiszana")
    embed.add_field(name="Name des Staates", value="Regatul Tiszana")
    embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Cornel")
    embed.add_field(name="Einwohner", value="43.858.298")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Sorana")
    await ctx.send(embed=embed)

@bot.command()
async def underbergen(ctx):
    embed = discord.Embed(title="Fakten über Underbergen")
    embed.add_field(name="Name des Staates", value="Freie Stadt Unterbergen")
    embed.add_field(name="Staatsform", value="parlamentarische Demokratie")
    embed.add_field(name="Staatsoberhaupt", value="vakant")
    embed.add_field(name="Einwohner", value="ca. 80.000")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Underbergen")
    await ctx.send(embed=embed)

@bot.command()
async def valorien(ctx):
    embed = discord.Embed(title="Fakten über Valorien")
    embed.add_field(name="Name des Staates", value="Grand-Marechalat de la Valorie")
    embed.add_field(name="Staatsform", value="Militärregierung")
    embed.add_field(name="Staatsoberhaupt", value="Gilles de Rais")
    embed.add_field(name="Einwohner", value="ca. 40 Mio.")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="Pressaq-sur-Renante")
    await ctx.send(embed=embed)

@bot.command()
async def valsanto(ctx):
    embed = discord.Embed(title="Fakten über Valsanto")
    embed.add_field(name="Name des Staates", value="Status Valsantinus")
    embed.add_field(name="Staatsform", value="absolute Monarchie")
    embed.add_field(name="Staatsoberhaupt", value="Simon II.")
    embed.add_field(name="Einwohner", value="250.000")
    embed.add_field(name="Kontinent", value="Antica")
    embed.add_field(name="Hauptstadt", value="San Pedro")
    await ctx.send(embed=embed)

@bot.command()
async def verland(ctx):
    embed = discord.Embed(title="Fakten über Verland")
    embed.add_field(name="Name des Staates", value="Frystaat Verland")
    embed.add_field(name="Staatsform", value="präsidiale Republik")
    embed.add_field(name="Staatsoberhaupt", value="Willem Pieck")
    embed.add_field(name="Einwohner", value="6.880.132")
    embed.add_field(name="Kontinent", value="Nerica")
    embed.add_field(name="Hauptstadt", value="Vryburg")
    await ctx.send(embed=embed)

@bot.command()
async def westnerica(ctx):
    embed = discord.Embed(title="Fakten über West Nerica")
    embed.add_field(name="Name des Staates", value="Republic of West Nerica")
    embed.add_field(name="Staatsform", value="parlamentarische Demokratie")
    embed.add_field(name="Staatsoberhaupt", value="Anozie Nwankwo")
    embed.add_field(name="Einwohner", value="ca. 116 Mio.")
    embed.add_field(name="Kontinent", value="Nerica")
    embed.add_field(name="Hauptstadt", value="Kumandae")
    await ctx.send(embed=embed)


@bot.command()
async def zedarien(ctx):
    embed = discord.Embed(title="Fakten über Zedarien")
    embed.add_field(name="Name des Staates", value="Zedarien")
    embed.add_field(name="Staatsform", value="sozialistischer Einparteienstaat")
    embed.add_field(name="Staatsoberhaupt", value="Achmed al Assudi")
    embed.add_field(name="Einwohner", value="ca. 150 Mio.")
    embed.add_field(name="Kontinent", value="Harnar")
    embed.add_field(name="Hauptstadt", value="Hadiqa")
    await ctx.send(embed=embed)

#falls command nicht existiert.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Sorry!")
        embed.add_field(name="Es tut mir leid..", value = "...aber diesen Befehl / diese MN kenne ich leider (noch) nicht.")
        await ctx.send(embed=embed)

bot.run(TOKEN)