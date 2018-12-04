import mysql.connector

#Establishes a connection with the database
chatbotDB = mysql.connector.connect(
  host   = "localhost",
  user   = "root",
  passwd = "chatbot2018",
  database = "chatbot"
)

cursor = chatbotDB.cursor(buffered=True)
def initialise(userID,rs):
    """Called upon a user input, checks if they are in the DB adds them if not, 
    otherwise retrieves their details. Takes the users discord ID as input and 
    the connection to the bot"""
    if checkUser(userID) == 0:
        reply = (rs.reply("localuser", "get database data")).split(" ")
        insertDB(userID,reply)
    else:
        details = getDetails(userID)
        details = " ".join(str(item) for item in details)
        rs.reply("localuser","set database data "+ str(details))

def checkUser(userID):
    """Checks if a user is in the database, returns the number of matches found, 
    if 0 then they don't exist"""
    cursor.execute("SELECT COUNT(*) FROM users WHERE userID="+str(userID))
    result = cursor.fetchone()
    return(result[0])

def checkUndefined(details):
    """Sets any undefined values as None so they can be better starred in the database. 
    The input is a list of the users details to be iterated over"""
    for i in range(0,len(details)):
        if details[i] == "undefined":
            details[i] = "None"
    return details

def insertDB(userID,details):
    """Inserts the users details into the database, inputs are the users discord ID 
    and a list of the details to be inserted."""
    cursor.execute(("INSERT INTO users(userID) VALUES(%s)"),(userID,))
    chatbotDB.commit()
    
    details = checkUndefined(details)
    cursor.executemany("UPDATE users SET name=%s, age=%s, favcolour=%s, gender=%s, city=%s, relationship=%s WHERE userID="+str(userID),(details,))
    chatbotDB.commit()
    
def updateDB(userID, details):
    """Updates the current values of the DB to be the new ones passed into the function"""
    details = checkUndefined(details)
    cursor.executemany("UPDATE users SET name=%s, age=%s, favcolour=%s, gender=%s, city=%s, relationship=%s WHERE userID="+str(userID),(details,))
    chatbotDB.commit()
    
def getDetails(userID):
    """Retreives the details from the DB for the passed in user, returns a list of their values"""
    dataQuery = ("SELECT name,age,favcolour,gender,city,relationship FROM users WHERE userID=%s")
    cursor.execute(dataQuery,(userID,))
    result = cursor.fetchall()
    return(result[0])

def updatePol(userID,newPolarity):
    """Updates only the polarity for a given user, polarity being the hapineness level between the user and the bot"""
    cursor.execute("UPDATE users SET relationship=%s WHERE userID="+str(userID),(newPolarity,))
    chatbotDB.commit()