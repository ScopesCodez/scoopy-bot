import discord
from discord.ext.commands import command
import json


class Tags(discord.ext.commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Tags(bot))
