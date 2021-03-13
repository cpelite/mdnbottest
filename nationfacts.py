#some facts about different nations

from discord.ext import commands
import discord

class astor(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def astor(self,ctx):
        embed = discord.Embed(title="Fakten über Astor")
        embed.add_field(name="Name des Staates", value="United States of Astor")
        embed.add_field(name="Staatsform", value="präsidiale Republik")
        embed.add_field(name="Staatsoberhaupt", value="Sarah Jones")
        embed.add_field(name="Einwohner", value="107.767.700")
        embed.add_field(name="Kontinent", value="Astor")
        embed.add_field(name="Hauptstadt", value="Astoria")
        await ctx.send(embed=embed)

        return

class albernia(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def albernia(self,ctx):
        embed = discord.Embed(title="Fakten über Albernia")
        embed.add_field(name="Name des Staates", value="Kingdom of Albernia")
        embed.add_field(name="Staatsform", value="parlamentarische Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Jane II.")
        embed.add_field(name="Einwohner", value="75.000.000")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Aldenroth")
        await ctx.send(embed=embed)

        return

class alsztyna(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def alsztyna(self,ctx):
        embed = discord.Embed(title="Fakten über Alsztyna")
        embed.add_field(name="Name des Staates", value="Freie Hansestadt Alsztyna")
        embed.add_field(name="Staatsform", value="Demokratie")
        embed.add_field(name="Staatsoberhaupt", value="Jouwe MacDubs")
        embed.add_field(name="Einwohner", value="715.143")
        embed.add_field(name="Kontinent", value="Harnar")
        embed.add_field(name="Hauptstadt", value="Alsztyna-Stadt")
        await ctx.send(embed=embed)

        return

class aquatropolis(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def aquatropolis(self,ctx):
        embed = discord.Embed(title="Fakten über Aquatropolis")
        embed.add_field(name="Name des Staates", value="Seereich Aquatropolis")
        embed.add_field(name="Staatsform", value="Diktatur")
        embed.add_field(name="Staatsoberhaupt", value="Jeanne Duchamp")
        embed.add_field(name="Einwohner", value="1.800.000")
        embed.add_field(name="Kontinent", value="nicht bekannt.")
        embed.add_field(name="Hauptstadt", value="Aquatropolis City")
        await ctx.send(embed=embed)

        return

class andro(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def andro(self,ctx):
        embed = discord.Embed(title="Fakten über Andro")
        embed.add_field(name="Name des Staates", value="Föderale Republik Andro")
        embed.add_field(name="Staatsform", value="föderale Demokratie")
        embed.add_field(name="Staatsoberhaupt", value="Georgi Reingoldowitsch Raschnikow")
        embed.add_field(name="Einwohner", value="142.754.206")
        embed.add_field(name="Kontinent", value="Renzia")
        embed.add_field(name="Hauptstadt", value="Koskow")
        await ctx.send(embed=embed)

        return

class barnstorvia(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def barnstorvia(self,ctx):
        embed = discord.Embed(title="Fakten über Barnstorvia")
        embed.add_field(name="Name des Staates", value="Royaume de Barnstorvia")
        embed.add_field(name="Staatsform", value="konst. Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Louis XXI.")
        embed.add_field(name="Einwohner", value="142.754.206")
        embed.add_field(name="Kontinent", value="Renzia")
        embed.add_field(name="Hauptstadt", value="Brissac")
        await ctx.send(embed=embed)

        return

class bengali(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def bengali(self,ctx):
        embed = discord.Embed(title="Fakten über Bengali")
        embed.add_field(name="Name des Staates", value="Bengali")
        embed.add_field(name="Staatsform", value="absolute Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Muawatalli Aliwata")
        embed.add_field(name="Einwohner", value="nicht bekannt")
        embed.add_field(name="Kontinent", value="Salvagiti")
        embed.add_field(name="Hauptstadt", value="Radeshasa")
        await ctx.send(embed=embed)

        return

class bergen(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def bergen(self,ctx):
        embed = discord.Embed(title="Fakten über Bergen")
        embed.add_field(name="Name des Staates", value="Bergen")
        embed.add_field(name="Staatsform", value="parlamentarische Republik")
        embed.add_field(name="Staatsoberhaupt", value="Willem Stroh")
        embed.add_field(name="Einwohner", value="25.061.321")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Freie Stadt Bergen")
        await ctx.send(embed=embed)

        return

class chinopien(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def chinopien(self,ctx):
        embed = discord.Embed(title="Fakten über Chinopien")
        embed.add_field(name="Name des Staates", value="Kaiserreich Chinopien")
        embed.add_field(name="Staatsform", value="absolute Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Te Mai")
        embed.add_field(name="Einwohner", value="657.420.400")
        embed.add_field(name="Kontinent", value="Renzia")
        embed.add_field(name="Hauptstadt", value="Qianlongjjing")
        await ctx.send(embed=embed)

        return

class cranberra(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def cranberra(self,ctx):
        embed = discord.Embed(title="Fakten über Cranberra")
        embed.add_field(name="Name des Staates", value="Dominion of Cranberra")
        embed.add_field(name="Staatsform", value="parl. Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Jane II.")
        embed.add_field(name="Einwohner", value="10.300.000")
        embed.add_field(name="Kontinent", value="Astor")
        embed.add_field(name="Hauptstadt", value="Oustburgh")
        await ctx.send(embed=embed)

        return

class daivan(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def daivan(self,ctx):
        embed = discord.Embed(title="Fakten über Daivan")
        embed.add_field(name="Name des Staates", value="Volksrepublik Daivan")
        embed.add_field(name="Staatsform", value="Volksrepublik")
        embed.add_field(name="Staatsoberhaupt", value="Nguyen Thuan Phong")
        embed.add_field(name="Einwohner", value="45.783.000")
        embed.add_field(name="Kontinent", value="Renzia")
        embed.add_field(name="Hauptstadt", value="Le Xuan")
        await ctx.send(embed=embed)

        return

class ratelon(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def ratelon(self,ctx):
        embed = discord.Embed(title="Fakten über die Demokratische Union Ratelon")
        embed.add_field(name="Name des Staates", value="Demokratische Union Ratelon")
        embed.add_field(name="Staatsform", value="föderale Republik")
        embed.add_field(name="Staatsoberhaupt", value="Heinz Lüneburg")
        embed.add_field(name="Einwohner", value="ca. 154.000.000")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Manuri")
        await ctx.send(embed=embed)

        return

class dionysos(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def dionysos(self,ctx):
        embed = discord.Embed(title="Fakten über Dionysos")
        embed.add_field(name="Name des Staates", value="Dionysos")
        embed.add_field(name="Staatsform", value="parlamentarische Demokratie")
        embed.add_field(name="Staatsoberhaupt", value="-")
        embed.add_field(name="Einwohner", value="11.735.430")
        embed.add_field(name="Kontinent", value="Harnar")
        embed.add_field(name="Hauptstadt", value="Klauth")
        await ctx.send(embed=embed)

        return

class dreibürgen(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def dreibürgen(self,ctx):
        embed = discord.Embed(title="Fakten über das Kaiserreich Dreibürgen")
        embed.add_field(name="Name des Staates", value="Kaiserreich Dreibürgen")
        embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Friedrich Wilhelm I.")
        embed.add_field(name="Einwohner", value="ca. 319. Mio")
        embed.add_field(name="Kontinent", value="Antica/Harnar")
        embed.add_field(name="Hauptstadt", value="Reichstal")
        await ctx.send(embed=embed)

        return

class eldeyja(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def eldeyja(self,ctx):
        embed = discord.Embed(title="Fakten über Eldeyja")
        embed.add_field(name="Name des Staates", value="Eldeyja")
        embed.add_field(name="Staatsform", value="parlamentarische Demokratie")
        embed.add_field(name="Staatsoberhaupt", value="Jónas Sigurðsson")
        embed.add_field(name="Einwohner", value="565.000")
        embed.add_field(name="Kontinent", value="Insel im Nordanik")
        embed.add_field(name="Hauptstadt", value="Höfudfjördur")
        await ctx.send(embed=embed)

        return

class flandrien(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def flandrien(self,ctx):
        embed = discord.Embed(title="Fakten über Flandrien")
        embed.add_field(name="Name des Staates", value="Flandrien")
        embed.add_field(name="Staatsform", value="sozialistische Demokratie")
        embed.add_field(name="Staatsoberhaupt", value="-")
        embed.add_field(name="Einwohner", value="9.503.838")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Marksfurth")
        await ctx.send(embed=embed)

        return

class freesland(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def freesland(self,ctx):
        embed = discord.Embed(title="Fakten über Freesland")
        embed.add_field(name="Name des Staates", value="Königreich Freesland")
        embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Annabelle I.")
        embed.add_field(name="Einwohner", value="16.500.000")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Blaakendam")
        await ctx.send(embed=embed)

        return

class fuchsen(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def fuchsen(self,ctx):
        embed = discord.Embed(title="Fakten über Fuchsen")
        embed.add_field(name="Name des Staates", value="Freistaat Fuchsen")
        embed.add_field(name="Staatsform", value="basisdemokratische Republik")
        embed.add_field(name="Staatsoberhaupt", value="Henrik Wegland")
        embed.add_field(name="Einwohner", value="ca. 16.4 Millionen")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Klapsmühltal")
        await ctx.send(embed=embed)

        return

class fuso(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def fuso(self,ctx):
        embed = discord.Embed(title="Fakten über Fuso")
        embed.add_field(name="Name des Staates", value="Fuso Teikoku")
        embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Hirohito")
        embed.add_field(name="Einwohner", value="54.568.829")
        embed.add_field(name="Kontinent", value="Renzia")
        embed.add_field(name="Hauptstadt", value="Saizu-miyako")
        await ctx.send(embed=embed)

        return

class futuna(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def futuna(self,ctx):
        embed = discord.Embed(title="Fakten über Futuna")
        embed.add_field(name="Name des Staates", value="Futunische Hegemonie")
        embed.add_field(name="Staatsform", value="Verband der futunischen Zivilisation")
        embed.add_field(name="Staatsoberhaupt", value="Jaavid Lya Gried")
        embed.add_field(name="Einwohner", value="-")
        embed.add_field(name="Kontinent", value="Nerica")
        embed.add_field(name="Hauptstadt", value="Mehita")
        await ctx.send(embed=embed)

        return

class grannovara(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def grannovara(self,ctx):
        embed = discord.Embed(title="Fakten über Gran Novara")
        embed.add_field(name="Name des Staates", value="Regno di Gran Novara")
        embed.add_field(name="Staatsform", value="konstitutionell-ständische Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Francesco V.")
        embed.add_field(name="Einwohner", value="135.947.000")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="San Vincenzo")
        await ctx.send(embed=embed)

        return

class glenverness(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def glenverness(self,ctx):
        embed = discord.Embed(title="Fakten über Glenverness")
        embed.add_field(name="Name des Staates", value="The Royal Realm of Glenverness")
        embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Hermione III.")
        embed.add_field(name="Einwohner", value="ca. 4.000.000")
        embed.add_field(name="Kontinent", value="Insel vor Antica")
        embed.add_field(name="Hauptstadt", value="Glenverdeen")
        await ctx.send(embed=embed)

        return

class heijan(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def heijan(self,ctx):
        embed = discord.Embed(title="Fakten über Heijan")
        embed.add_field(name="Name des Staates", value="Kaiserreich Heijan")
        embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Sadahito")
        embed.add_field(name="Einwohner", value="-")
        embed.add_field(name="Kontinent", value="Renzia")
        embed.add_field(name="Hauptstadt", value="Heijan-Kyo")
        await ctx.send(embed=embed)

        return

class ladinien(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def ladinien(self,ctx):
        embed = discord.Embed(title="Fakten über Ladinien")
        embed.add_field(name="Name des Staates", value="Imperium Ladinorum")
        embed.add_field(name="Staatsform", value="absolute Monarchie (Institutionelle Dyarchie)")
        embed.add_field(name="Staatsoberhaupt", value="Arcadius Flavius Aelianus und Honorius Flavius Julianus")
        embed.add_field(name="Einwohner", value="80.000.000")
        embed.add_field(name="Kontinent", value="Salvagiti")
        embed.add_field(name="Hauptstadt", value="Alba Longa und Justianopolis")
        await ctx.send(embed=embed)

        return

class korland(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def korland(self,ctx):
        embed = discord.Embed(title="Fakten über Korland")
        embed.add_field(name="Name des Staates", value="Freistaat Korland")
        embed.add_field(name="Staatsform", value="Ständestaat")
        embed.add_field(name="Staatsoberhaupt", value="Werner Balzer")
        embed.add_field(name="Einwohner", value="-")
        embed.add_field(name="Kontinent", value="Harnar")
        embed.add_field(name="Hauptstadt", value="Kaisersburg")
        await ctx.send(embed=embed)

        return

class masowien(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def masowien(self,ctx):
        embed = discord.Embed(title="Fakten über Masowien")
        embed.add_field(name="Name des Staates", value="Demokratische Räterepublik Masowien-Baltonien")
        embed.add_field(name="Staatsform", value="demokratische Räterepublik")
        embed.add_field(name="Staatsoberhaupt", value="Gerdu Donk")
        embed.add_field(name="Einwohner", value="-")
        embed.add_field(name="Kontinent", value="Harnar")
        embed.add_field(name="Hauptstadt", value="Masowien-Stadt")
        await ctx.send(embed=embed)

        return

class livornien(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def livornien(self,ctx):
        embed = discord.Embed(title="Fakten über Livornien")
        embed.add_field(name="Name des Staates", value="Königreich beider Archipele Livornien und Melba")
        embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Philipp V.")
        embed.add_field(name="Einwohner", value="ca. 35.855.000")
        embed.add_field(name="Kontinent", value="Insel vor Antica")
        embed.add_field(name="Hauptstadt", value="Altburg")
        await ctx.send(embed=embed)

        return

class monikberg(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def monikberg(self,ctx):
        embed = discord.Embed(title="Fakten über Münchberg")
        embed.add_field(name="Name des Staates", value="Monikberg")
        embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Willem IV.")
        embed.add_field(name="Einwohner", value="25.836.742")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Nicolaasburg")
        await ctx.send(embed=embed)

        return

class naulakha(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def naulakha(self,ctx):
        embed = discord.Embed(title="Fakten über Naulakha")
        embed.add_field(name="Name des Staates", value="Herzogtum Naulakha")
        embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Alois IV. von Dunkelstein")
        embed.add_field(name="Einwohner", value="30.785.500")
        embed.add_field(name="Kontinent", value="Renzia")
        embed.add_field(name="Hauptstadt", value="Mühlbucht")
        await ctx.send(embed=embed)

        return

class nordhanar(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def nordhanar(self,ctx):
        embed = discord.Embed(title="Fakten über Nordhanar")
        embed.add_field(name="Name des Staates", value="Vereinigtes Kaiserthum von Nordhanar")
        embed.add_field(name="Staatsform", value="parlamentarische Wahlmonarchie")
        embed.add_field(name="Staatsoberhaupt", value="Benedikt I.")
        embed.add_field(name="Einwohner", value="ca. 47. Mio.")
        embed.add_field(name="Kontinent", value="Harnar")
        embed.add_field(name="Hauptstadt", value="Syffia")
        await ctx.send(embed=embed)

        return

class nordmark(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def nordmark(self,ctx):
        embed = discord.Embed(title="Fakten über Nordmark")
        embed.add_field(name="Name des Staates", value="Vereinigtes Königreich der Nordmark")
        embed.add_field(name="Staatsform", value="konstitutionelle Wahlmonarchie")
        embed.add_field(name="Staatsoberhaupt", value="Oskar I.")
        embed.add_field(name="Einwohner", value="21.367.985")
        embed.add_field(name="Kontinent", value="-")
        embed.add_field(name="Hauptstadt", value="Warudin")
        await ctx.send(embed=embed)

        return

class pottyland(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def pottyland(self,ctx):
        embed = discord.Embed(title="Fakten über Pottyland")
        embed.add_field(name="Name des Staates", value="Königreich Pottyland")
        embed.add_field(name="Staatsform", value="absolute Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="König Potty")
        embed.add_field(name="Einwohner", value="ca. 4.2 Mio.")
        embed.add_field(name="Kontinent", value="Insel im Medianik")
        embed.add_field(name="Hauptstadt", value="Potopia")
        await ctx.send(embed=embed)

        return

class sancristobal(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def sancristobal(self,ctx):
        embed = discord.Embed(title="Fakten über San Cristobal")
        embed.add_field(name="Name des Staates", value="Republik San Cristobal")
        embed.add_field(name="Staatsform", value="Militärregierung")
        embed.add_field(name="Staatsoberhaupt", value="Gen. Raul Garcia")
        embed.add_field(name="Einwohner", value="39.085.590")
        embed.add_field(name="Kontinent", value="Salvagiti")
        embed.add_field(name="Hauptstadt", value="Puerto Rojo")
        await ctx.send(embed=embed)

        return

class schwarzhahnland(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def schwarzhahnland(self,ctx):
        embed = discord.Embed(title="Fakten über das Schwarzhahnland")
        embed.add_field(name="Name des Staates", value="Schwarzhahnland")
        embed.add_field(name="Staatsform", value="Militärregierung")
        embed.add_field(name="Staatsoberhaupt", value="Zwölferrat")
        embed.add_field(name="Einwohner", value="-")
        embed.add_field(name="Kontinent", value="Nerica")
        embed.add_field(name="Hauptstadt", value="-")
        await ctx.send(embed=embed)

        return

class severanien(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def severanien(self,ctx):
        embed = discord.Embed(title="Fakten über Severanien")
        embed.add_field(name="Name des Staates", value="Bundesrepublik Severanien")
        embed.add_field(name="Staatsform", value="präsidiale Bundesrepublik")
        embed.add_field(name="Staatsoberhaupt", value="Alexander Cetkovic")
        embed.add_field(name="Einwohner", value="ca. 49.9 Mio.")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Vinasy")
        await ctx.send(embed=embed)

        return

class slezsko(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def slezsko(self,ctx):
        embed = discord.Embed(title="Fakten über Slezsko")
        embed.add_field(name="Name des Staates", value="Slezsko")
        embed.add_field(name="Staatsform", value="präsidiale Republik")
        embed.add_field(name="Staatsoberhaupt", value="Frantisek Hora")
        embed.add_field(name="Einwohner", value="ca. 6.49 Mio.")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Hradcany")
        await ctx.send(embed=embed)

        return

class soleado(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def soleado(self,ctx):
        embed = discord.Embed(title="Fakten über Soleado")
        embed.add_field(name="Name des Staates", value="La Republica de Soleado")
        embed.add_field(name="Staatsform", value="präsidiale Republik")
        embed.add_field(name="Staatsoberhaupt", value="-")
        embed.add_field(name="Einwohner", value="3.983.833")
        embed.add_field(name="Kontinent", value="-")
        embed.add_field(name="Hauptstadt", value="Laguna")
        await ctx.send(embed=embed)

        return

class targa(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def targa(self,ctx):
        embed = discord.Embed(title="Fakten über Targa")
        embed.add_field(name="Name des Staates", value="Al Mamluka al Targa")
        embed.add_field(name="Staatsform", value="föderal-konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Meehregaan al Talib")
        embed.add_field(name="Einwohner", value="-")
        embed.add_field(name="Kontinent", value="Nerica")
        embed.add_field(name="Hauptstadt", value="Fezzan")
        await ctx.send(embed=embed)

        return

class tirnanog(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def tirnanog(self,ctx):
        embed = discord.Embed(title="Fakten über Tir na nOg")
        embed.add_field(name="Name des Staates", value="Freie Republik Tir na nOg")
        embed.add_field(name="Staatsform", value="Räterepublik")
        embed.add_field(name="Staatsoberhaupt", value="Siddharta")
        embed.add_field(name="Einwohner", value="ca. 38.691 Mio.")
        embed.add_field(name="Kontinent", value="Insel vor Nerica")
        embed.add_field(name="Hauptstadt", value="Droch-Amsir")
        await ctx.send(embed=embed)

        return

class tiszana(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def tiszana(self,ctx):
        embed = discord.Embed(title="Fakten über Tiszana")
        embed.add_field(name="Name des Staates", value="Regatul Tiszana")
        embed.add_field(name="Staatsform", value="konstitutionelle Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Cornel")
        embed.add_field(name="Einwohner", value="43.858.298")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Sorana")
        await ctx.send(embed=embed)

        return

class turanien(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def turanien(self,ctx):
        embed = discord.Embed(title="Fakten über Turanien")
        embed.add_field(name="Name des Staates", value="Turanische Föderation")
        embed.add_field(name="Staatsform", value="parlamentarische Demokratie")
        embed.add_field(name="Staatsoberhaupt", value="Sigurd Thorwald")
        embed.add_field(name="Einwohner", value="50.048.300")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Turan")
        await ctx.send(embed=embed)

        return

class underbergen(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def underbergen(self,ctx):
        embed = discord.Embed(title="Fakten über Underbergen")
        embed.add_field(name="Name des Staates", value="Freie Stadt Unterbergen")
        embed.add_field(name="Staatsform", value="parlamentarische Demokratie")
        embed.add_field(name="Staatsoberhaupt", value="vakant")
        embed.add_field(name="Einwohner", value="ca. 80.000")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Underbergen")
        await ctx.send(embed=embed)

        return

class valorien(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def valorien(self,ctx):
        embed = discord.Embed(title="Fakten über Valorien")
        embed.add_field(name="Name des Staates", value="Grand-Marechalat de la Valorie")
        embed.add_field(name="Staatsform", value="Militärregierung")
        embed.add_field(name="Staatsoberhaupt", value="Gilles de Rais")
        embed.add_field(name="Einwohner", value="ca. 40 Mio.")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="Pressaq-sur-Renante")
        await ctx.send(embed=embed)

        return

class valsanto(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def valsanto(self,ctx):
        embed = discord.Embed(title="Fakten über Valsanto")
        embed.add_field(name="Name des Staates", value="Status Valsantinus")
        embed.add_field(name="Staatsform", value="absolute Monarchie")
        embed.add_field(name="Staatsoberhaupt", value="Simon II.")
        embed.add_field(name="Einwohner", value="250.000")
        embed.add_field(name="Kontinent", value="Antica")
        embed.add_field(name="Hauptstadt", value="San Pedro")
        await ctx.send(embed=embed)

        return

class verland(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def verland(self,ctx):
        embed = discord.Embed(title="Fakten über Verland")
        embed.add_field(name="Name des Staates", value="Frystaat Verland")
        embed.add_field(name="Staatsform", value="präsidiale Republik")
        embed.add_field(name="Staatsoberhaupt", value="Willem Pieck")
        embed.add_field(name="Einwohner", value="6.880.132")
        embed.add_field(name="Kontinent", value="Nerica")
        embed.add_field(name="Hauptstadt", value="Vryburg")
        await ctx.send(embed=embed)

        return

class westnerica(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def westnerica(self,ctx):
        embed = discord.Embed(title="Fakten über West Nerica")
        embed.add_field(name="Name des Staates", value="Republic of West Nerica")
        embed.add_field(name="Staatsform", value="parlamentarische Demokratie")
        embed.add_field(name="Staatsoberhaupt", value="Anozie Nwankwo")
        embed.add_field(name="Einwohner", value="ca. 116 Mio.")
        embed.add_field(name="Kontinent", value="Nerica")
        embed.add_field(name="Hauptstadt", value="Kumandae")
        await ctx.send(embed=embed)

        return

class zedarien(commands.Cog):
    def __init__(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def zedarien(self,ctx):
        embed = discord.Embed(title="Fakten über Zedarien")
        embed.add_field(name="Name des Staates", value="Zedarien")
        embed.add_field(name="Staatsform", value="sozialistischer Einparteienstaat")
        embed.add_field(name="Staatsoberhaupt", value="Achmed al Assudi")
        embed.add_field(name="Einwohner", value="ca. 150 Mio.")
        embed.add_field(name="Kontinent", value="Harnar")
        embed.add_field(name="Hauptstadt", value="Hadiqa")
        await ctx.send(embed=embed)

        return

def setup(mdnbot):
    mdnbot.add_cog(astor(mdnbot))
    mdnbot.add_cog(albernia(mdnbot))
    mdnbot.add_cog(alsztyna(mdnbot))
    mdnbot.add_cog(aquatropolis(mdnbot))
    mdnbot.add_cog(andro(mdnbot))
    mdnbot.add_cog(barnstorvia(mdnbot))
    mdnbot.add_cog(bengali(mdnbot))
    mdnbot.add_cog(bergen(mdnbot))
    mdnbot.add_cog(chinopien(mdnbot))
    mdnbot.add_cog(daivan(mdnbot))
    mdnbot.add_cog(ratelon(mdnbot))
    mdnbot.add_cog(dionysos(mdnbot))
    mdnbot.add_cog(dreibürgen(mdnbot))
    mdnbot.add_cog(eldeyja(mdnbot))
    mdnbot.add_cog(flandrien(mdnbot))
    mdnbot.add_cog(freesland(mdnbot))
    mdnbot.add_cog(fuchsen(mdnbot))
    mdnbot.add_cog(fuso(mdnbot))
    mdnbot.add_cog(heijan(mdnbot))
    mdnbot.add_cog(ladinien(mdnbot))
    mdnbot.add_cog(korland(mdnbot))
    mdnbot.add_cog(masowien(mdnbot))
    mdnbot.add_cog(livornien(mdnbot))
    mdnbot.add_cog(monikberg(mdnbot))
    mdnbot.add_cog(naulakha(mdnbot))
    mdnbot.add_cog(nordhanar(mdnbot))
    mdnbot.add_cog(nordmark(mdnbot))
    mdnbot.add_cog(pottyland(mdnbot))
    mdnbot.add_cog(sancristobal(mdnbot))
    mdnbot.add_cog(schwarzhahnland(mdnbot))
    mdnbot.add_cog(severanien(mdnbot))
    mdnbot.add_cog(slezsko(mdnbot))
    mdnbot.add_cog(targa(mdnbot))
    mdnbot.add_cog(tirnanog(mdnbot))
    mdnbot.add_cog(turanien(mdnbot))
    mdnbot.add_cog(tiszana(mdnbot))
    mdnbot.add_cog(underbergen(mdnbot))
    mdnbot.add_cog(valorien(mdnbot))
    mdnbot.add_cog(valsanto(mdnbot))
    mdnbot.add_cog(westnerica(mdnbot))
    mdnbot.add_cog(zedarien(mdnbot))
