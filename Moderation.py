import discord
import random
from discord.ext import commands

class Moderation:
    def __init__(self, client):
        self.client = client

    @commands.command()


def setup(bot):
    bot.add_cog(Moderation(bot))