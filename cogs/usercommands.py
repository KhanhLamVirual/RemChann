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

def setup(bot):
    bot.add_cog(UserCommands(bot))
