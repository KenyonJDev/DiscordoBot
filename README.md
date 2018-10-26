# https://discord.gg/WSQ2DK
Link for discord server
# Chatbot
version 1.0
# Discord
This bot has been created to serve as a tool that can be used for useful features
on the discord platform as part of an assignment.



# Program modules
- [ ] **Brad** Math - number operations
- [ ] **Josh** Weather
- [ ] **Armandas** Live sport results
- [ ] **Brad** Basic chat(Personal questions) and greetings
- [ ] **Phillip** Basic game-(s)
- [ ] **Jake** Recipes
- [ ] **Phillip** Music and Films
- [ ] **Armandas** Reminder function (android notification or discord message)
- [ ] **---** University rankings (worldwide or UK)
- [ ] **---** Bus timetables at Coventry
- [ ] **Armandas** Currency conversion
- [ ] **Jake** One more task!!!: is main code part which connects DISCORD client and redirect a sentance to a module
- [ ] **Armandas** Another task!!!: user input simulator - testing program

**If a module cannot answer the question, as default, answer eg. "Sorry ..."**

Every module is a class which is made to answer questions about 1 topic.

**Every module _must implement_ 3 functions:**
1. \_\_init\_\_() - constructor
2. getKeywords() - must return list of words or words combinations
3. genAnswer() - module starting function. It analyzes user input and gives answer
genAnswer() function must **return TUPLE(boolean, string)** - (success?, str_answer_to_user)
if success == False, str_answer can be "" (empty string)

