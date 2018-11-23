import discord
from discord.ext import commands
import asyncio

class debug:
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["d","D"])
    async def debug(self, ctx, *, code):
        """Evaluates code"""
        if ctx.message.author.id == 143092204741722112:
            author = ctx.message.author
            channel = ctx.message.channel
            code = code.strip('` ')
            result = None
            global_vars = globals().copy()
            global_vars['bot'] = commands
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

def setup(bot):
    bot.add_cog(debug(bot))
