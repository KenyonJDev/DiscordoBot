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

#The following code is influenced by the example in the README 
#from the official Discord.py Github page - 
#https://github.com/Rapptz/discord.py
#It has been altered a lot to fit this project

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

#The following async function was initially taken from https://github.com/Rapptz/discord.py
#It has pretty much been completely re-written and adapted to suit this project.
@client.event
async def on_message(message):
    """Runs everytime a user sends a message to the server with the bot"""
    
    # Prevents the bot being able to reply to itself
    if message.author == client.user:
        return
    
    userID = message.author.id
    stringInp = message.content  
    dbQueries.initialise(userID, rs)   #Initialises the database and retrieves user information if it exists
             
    moduleName = rs.reply("localuser", stringInp)    #Determines which module should be ran by passing to rivescript
    output = conversation.keywordToModule(moduleName, stringInp,rs, userID, client, message, onNotification) #Gets an output for the bot to send via keywordToModule()
    
    #Attempt to output the message as a file, if this isn't possible then output as message
    try:
        await client.send_file(message.channel, output)
    except:
        await client.send_message(message.channel, output)

client.run(TOKEN, bot=True, reconnect=True)
asyncio.run(main())
