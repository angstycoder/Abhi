import discord
from discord.ext import commands

class custom():
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def version(self):
        """To be edited"""
        await self.bot.say(discord.__version__)
    #@commands.command(s)


def setup(bot):
    bot.add_cog(custom(bot))