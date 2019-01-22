# module imports
import discord
from discord.ext import commands
import asyncio
extensions = ['BasicCommands','debug','Moderation','music']
TOKEN = 'not today mr'
client = commands.Bot(command_prefix = '!')
@client.event
async def on_ready():
    """Runs when the bot is ready, prints to terminal"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def load(ctx, extension):
    """Loads an extension"""
    try:
        client.load_extension(extension)
        message = ('Loaded {}'.format(extension))
        print(message)
        await ctx.send(message)
    except Exception as error:
        error_loading = ("error loading [{}]".format(extension, error))
        print(error_loading)
        await ctx.send(error_loading)

@client.command()
async def unload(ctx, extension):
    """Unloads an extension"""
    try:
        client.unload_extension(extension)
        message = ('Unloaded {}'.format(extension))
        print(message)
        await ctx.send(message)
    except Exception as error:
        error_loading = ("error unloading [{}]".format(extension, error))
        print(error_loading)
        await ctx.send(error_loading)

if __name__ == '__main__': #Fetches our cogs from the main file
    for extension in extensions:
        try:
         client.load_extension(extension)
        except Exception as error:
         print("error loading [{}]".format(extension, error))

client.run(TOKEN, bot=True, reconnect=True)
asyncio.run(main())


