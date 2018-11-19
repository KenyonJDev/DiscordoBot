import discord
from discord.ext import commands

class BasicCommands:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self):
        await cient.say('pong!')

    @commands.command()
    async def info(client, *, member: discord.Member):
        fmt = '{0} joined on {0.joined_at} and has {1} roles.'
        await client.send(fmt.format(member, len(member.roles)))

    @commands.command(pass_context=True)
    async def play(ctx):
        url = ctx.message.content
        author = ctx.message.author

        voice_channel = author.voice_channel
        vc = await client.join_voice_channel(voice_channel)

        player = await vc.create_ytdl_player(url)
        player.start()



def setup(bot):
    bot.add_cog(BasicCommands(bot))