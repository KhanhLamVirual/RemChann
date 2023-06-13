import discord, os
from discord.ext import commands
from discord.ext.commands import Bot
from api import token, command_prefix

bot = Bot(command_prefix=command_prefix, intents=discord.Intents.all())

for f in os.listdir('./cogs'):
    if f.endswith('.py'):
        bot.load_extension(f"cogs.{f[:-3]}")

bot.run(token)

