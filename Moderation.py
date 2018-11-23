import discord
from discord.ext import commands

class Moderation:
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def welcome(self, ctx):
        """Generates a simple welcome message for the server"""
        embed = discord.Embed(colour = 0x00ff00,
                              title = "Welcome to " + ctx.guild.name + "!",
                              description = "owned by {}".format(ctx.guild.owner)
                              )
        embed.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.guild.name))
        embed.set_footer(text="KenyonJ")
        embed.set_image(url='http://pluspng.com/img-png/welcome-png-welcome-png-image-1556.png')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(content = None, embed = embed)

def setup(bot):
    bot.add_cog(Moderation(bot))