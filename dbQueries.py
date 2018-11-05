import mysql.connector

chatbotDB = mysql.connector.connect(
  host   = "localhost",
  user   = "root",
  passwd = "chatbot2018",
  database = "chatbot"
)

cursor = chatbotDB.cursor(buffered=True)

def checkUser(userID):
    cursor.execute("SELECT COUNT(*) FROM users WHERE userID="+str(userID))
    result = cursor.fetchone()
    return(result[0])

def checkUndefined(details):
    for i in range(0,len(details)):
        if details[i] == "undefined":
            details[i] = "None"
            
    return details

def insertDB(userID,details):
    cursor.execute(("INSERT INTO users(userID) VALUES(%s)"),(userID,))
    chatbotDB.commit()
    
    details = checkUndefined(details)
    cursor.executemany("UPDATE users SET name=%s, age=%s, favcolour=%s, gender=%s, city=%s, relationship=%s WHERE userID="+str(userID),(details,))
    chatbotDB.commit()
    
def updateDB(userID,details):
    details = checkUndefined(details)
    cursor.executemany("UPDATE users SET name=%s, age=%s, favcolour=%s, gender=%s, city=%s, relationship=%s WHERE userID="+str(userID),(details,))
    chatbotDB.commit()
    
def getDetails(userID):
    dataQuery = ("SELECT name,age,favcolour,gender,city,relationship FROM users WHERE userID=%s")
    cursor.execute(dataQuery,(userID,))
    result = cursor.fetchall()
    return(result[0])

def updatePol(userID,newPolarity):
    cursor.execute("UPDATE users SET relationship=%s WHERE userID="+str(userID),(newPolarity,))
    chatbotDB.commit()
    print(getDetails(userID))