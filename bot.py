#Get user input
import discord

TOKEN = 'NTA0NjYwOTQ5OTcwNzE0NjQ1.DrISJw.jP8hJ23eycSshKKa7ur-w0ylkwc'

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

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
        
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    
    
client.run(TOKEN)

#Pass into getKeyword() which breaks down the sentence and determines
#what module should be ran.

#For example:
#User enters "What is 2 x 2?"
#getKeyword("What is 2 x 2?")
#getKeyword return that math.py should be used