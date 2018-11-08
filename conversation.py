from textblob import TextBlob
import mathBot
import weather
import shibBot
import dbQueries
from reminder import Reminder
import asyncio

def defaultChat(stringInp,rs,userID):
    reply = (rs.reply("localuser", "get database data")).split(" ")
    
    dbQueries.updateDB(userID,reply)

    blob = TextBlob(stringInp)
    polarity = blob.sentiment.polarity

    pre = int(polarity)
    post = abs(polarity - pre)

    if polarity >= 0:
        negative = False
    elif polarity < 0:
        negative = True

    polarityToPass = str(negative) + " " + str(post)[2:]
    newPolarity = rs.reply("localuser", "setting polarity " + polarityToPass) #Pass polarity to rivescript to update happiness of both'
    dbQueries.updatePol(userID,newPolarity)

    reply = (rs.reply("localuser", "get database data")).split(" ")
    dbQueries.updateDB(userID,reply)
    
    return(rs.reply("localuser", stringInp))

def keywordToModule(moduleName, stringInp, rs, userID, client, function=None):
    rmndr = Reminder()
    if moduleName == "math":
        return mathBot.checkMath(stringInp)
    
    elif(moduleName == "dog"):
        return shibBot.checkDog(stringInp)
    
    elif(moduleName == "weather"):
        return weather.checkWeather(stringInp)
    
    elif(rmndr.check(stringInp)):
#         rmndr.listener += function
        rmndr.listener += asyncio.create_task(function).run_until_complete(function)
        rmndr.setReminder('This is my message', 6)
        return rmndr.getAnswer(stringInp)
    else:
        return defaultChat(stringInp,rs, userID)