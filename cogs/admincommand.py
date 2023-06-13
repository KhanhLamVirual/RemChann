from discord.ext import commands
from discord.ext.commands import *
import discord

class AdminCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded:AdminCommand Loaded")

    @commands.command()
    @has_role("Owner")
    async def add(self, ctx, role:discord.Role=None, member:discord.Member=None):
        embed = discord.Embed(title="Add Role", color=discord.Color.random())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        if role != None:
            if member != None:
                await member.add_roles(role)
                embed.add_field(name="Success", value=f"Added Role {role} To {member.display_name}", inline=True)
            else:
                embed.add_field(name="Missing", value="Missing Role Or Member", inline=True)

        await ctx.reply(embed=embed)

    @commands.command()
    @has_role("Owner")
    async def remove(self, ctx, role:discord.Role=None, member:discord.Member=None):
        embed = discord.Embed(title="Remove Role", color=discord.Color.random())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        if role != None:
            if member != None:
                await member.remove_roles(role)
                embed.add_field(name="Success", value=f"Removed Role {role} From {member.display_name}", inline=True)
            else:
                embed.add_field(name="Missing", value="Missing Member", inline=True)
        else:
            embed.add_field(name="Missing", value="Missing Role", inline=True)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(AdminCommand(bot))
