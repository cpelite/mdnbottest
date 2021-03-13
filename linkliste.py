from discord.ext import commands
import discord

class allgemeineangebote(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def mnsallgemein(self, ctx):
        embed = discord.Embed(title="Allgemeine MN-Links")
        embed.add_field(name="CartA (Karte)", value="https://carta.mn-orga.de")
        embed.add_field(name="MN-Marktplatz", value="https://mn-marktplatz.de")
        embed.add_field(name="MN-Wiki", value="https://www.mn-wiki.de/index.php?title=Hauptseite")
        await ctx.send(embed=embed)

        return

def setup(mdnbot):
    mdnbot.add_cog(allgemeineangebote(mdnbot))