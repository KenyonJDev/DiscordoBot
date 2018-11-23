import discord
from discord.ext import commands
from datetime import datetime

class BasicCommands:
    def __init__(self, client):
        self.client = client

    @commands.command(aliases =["p","P"])
    @commands.guild_only()
    async def ping(self, ctx):
        """gives response time"""
        duration = datetime.now() - discord.utils.snowflake_time(ctx.message.id)
        ms = duration.microseconds / 1000
        embed = discord.Embed(colour = 0x00ff00,
                              title = "Pong! took `%s ms`" %ms,
                              description = ctx.guild.name
                              )
        embed.set_author(icon_url = ctx.author.avatar_url, name= str(ctx.author))
        embed.set_footer(text = "kenyonJ")
        await ctx.send(content = None, embed = embed)

    @commands.command(aliases = ["i","I"])
    @commands.guild_only()
    async def info(self, ctx, *, member: discord.Member):
        """Gives information on user"""
        embed = discord.Embed(colour = 0x00ff00,
                              title = '{0} joined on {0.joined_at} and has {1} role/s.'.format(member, len(member.roles)-1),
                              description = ctx.guild.name
                              )
        embed.set_author(icon_url = member.avatar_url, name=str(member))
        embed.set_footer(text = "KenyonJ")
        await ctx.send(content = None, embed = embed)

    @commands.command(pass_context=True)
    async def play(self, ctx, *, url: str):
        """plays music to a voice channel"""
        vc = await ctx.author.voice.channel.connect()


        player = await vc.create_ytdl_player(url)
        player.start()

    @commands.command()
    async def repeat(self, ctx, *, arg):
        """repeats what you type"""
        await ctx.send(arg)

    @commands.command()
    async def wordcount(self, ctx, *args):
        """Counts words in string"""
        await ctx.send('{} words'.format(len(args), ', '.join(args)))

    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...')

    @info.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You aren't in a channel!")

    @info.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You aren't in a channel!")


def setup(bot):
    bot.add_cog(BasicCommands(bot))
