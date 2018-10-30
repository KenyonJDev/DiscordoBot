#Get user input
import discord
import asyncio
# module imports
import mathBot

TOKEN = 'NTA0NjYwOTQ5OTcwNzE0NjQ1.DrJuWA.qYYoCL_xGOI_FB8UQBb1YyeBSCk'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    
@client.event
async def on_message(message):
    
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
   
    stringInp = message.content
    isMath = False;   
    
    if message.content.startswith('what'):
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
            await client.send_message(message.channel, 'The answer is {}'.format(ans))
            
client.run(TOKEN)

#For example:
#User enters "What is 2 x 2?"
#getKeyword("What is 2 x 2?")
#getKeyword return that math.py should be used
