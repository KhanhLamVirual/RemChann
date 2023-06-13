from discord.ext import commands
from discord.ext import *
import discord

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
            embed.set_footer(text=f"Link Download:[Here]({ctx.author.avatar})")
            embed.set_thumbnail(url=ctx.author.avatar)
        else:
            embed.add_field(name=f"{member.display_name} Avatar's ", value=None, inline=True)
            embed.set_image(url=member.avatar)
            embed.set_footer(text=f"Link Download:[Here]({member.avatar})")
            embed.set_thumbnail(url=member.avatar)
        await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(UserCommands(bot))
