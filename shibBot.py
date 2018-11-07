import os 
import random 

#    https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.send_file
#    https://docs.python.org/3/library/asyncio-task.html#coroutine

def dogCall(request):
    chosenDog = random.choice(os.listdir("/dogContent"))
    dogDir = "/dogContent/" + chosenDog + ".jpg"
    return chosenDog