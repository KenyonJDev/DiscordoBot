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


"""
for i in range(0,len(stringArr)):
    if (isNum(stringArr[i])):
        self.start = i
        break;

for j in range(self.start + 1, len(stringArr)):
    print(j)
    if (isNum(stringArr[j]) == False and checkOperator(stringArr[j])) == False or (j == len(stringArr)):
        print(self.mathAnswer.join(stringArr[2:7]))
        self.mathAnswer = eval(self.mathAnswer.join(stringArr[self.start:j + 1]))
"""        
    