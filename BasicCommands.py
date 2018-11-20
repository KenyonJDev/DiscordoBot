import discord
from discord.ext import commands
from datetime import datetime

class BasicCommands:
    def __init__(self, client):
        self.client = client

    @commands.command(name="ping")
    async def ping(self, ctx):
        duration = datetime.now() - discord.utils.snowflake_time(ctx.message.id)
        ms = duration.microseconds / 1000
        content = f"Pong! took `{ms} ms`"
        await ctx.send(content=content)

    @commands.command(pass_context=True)
    async def info(self, ctx, *, member: discord.Member):
        fmt = '{0} joined on {0.joined_at} and has {1} roles.'
        await ctx.send(fmt.format(member, len(member.roles)))

    @commands.command(pass_context=True)
    async def play(self, ctx, *, url: str):
        vc = await ctx.author.voice.channel.connect()

        player = await vc.create_ytdl_player(url)
        player.start()



def setup(client):
    client.add_cog(BasicCommands(client))