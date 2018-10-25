#Get user input
import discord
import asyncio

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
   
    stringArr = message.content.split(" ") #Split the input into an array
    isMath = False;   
    
    if message.content.startswith('what'):
        #flags to decide if the question is a math one
        numCheck = False
        opCheck = False
        
        #Loop through string, check if both and operator and number are included using mathBot
        for i in range(0,len(stringArr)):
            if (mathBot.isNum(stringArr[i])):
                numCheck = True
            elif (mathBot.checkOperator(stringArr[i])):
                opCheck = True
                
        #If both operator and number are included then run calculate from mathBot
        if (numCheck == True and opCheck == True):
            ans = mathBot.calculate(stringArr)
            await client.send_message(message.channel, 'The answer is {}'.format(ans))
            
client.run(TOKEN)

"""
#Tells the user how many messages are in the chat log between them and the bot
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages. Update'.format(counter))
        
    #After 5 seconds the bot 'wakes up'
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
        
    #Greets the user if they type !hello
    elif message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

#Pass into getKeyword() which breaks down the sentence and determines
#what module should be ran.
"""
#For example:
#User enters "What is 2 x 2?"
#getKeyword("What is 2 x 2?")
#getKeyword return that math.py should be used
