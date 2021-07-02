import os
import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot(command_prefix="-",
                   intents=discord.Intents.all(), case_sensitive=False)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(config("TOKEN"))
