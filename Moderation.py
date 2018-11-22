import discord
from discord.ext import commands

class Moderation:
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def welcome(self, ctx):
        embed = discord.Embed(colour = 0x00ff00,
                              title = "Welcome to " + ctx.guild.name + "!",
                              description = "owned by {}".format(ctx.guild.owner)
                              )
        embed.set_author(name=str(ctx.guild.name), icon_url=ctx.guild.icon_url)
        embed.set_footer(text="KenyonJ")
        await ctx.send(content = None, embed = embed)

def setup(bot):
    bot.add_cog(Moderation(bot))