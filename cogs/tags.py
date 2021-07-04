import discord
from discord.ext.commands import command, Cog, group
from discord.ext import commands
import json


class Tags(Cog):

    def __init__(self, bot):
        self.bot = bot

    @group(invoke_without_command=True)
    async def tag(self, ctx, *, arg=None):
        if arg != None:
            with open("tags.json", "r") as f:
                load = json.load(f)

            try:
                result = load[arg.lower()]
            except KeyError:
                return await ctx.reply("Could not find the tag you are looking for.")

            embed = discord.Embed(color=ctx.author.color,
                                  title=f"{arg}", description=result)
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                color=ctx.author.color, description="To create/edit a tag use `-tag set <tag name>`\nTo delete a tag use `-tag delete <tag name>`\nTo get a tag use `-tag <tag name>`\nWant to submit a tag? Use `-tag submit <tag name>`")
            await ctx.send(embed=embed)

    @tag.command()
    @commands.has_permissions(manage_messages=True)
    async def set(self, ctx, *, arg):
        with open("tags.json", "r") as f:
            load = json.load(f)

        await ctx.send(f"What do you want to set as an answer for '**{arg}**'")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        response = await self.bot.wait_for("message", check=check)
        res = response.content

        load[arg] = res

        with open("tags.json", "w") as f:
            json.dump(load, f, indent=4)

        embed = discord.Embed(color=ctx.author.color, title="Tag set!")
        embed.add_field(name=arg, value=res)
        await ctx.send(embed=embed)

    @tag.command()
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, *, arg):
        with open("tags.json", "r") as f:
            load = json.load(f)

        try:
            load[arg]
            load.pop(arg)
            with open("tags.json", "w") as f:
                json.dump(load, f, indent=4)
        except KeyError:
            return await ctx.send("No tag found with the given arguments")

        embed = discord.Embed(color=ctx.author.color,
                              description="Deleted tag!")
        await ctx.send(embed=embed)

    @tag.command()
    async def submit(self, ctx, *, arg):
        await ctx.send(f"What do you want to set as an answer for '**{arg}**'")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        response = await self.bot.wait_for("message", check=check)
        res = response.content

        channel = self.bot.get_channel(861125389749452811)

        embed = discord.Embed(color=ctx.author.color, title="Tag submit!")
        embed.add_field(name=arg, value=res)
        embed.set_footer(text=f"Submitted by {ctx.author} ({ctx.author.id})")
        await channel.send(embed=embed)
        await ctx.send(f"{ctx.author.mention}, your tag has been submitted!")


def setup(bot):
    bot.add_cog(Tags(bot))
