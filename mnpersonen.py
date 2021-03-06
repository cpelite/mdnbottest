from discord.ext import commands
import discord

class personen(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def svh(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Sebastian von Hammer")
        embed.add_field(name="Bekannt für", value="Entwickler des MN-Bots")
        embed.add_field(name="Aktuelle Heimatnation", value="Nordhanar")
        embed.add_field(name="Ämter die die Person bekleidet", value="Mitglied der Reichsdiät, Minister für Äußeres und int. Kooperation")
        embed.add_field(name="frühere nennenswerte Ämter", value="ehemaliger dreibürgischer Reichskanzler")
        embed.add_field(name="Funfact", value="Wurde durch einen Putsch aus seinem Amt gejagt.")
        await ctx.send(embed=embed)

        return

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

    @commands.command()
    async def benjaminvonnehrenmann(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Benjamin von Nehrenmann")
        embed.add_field(name="Bekannt für", value="#IusTrimontania #IusAstoria")
        embed.add_field(name="Aktuelle Heimatnation", value="Dreibürgen")
        embed.add_field(name="Ämter die die Person bekleidet", value="Hofkanzler")
        embed.add_field(name="frühere nennenswerte Ämter", value="Reichsjustizminister")
        embed.add_field(name="Funfact", value="Hat bei der Migration des Dreibürgen-Boards auf einen neuen Server, dasselbige als Schlampe bezeichnet.")
        await ctx.send(embed=embed)

        return

    @commands.command()
    async def oliviakaiser(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Olivia Kaiser")
        embed.add_field(name="Bekannt für", value="Ausarbeitung des Gesundheitsberichts in Dreibürgen")
        embed.add_field(name="Aktuelle Heimatnation", value="Dreibürgen")
        embed.add_field(name="Ämter die die Person bekleidet", value="Reichsministerin für Gesundheit und Soziales")
        embed.add_field(name="frühere nennenswerte Ämter", value="-")
        embed.add_field(name="Funfact",value="Traumatisiert gerne Mitspieler.")
        await ctx.send(embed=embed)

        return

    @commands.command()
    async def der(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Giuseppe de Rossi")
        embed.add_field(name="Bekannt für", value="Design-Papst der MNs")
        embed.add_field(name="Aktuelle Heimatnation", value="Gran Novara")
        embed.add_field(name="Ämter die die Person bekleidet", value="-")
        embed.add_field(name="frühere nennenswerte Ämter", value="Generalsekretär des RdN")
        embed.add_field(name="Funfact",value="-")
        await ctx.send(embed=embed)

        return

    @commands.command()
    async def buddenberg(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Dionysos Buddenberg")
        embed.add_field(name="Bekannt für", value="Förderung der kulturellen Szene in den MNs")
        embed.add_field(name="Aktuelle Heimatnation", value="Albernia")
        embed.add_field(name="Ämter die die Person bekleidet", value="-")
        embed.add_field(name="frühere nennenswerte Ämter", value="-")
        embed.add_field(name="Funfact",value="-")
        await ctx.send(embed=embed)

        return

    @commands.command()
    async def platzmeister(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Platzmeister / Attila Saxburger")
        embed.add_field(name="Bekannt für", value="Dienstleistungen rund um die MNs (Minasol)")
        embed.add_field(name="Aktuelle Heimatnation", value="Turanien")
        embed.add_field(name="Ämter die die Person bekleidet", value="Landeshauptmann von Schwion")
        embed.add_field(name="frühere nennenswerte Ämter", value="-")
        embed.add_field(name="Funfact",value="Vater des MN-Hostings.")
        await ctx.send(embed=embed)

        return

    @commands.command()
    async def denton(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Adam Denton")
        embed.add_field(name="Bekannt für", value="Entwickler diverser Plugins für MNs zu Zeiten des WBB3.")
        embed.add_field(name="Aktuelle Heimatnation", value="Astor")
        embed.add_field(name="Ämter die die Person bekleidet", value="-")
        embed.add_field(name="frühere nennenswerte Ämter", value="President of the United States")
        embed.add_field(name="Funfact",value="-")
        await ctx.send(embed=embed)

        return

    @commands.command()
    async def hugovonsagen(self,ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Hugo von Sagen")
        embed.add_field(name="Bekannt für", value="Dreibürgische Außeneule")
        embed.add_field(name="Aktuelle Heimatnation", value="Dreibürgen")
        embed.add_field(name="Ämter die die Person bekleidet", value="Reichsminister")
        embed.add_field(name="frühere nennenswerte Ämter", value="ehem. Reichskanzler, Reichstagspräsident und Reichsminister des Auswärtigen")
        embed.add_field(name="Funfact",value="Ließ ein diplomatisches Schreiben aus Pottyland schreddern.")
        await ctx.send(embed=embed)

        return

    @commands.command()
    async def heinzlüneburg(self, ctx):
        embed = discord.Embed(title="Fakten über eine MN-Persönlichkeit")
        embed.add_field(name="Name der Person", value="Heinz Lüneburg")
        embed.add_field(name="Bekannt für", value="Sammelt Sperrungen wie Panini-Sticker, Defeater of Helen Bont")
        embed.add_field(name="Heimatnation", value="Ratelon")
        embed.add_field(name="Ämter die die Person bekleidet", value="Unionspräsident")
        embed.add_field(name="frühere nennenswerte Ämter", value="Ministerpräsident von Salbor-Katista")
        embed.add_field(name="Funfact", value="Hat Bont fast zum Rücktritt gebracht, traumatisiert gerne Delta.")
        await ctx.send(embed=embed)

        return


def setup(mdnbot):
    mdnbot.add_cog(personen(mdnbot))
