import os
import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot(command_prefix="-",
                   intents=discord.Intents.all(), case_sensitive=False)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

for cog in os.listdir(r"cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} is failed to load:")
            raise e

bot.run(config("TOKEN"))
