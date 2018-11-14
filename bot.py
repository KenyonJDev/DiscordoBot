# module imports
from textblob import TextBlob
from rivescript import RiveScript
import discord
from discord.ext import commands
from rivescript import RiveScript
import asyncio
#import hangman
#import hangBot
import dbQueries
import re
import conversation
import sys, traceback
TOKEN = 'NTA0NjYwOTQ5OTcwNzE0NjQ1.DrJuWA.qYYoCL_xGOI_FB8UQBb1YyeBSCk'

isFile = False

class MembersCog:
    def __init__(self, bot):
        self.bot = bot

bot = commands.Bot(command_prefix='!')

client = discord.Client()
rs = RiveScript()
rs.load_directory("../ChatBot/RiveFiles", ext=".rive")
rs.sort_replies()

# @commands.command()
# @commands.guild_only()
# async def info(client, *, member: discord.Member):
#     fmt = '{0} joined on {0.joined_at} and has {1} roles.'
#     await client.send(fmt.format(member, len(member.roles)))

@commands.command(pass_context=True)
async def play(ctx):
    url = ctx.message.content
    author = ctx.message.author
        
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

    player = await vc.create_ytdl_player(url)
    player.start()

@client.event
async def on_ready():
    """Runs when the bot is ready, prints to terminal"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

reminderText = ' '
    
def onNotification(sender, text):
    print(text)
    client.send_message("Direct Message with BradAngliss", "test " + text)

@client.event
async def on_message(message):
    """Runs everytime a user sends a message to the server with the bot"""
    userID = message.author.id
    dbQueries.initialise(userID,rs)   #Initialises the database and retrieves user information
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
    moduleName = rs.reply("localuser", stringInp)    #Determines module by passing to rivescript
    output = conversation.keywordToModule(moduleName, stringInp,rs, userID, client, message, onNotification)
    if ("../ChatBot/dog" in output):
        await client.send_file(message.channel, output)
    else:
        await client.send_message(message.channel, output)
    
# @bot.command()
# async def weather()

client.run(TOKEN, bot=True, reconnect=True)
asyncio.run(main())


