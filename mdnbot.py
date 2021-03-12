# imports
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# loading token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# some playing
bot = commands.Bot

# intents festlegen
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#welcome message
@client.event
async def on_ready():
    print('Bot wurde als {0.user} eingeloggt und wartet auf Befehle.'.format(client))

    ''''#Change Status
    activity = discord.Game(name="MN-Marktplatz")
    await client.change_presence(activity=activity)'''''

# normale facts
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$nordhanar'):
        await message.channel.send('Staatsform: Monarchie')
        await message.channel.send('Hauptstadt: Syffia')

    if message.content.startswith('$ratelon'):
        await message.channel.send('Staatsform: Republik')
        await message.channel.send('Hauptstadt: Manuri')

    if message.content.startswith('$dreibürgen'):
        await message.channel.send('Staatsform: konstituionelle Monarchie')
        await message.channel.send('Hauptstadt: Reichstal')

client.run(TOKEN)