# module imports
import discord
from discord.ext import commands
import asyncio
extensions = ['BasicCommands','weather','Moderation']
TOKEN = 'NTE0MjE4MjA1MzUxNTEwMDE3.DtTWng.P51Ms3PD131pmZ00QjclA5XOeqE'
client = commands.Bot(command_prefix = '!')
@client.event
async def on_ready():
    """Runs when the bot is ready, prints to terminal"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
        await ctx.send('loaded {}'.format(extension))
    except Exception as error:
        print("error loading [{}]".format(extension, error))

@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Unloaded {}'.format(extension))
        await ctx.send('unloaded {}'.format(extension))
    except Exception as error:
        print("error unloading [{}]".format(extension, error))

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print("error loading [{}]".format(extension, error))

client.run(TOKEN, bot=True, reconnect=True)
asyncio.run(main())


