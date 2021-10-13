import os
import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot(command_prefix="-",
                   intents=discord.Intents.all(), case_sensitive=False)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

for cog in os.listdir("cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog[:-3]}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} failed to load:")
            raise e

bot.run(config("TOKEN"))
