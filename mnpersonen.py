from discord.ext import commands
import discord

class svh(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def svh(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Sebastian von Hammer")
        embed.add_field(name="Bekannt für", value="Entwickler des MN-Bots")
        embed.add_field(name="Aktuelle Heimatnation", value="Nordhanar")
        embed.add_field(name="Ämter die die Person bekleidet", value="Mitglied der Reichsdiät, Gouverneur von San Vezzano")
        embed.add_field(name="frühere nennenswerte Ämter", value="ehemaliger dreibürgischer Reichskanzler")
        embed.add_field(name="Funfact", value="Wurde durch einen Putsch aus seinem Amt gejagt.")
        await ctx.send(embed=embed)

        return

class lordreis(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def lordreis(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Lord Reis")
        embed.add_field(name="Bekannt für", value="sehr bekannter Außenpolitiker")
        embed.add_field(name="Aktuelle Heimatnation", value="Pottyland")
        embed.add_field(name="Ämter die die Person bekleidet", value="Außenminister, Minister für Kalauer und schlechte Witze")
        embed.add_field(name="frühere nennenswerte Ämter", value="-")
        embed.add_field(name="Funfact", value="Ist der Herrscher über einen Haufen Fischstäbchen.")
        await ctx.send(embed=embed)

        return

class spamberg(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def spamberg(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Ludwig von Silberberg")
        embed.add_field(name="Bekannt für", value="ehemaliger oberster Spammer Dreibürgens")
        embed.add_field(name="Aktuelle Heimatnation", value="Dreibürgen")
        embed.add_field(name="Ämter die die Person bekleidet", value="Erbauer der Spamschanze")
        embed.add_field(name="frühere nennenswerte Ämter", value="-")
        embed.add_field(name="Funfact", value="Threadarchäologe")
        await ctx.send(embed=embed)

        return

class nilsvonberg(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def nilsvonberg(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Nils von Berg")
        embed.add_field(name="Bekannt für", value="Inbegriff des MN-Militarismus")
        embed.add_field(name="Aktuelle Heimatnation", value="Dreibürgen")
        embed.add_field(name="Ämter die die Person bekleidet", value="Oberbefehlshaber der Marine")
        embed.add_field(name="frühere nennenswerte Ämter", value="ehemaliger Reichskanzler, ehemaliger Reichsprotektor, ehemaliger Prinzregent von Stauffen")
        embed.add_field(name="Funfact", value="Hat als er Fähnrich zur See das Sautieren erfunden.")
        await ctx.send(embed=embed)

        return

class benjaminvonnehrenmann(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def benjaminvonnehrenmann(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Benjamin von Nehrenmann")
        embed.add_field(name="Bekannt für", value="#JusTrimontania #JusAstoria")
        embed.add_field(name="Aktuelle Heimatnation", value="Dreibürgen")
        embed.add_field(name="Ämter die die Person bekleidet", value="Hofkanzler")
        embed.add_field(name="frühere nennenswerte Ämter", value="-")
        embed.add_field(name="Funfact", value="Hat bei der Migration des Dreibürgen-Boards auf einen neuen Server, dasselbige als Schlampe bezeichnet.")
        await ctx.send(embed=embed)

        return


def setup(mdnbot):
    mdnbot.add_cog(svh(mdnbot))
    mdnbot.add_cog(lordreis(mdnbot))
    mdnbot.add_cog(spamberg(mdnbot))
    mdnbot.add_cog(nilsvonberg(mdnbot))
    mdnbot.add_cog(benjaminvonnehrenmann(mdnbot))