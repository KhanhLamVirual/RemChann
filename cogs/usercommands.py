from discord.ext import commands
from discord.ext import *
import discord
from discord.invite import I
from mindustry import Server

class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded:UserCommands")

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="Pong", description="Bot Is Online!:)", color=discord.Color.random())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.set_thumbnail(url=ctx.author.avatar)
        await ctx.reply(embed = embed)
    
    @commands.command()
    async def avatar(self, ctx, member:discord.Member=None):
        embed = discord.Embed(title="Avatar", color=discord.Color.random())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        if member == None:
            embed.add_field(name=f"{ctx.author.display_name} Avatar's ", value=None, inline=True)
            embed.set_image(url=ctx.author.avatar)
            embed.set_thumbnail(url=ctx.author.avatar)
        else:
            embed.add_field(name=f"{member.display_name} Avatar's ", value=None, inline=True)
            embed.set_image(url=member.avatar)
            embed.set_thumbnail(url=member.avatar)
        await ctx.reply(embed = embed)

    @commands.command()
    async def pingdustry(self, ctx, host:str=None, port:int=6567, timeout:int=10):
        embed = discord.Embed(title="PingDustry", color=discord.Color.random())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        if host == None:
            embed.add_field(name="Missing", value="Missing Address", inline=True)
        else:
            try:
                lol = Server(host, port)
                info = lol.get_status(timeout)
                embed.add_field(name="Name:", value=info['name'], inline=True)
                embed.add_field(name="Map:", value=info['map'], inline=True)
                embed.add_field(name="Players:", value=info["players"], inline=True)
                embed.add_field(name="Wave:", value=info["wave"], inline=False)
                embed.add_field(name="Version:", value=info['version'], inline=False)
                embed.add_field(name="VerType:", value=info["vertype"], inline=False)
                embed.add_field(name="Ping:", value=info["ping"], inline=False)
            except Exception as e:
                embed.add_field(name="Error", value=str(e), inline=False)
        await ctx.reply(embed = embed)
            
def setup(bot):
    bot.add_cog(UserCommands(bot))
