import os 
import random 

#    used to aid in building 
#    https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.send_file
#    https://docs.python.org/3/library/asyncio-task.html#coroutine


def checkDog(stringInp):
    """Input the user request. 
       Uses this to check the validity of any additional specifications provided 
       (such as 'pug') and then proceeds with the appropriate steps."""
    splitRequest = stringInp.split('dog', 1)    #strip the request down to the relevant content to be checked.
    print(splitRequest)
    dogRequest = splitRequest[1].strip(" ")
    
    dogCheck = dogInputValidity(dogRequest)    #calls the validity check function

    if dogCheck == True:
        dogImage = dogCall(dogRequest)    #calls the function to output the image
        return dogImage
    else:
        if dogRequest == "help":
            return "To request a dog please write dog.\nTo specify a dog, add one of the following to your request using the format 'dog *chosen type here*;\nshiba, samoyed, pug, cursed, other'"
        else:
            return "Sorry, that isnt a valid dog type!"

def dogInputValidity(dogCheck):
    """The validity check used by checkDog()."""
    if dogCheck == "shiba" or dogCheck == "samoyed" or dogCheck == "pug" or dogCheck == "other" or dogCheck == "cursed" or dogCheck == "":
        return True #return whether or not the additional content is valid to the module or not
    else:
        return False
    
def dogCall(request):    
    """Outputs the image the user has requested, taking into account any specifications."""
    chosenType = ""
    chosenDog = ""
    dogType = request
    if dogType == "":    #if the user has no additional specifications, this code is run to output a completely random image
        chosenType = random.choice(os.listdir("../ChatBot/dogContent"))    #this randomises a selection of the folders within 'dogContent'
        chosenDog = chosenType + "/" + random.choice(os.listdir("../ChatBot/dogContent/" + chosenType))    #this randomises a selection from the images within the selected folder
        dogDir = "../ChatBot/dogContent/" + chosenDog 
        return dogDir
    else:    #if this code has been run and there was a specification added on to the end which was not 'help'; this code is run
        chosenType = dogType
        chosenDog = chosenType + "/" + random.choice(os.listdir("../ChatBot/dogContent/" + chosenType))    #this randomises a selection from the images within the selected folder
        dogDir = "../ChatBot/dogContent/" + chosenDog 
        return dogDir