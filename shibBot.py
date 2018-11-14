import os 
import random 

#    used to aid in building 
#    https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.send_file
#    https://docs.python.org/3/library/asyncio-task.html#coroutine


def checkDog(stringInp):
    splitRequest = stringInp.split('dog', 1) #trip the request down to the relevent content
    print(splitRequest)
    dogRequest = splitRequest[1].strip(" ")
    
    dogCheck = dogInputValidity(dogRequest)

    if dogCheck == True:
        dogImage = dogCall(dogRequest)
        return dogImage
    else:
        if dogRequest == "help":
            return "To request a dog please write dog.\nTo specify a dog, add one of the following to your request using the format dog *chosen type here*;\nshiba, samoyed, pug, cursed, other"
        else:
            return "Sorry, that isnt a valid dog type!"

def dogInputValidity(dogCheck):
    if dogCheck == "shiba" or dogCheck == "samoyed" or dogCheck == "pug" or dogCheck == "other" or dogCheck == "cursed" or dogCheck == "":
        return True #return whether or not the additional content is valid to the module or not
    else:
        return False
    
def dogCall(request):
    chosenType = ""
    chosenDog = ""
    dogType = request
    if dogType == "":
        chosenType = random.choice(os.listdir("../ChatBot/dogContent"))
        chosenDog = chosenType + "/" + random.choice(os.listdir("../ChatBot/dogContent/" + chosenType))
        dogDir = "../ChatBot/dogContent/" + chosenDog 
        return dogDir
    elif dogType == "help":
        important 
    else:
        chosenType = dogType
        chosenDog = chosenType + "/" + random.choice(os.listdir("../ChatBot/dogContent/" + chosenType))
        dogDir = "../ChatBot/dogContent/" + chosenDog 
        return dogDir