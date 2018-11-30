import discord
from discord.ext import commands

time_rx = re.compile('[0-9]+')
url_rx = re.compile('https?:\/\/(?:www\.)?.+')

class music:
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['p','P'])
    @commands.guild_only()
    async def play(self, ctx, *, query: str):


def setup(bot):
    bot.add_cog(music(bot))
    print("music loaded")