import discord
from discord.ext import commands

class errors:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def debug(ctx, *, code):
        """Evaluates code"""
        if ctx.message.author.id == 143092204741722112:
            author = ctx.message.author
            channel = ctx.message.channel
            code = code.strip('` ')
            result = None
            global_vars = globals().copy()
            global_vars['bot'] = "test bot"
            global_vars['ctx'] = ctx
            global_vars['message'] = ctx.message
            global_vars['author'] = ctx.message.author
            global_vars['channel'] = ctx.message.channel
            global_vars['server'] = ctx.message.guild
            try:
                result = eval(code, global_vars, locals())
            except Exception as e:
                await channel.send("``py\n{}: {}``".format(type(e).__name__, str(e)))
                return
            if asyncio.iscoroutine(result):
                result = await result
            await channel.send("``py\n{}``".format(str(result)))

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
    bot.add_cog(errors(bot))
