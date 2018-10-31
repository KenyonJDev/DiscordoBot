import os 
import random 

def dogCall(request):
    chosenDog = random.choice(os.listdir("/dogContent"))
    dogDir = "/dogContent/" + chosenDog + ".jpg"
    await client.send_file(message.channel, dogDir, content=chosenDog[1])