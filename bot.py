# module imports
from textblob import TextBlob
from rivescript import RiveScript
import discord
import asyncio
import mathBot
import weather
#import shibBot
#import hangman
#import hangBot
import dbQueries
import re

TOKEN = 'NTA0NjYwOTQ5OTcwNzE0NjQ1.DrJuWA.qYYoCL_xGOI_FB8UQBb1YyeBSCk'

client = discord.Client()
rs = RiveScript()
rs.load_directory("../ChatBot/RiveFiles", ext=".rive")
rs.sort_replies()

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
#     if stringInp[0] == '!':
#         reObj = re.match('!\w* *', stringInp)
#         if reObj:
#             stringAction = "{}".format(reObj.group(0))
#             stringInp = stringInp.replace(stringAction,"")
#             stringAction = stringAction.replace(" ", "")
    
    
    if dbQueries.checkUser(userID) == 0:
        reply = (rs.reply("localuser", "get database data")).split(" ")
        dbQueries.insertDB(userID,reply)
    else:
        details = dbQueries.getDetails(userID)
        details = " ".join(str(item) for item in details)
        rs.reply("localuser","set database data "+ str(details))
        
    if message.content.startswith('!calculate'):
        #Change english to operators and overwrite the input 
        stringInp = mathBot.checkDict(stringInp)
        
        #Flags to decide if the question is a math one
        numCheck = False
        opCheck = False
        rootCheck = False
        
        #Loop through string, check if both and operator and number are included or there is a square root using mathBot
        for i in range(len(stringInp)):
            if (mathBot.isNum(stringInp[i])):
                numCheck = True
            elif (mathBot.checkOperator(stringInp[i])):
                opCheck = True
            elif (mathBot.checkRoot(stringInp)):
                rootCheck = True

        #If both operator and number are included or there is a square root then run calculate from mathBot
        if (numCheck == True and opCheck == True) or rootCheck:
            strToAns = mathBot.isMath(stringInp)
            ans = strToAns.currentEval
            await client.send_message(message.channel, ans)
        else:
            #Set the reply to what is returned by the RiveScript file
            reply = rs.reply("localuser", stringInp)
            await client.send_message(message.channel, reply)

    elif message.content.startswith('!dog'):
        #passes to the shibBot.py module
        dogRequest = stringInp

        shibBot.dogCall(dogRequest)

    elif message.content.startswith('!weather'):
        weather.url_builder(stringInp)
        reply = rs.reply("localuser", stringInp)
        await client.send_message(message.channel, data_output)
    else:
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
        
        reply = rs.reply("localuser", stringInp)
        await client.send_message(message.channel, reply)  
         
        reply = (rs.reply("localuser", "get database data")).split(" ")
        dbQueries.updateDB(userID,reply)


client.run(TOKEN)
asyncio.run(main())
