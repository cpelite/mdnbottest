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

    @commands.command()
    async def organisationen(self, ctx):
        embed = discord.Embed(title="Organisationen")
        embed.add_field(name="Internationale Organisation für Flugverkehr (IOF)", value="https://iof.mn-orga.de")
        embed.add_field(name="Internationale Organisation für Weltraumangelegenheiten (IOWA)", value="https://iowa.mn-orga.de")
        embed.add_field(name="Internationaler Rat", value="https://livornien.li/woltlab/index.php?board/540-maison-des-nations/")
        embed.add_field(name="Völkerbund", value="https://du.mn-welt.de/board/index.php?board/281-völkerbund/")
        await ctx.send(embed=embed)

def setup(mdnbot):
    mdnbot.add_cog(allgemeineangebote(mdnbot))