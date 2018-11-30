# module imports
from textblob import TextBlob
from rivescript import RiveScript
import discord
from discord.ext import commands
import asyncio
import dbQueries
import re
import conversation
import BasicCommands
import sys, traceback
extensions = ['BasicCommands']
TOKEN = 'NTA0NjYwOTQ5OTcwNzE0NjQ1.DrJuWA.qYYoCL_xGOI_FB8UQBb1YyeBSCk'


client = discord.Client()
clientBot = commands.Bot(command_prefix = '!')

if __name__ == '__main__':
    for extension in extensions:
        try:
            clientBot.load_extension(extension)
        except Exception as error:
            print("error loading [{}]".format(extension, error))

rs = RiveScript()
rs.load_directory("../ChatBot/RiveFiles", ext=".rive")
rs.sort_replies()
    
@client.event
async def on_ready():
    """Runs when the bot is ready, prints to terminal"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@clientBot.command()
async def load(extension):
    try:
        clientBot.load_extension(extension)
        print('Loaded {}'.format(extension))
        await ctx.send('loaded {}'.format(extension))
    except Exception as error:
        print("error loading [{}]".format(extension, error))

@clientBot.command()
async def unload(extension):
    try:
        clientBot.unload_extension(extension)
        print('Unloaded {}'.format(extension))
        await ctx.send('unloaded {}'.format(extension))
    except Exception as error:
        print("error loading [{}]".format(extension, error))


def onNotification(sender, text):
    print(text)

@client.event
async def on_message(message):
    """Runs everytime a user sends a message to the server with the bot"""
    
    # Make sure the bot doesn't reply to itself
    if message.author == client.user:
        return
    
    userID = message.author.id
    dbQueries.initialise(userID, rs)   #Initialises the database and retrieves user information
    stringInp = message.content       
    
    #Get an output for the bot to send via keywordToModule()
    moduleName = rs.reply("localuser", stringInp)    #Determines module by passing to rivescript
    
#     if moduleName == "game":
#         await client.send_file(message.channel, "Welcome to Hangman!")
#         await client.send_file(message.channel, "The word has",length, "letters.")
    
    output = conversation.keywordToModule(moduleName, stringInp,rs, userID, client, message, onNotification)
    
    try:
        await client.send_file(message.channel, output)
    except:
        await client.send_message(message.channel, output)

client.run(TOKEN, bot=True, reconnect=True)
asyncio.run(main())
