# module imports
from textblob import TextBlob
# from rivescript import RiveScript
import discord
from discord.ext import commands
from rivescript import RiveScript
import asyncio
#import hangman
#import hangBot
#import dbQueries
import re
#import conversation
import BasicCommands
import sys, traceback
extensions = ['BasicCommands']
TOKEN = 'NTA0NjYwOTQ5OTcwNzE0NjQ1.DrJuWA.qYYoCL_xGOI_FB8UQBb1YyeBSCk'

bot = commands.Bot(command_prefix='!')
client = discord.Client()
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

@bot.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print("error loading [{}]".format(extension, error))

@bot.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print("error loading [{}]".format(extension, error))

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print("error loading [{}]".format(extension, error))

def onNotification(sender, text):
    print(text)
    client.send_message("Direct Message with BradAngliss", "test " + text)

@client.event
async def on_message(message):
    """Runs everytime a user sends a message to the server with the bot"""
    userID = message.author.id
    #dbQueries.initialise(userID,rs)   #Initialises the database and retrieves user information
    stringInp = message.content       
    
    if "[notification]" in str(message):
        await client.send_message(message.channel, message)
    
    # Make sure the bot doesn't reply to itself
    if message.author == client.user:
        return
    
    #Check for command words starting with !, strip out the unimportant parts
    if stringInp[0] == '!':
        reObj = re.match('!\w* *', stringInp)
        if reObj:
            stringAction = "{}".format(reObj.group(0))
            stringInp = stringInp.replace(stringAction,"")
            stringAction = stringAction.replace(" ", "")
    
    #Get an output for the bot to send via keywordToModule()
   # moduleName = rs.reply("localuser", stringInp)    #Determines module by passing to rivescript
   # output = conversation.keywordToModule(moduleName, stringInp,rs, userID, client, message, onNotification)
  #  await client.send_message(message.channel, output)
    
# @bot.command()
# async def weather()

client.run(TOKEN, bot=True, reconnect=True)
asyncio.run(main())
