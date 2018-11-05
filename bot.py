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
    
    #Select userID from database and compare to discordID of user talking, 
    #if they are equivalent then load previous 'conversation'
    
    if dbQueries.checkUser(userID) == 0:
        reply = (rs.reply("localuser", "get database data")).split(" ")
        dbQueries.insertDB(userID,reply)
    else:
        details = dbQueries.getDetails(userID)
        details = " ".join(str(item) for item in details)
        rs.reply("localuser","set database data "+ str(details))
        
    stringInp = message.content
    
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
        city_id = stringInp
    else:
        blob = TextBlob(stringInp)
        print(blob.sentiment.polarity)
#         reply = rs.reply("localuser", stringInp)
#         await client.send_message(message.channel, reply)
    
    
    
    async def updateCycle(userID):
        await client.wait_until_ready()
        counter = 0    
        while not client.is_closed:
            counter += 1
            reply = (rs.reply("localuser", "get database data")).split(" ")
            dbQueries.updateDB(userID,reply)
            await asyncio.sleep(5)
            
    client.loop.create_task(updateCycle(userID))


client.run(TOKEN)
asyncio.run(main())

