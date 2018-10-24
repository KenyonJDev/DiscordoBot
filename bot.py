#Get user input
import discord

TOKEN = 'NTA0NjYwOTQ5OTcwNzE0NjQ1.DrISJw.jP8hJ23eycSshKKa7ur-w0ylkwc'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
#Pass into getKeyword() which breaks down the sentence and determines
#what module should be ran.

#For example:
#User enters "What is 2 x 2?"
#getKeyword("What is 2 x 2?")
#getKeyword return that math.py should be used
