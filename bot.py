# module imports
from discord.ext import commands
from textblob import TextBlob
from rivescript import RiveScript
import discord
import asyncio
import mathBot
import weather
import shibBot
#import hangman
#import hangBot
import dbQueries
import re

TOKEN = 'NTA0NjYwOTQ5OTcwNzE0NjQ1.DrJuWA.qYYoCL_xGOI_FB8UQBb1YyeBSCk'

bot = commands.Bot(command_prefix='!')

client = discord.Client()
rs = RiveScript()
rs.load_directory("../ChatBot/RiveFiles", ext=".rive")
rs.sort_replies()

@bot.command()
async def info(client, *, member: discord.Member):
    fmt = '{0} joined on {0.joined_at} and has {1} roles.'
    await client.send(fmt.format(member, len(member.roles)))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    userID = message.author.id
    
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
           
    stringInp = message.content
    if stringInp[0] == '!':
        reObj = re.match('!\w* *', stringInp)
        if reObj:
            stringAction = "{}".format(reObj.group(0))
            stringInp = stringInp.replace(stringAction,"")
            stringAction = stringAction.replace(" ", "")
    
    if dbQueries.checkUser(userID) == 0:
        reply = (rs.reply("localuser", "get database data")).split(" ")
        dbQueries.insertDB(userID,reply)
    else:
        details = dbQueries.getDetails(userID)
        details = " ".join(str(item) for item in details)
        rs.reply("localuser","set database data "+ str(details))
       
    #Pass string to rivescript - check for keywords
    #Return function to run to variable in bot
    
    moduleName = rs.reply("localuser", stringInp)
    def keywordToModule(moduleName, stringInp):
    
        if moduleName == "math":
            return mathBot.checkMath(stringInp)
        elif(moduleName == "dog"):
            return shibBot.checkDog(stringInp)
        elif(moduleName == "weather"):
            return weather.checkWeather(stringInp)
        else:
            return defaultChat(stringInp)
        
    def defaultChat(stringInp):
        reply = (rs.reply("localuser", "get database data")).split(" ")
        dbQueries.updateDB(userID,reply)

        blob = TextBlob(stringInp)
        polarity = blob.sentiment.polarity

        pre = int(polarity)
        post = abs(polarity - pre)

        if polarity >= 0:
            negative = False
        elif polarity < 0:
            negative = True

        polarityToPass = str(negative) + " " + str(post)[2:]
        newPolarity = rs.reply("localuser", "setting polarity " + polarityToPass) #Pass polarity to rivescript to update happiness of both'
        dbQueries.updatePol(userID,newPolarity)

        return(rs.reply("localuser", stringInp))

        reply = (rs.reply("localuser", "get database data")).split(" ")
        dbQueries.updateDB(userID,reply)
        
    output = keywordToModule(moduleName, stringInp)
    await client.send_message(message.channel, output)
    


    
# @bot.command()
# async def weather()

client.run(TOKEN)
asyncio.run(main())
