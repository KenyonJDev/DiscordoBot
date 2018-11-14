import os 
import random 

#    used to aid in building 
#    https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.send_file
#    https://docs.python.org/3/library/asyncio-task.html#coroutine


def checkDog(stringInp):
    #passes to the shibBot.py module

    splitRequest = stringInp.split('!dog ', 1) #strip the request down to the relevent content
    dogRequest = splitRequest[1].strip(" ")

    dogCheck = dogInputValidity(dogRequest)

    if dogCheck == True:
        dogImage = dogCall(dogRequest)
# #         await client.send_file(message.channel, dogImage, :feet:, tts = False)
    else:
        if dogRequest == "help":
            return "To request a dog please write !dog.\nTo specify a dog, add one of the following to your request using the format !dog *chosen type here*;\nshiba, samoyed, pug, cursed, other"
        else:
            return "Sorry, that isnt a valid dog type!"

def dogInputValidity(dogCheck):
    if dogCheck == "shiba" or dogType == "samoyed" or dogType == "pug" or dogType == "other" or dogType == "cursed" or dogType == "":
        return True #return whether or not the additional content is valid to the module or not
    else:
        return False
    
def dogCall(request):
    chosenType = ""
    chosenDog = ""
    dogType = request
    if dogType == "":
        chosenType = random.choice(os.listdir("/dogContent"))
        chosenDog = chosenType + "/" + random.choice(os.listdir("/" + chosenType))
        dogDir = "/dogContent/" + chosenDog + ".jpg"
        return chosenDog
    elif dogType == "help":
        important 
    else:
        chosenType = dogType
        chosenDog = chosenType + "/" + random.choice(os.listdir("/" + chosenType))
        dogDir = "/dogContent/" + chosenDog + ".jpg"
        return chosenDog