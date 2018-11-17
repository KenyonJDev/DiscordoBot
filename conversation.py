from textblob import TextBlob
import mathBot
import weather
import shibBot
import dbQueries
from reminder import Reminder
import asyncio

def defaultChat(stringInp, rs, userID):
    """Determines the context of the user input as string and returns a response for the bot to output. Updates database."""
    
    #get the current data of the user from RiveScript and update the database
    dbData = (rs.reply("localuser", "get database data")).split(" ")    
    dbQueries.updateDB(userID, dbData)

    #Creates a TextBlob of the input using the TextBlob API
    blob = TextBlob(stringInp)
    polarity = blob.sentiment.polarity    #Determines the sentiment of the input i.e. nice or nasty 

    #Passes the polarity to rivescript to update current 'happiness', floats cannot be passed 
    #to rivescript so pre and post decimal are passed individually
    pre = int(polarity)
    post = abs(polarity - pre)

    if polarity >= 0:
        negative = False
    elif polarity < 0:
        negative = True

    polarityToPass = str(negative) + " " + str(post)[2:]
    newPolarity = rs.reply("localuser", "setting polarity " + polarityToPass)
    dbQueries.updatePol(userID, newPolarity)
    
    dbData = (rs.reply("localuser", "get database data")).split(" ")
    dbQueries.updateDB(userID, dbData)
    
    return(rs.reply("localuser", stringInp))
    
def keywordToModule(moduleName, stringInp, rs, userID, client, message, function = None):
    """Depending on what rivescript returned, the appropriate module is ran"""
    
    rmndr = Reminder()        #Reminder module checked differently so object is instantiated first
    
    if moduleName == "math":
        return mathBot.checkMath(stringInp)
    
    elif(moduleName == "dog"):
        return shibBot.checkDog(stringInp)
    
    elif(moduleName == "weather"):
        return weather.checkWeather(stringInp)
    
#     elif(rmndr.check(stringInp)):         #Boolean is returned, if True then it is a reminder else it isn't
#         pass
#         rmndr.listener += function
#         rmndr.setReminder('This is my message', 2)
#         return(rmndr.getAnswer(stringInp))
    else:
        return defaultChat(stringInp,rs, userID)
    
# rmndr.listener += function
#         rmndr.setReminder('This is my message', 6, client, message)
#         return rmndr.getAnswer(stringInp)