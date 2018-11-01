# https://discord.gg/GA6bG2g
Link for discord server
# Chatbot
version 1.0
# Discord
This bot has been created to serve as a tool that can be used for useful features
on the discord platform as part of an assignment.

# TO TEST IN CODIO RUN THE FOLLOWING COMMANDS TO CHANGE THE PYTHON VERSION
1) alias python='/usr/bin/python3.5'
2) . ~/.bashrc

To run bot in discord:

3) cd ChatBot/
4) python bot.py

# Running the Stanford CoreNLP server

Make sure you've installed the jdk: 
sudo apt install openjdk-8-jdk

Install stanford coreNPL:
wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip
unzip stanford-corenlp-full-2018-10-05.zip

Run the server:
cd stanford-corenlp-full-2018-10-05
java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000

# Program modules
- [ ] **Jake** One more task!!!: is main code part which connects DISCORD client and redirect a sentence to a module
- [ ] input_simulator**Armandas** Another task!!!: user input simulator - testing program
- [ ] **Brad** Basic chat(Personal questions) and greetings
- [ ] **Armandas** Reminder function (android notification or discord message)
- [ ] **Brad** Math - number operations
- [ ] **Phillip** Basic game-(s)
- [ ] **Josh** Weather
- [ ] **Armandas** Live sport results
- [ ] **Jake** Recipes
- [ ] **Phillip** Music and Films
- [ ] **Armandas** Currency conversion
- [ ] **Sam** Maths Quiz
- [ ] **---** University rankings (worldwide or UK)
- [ ] **Josh** Bus timetables at Coventry

**If a module cannot answer the question, as default, answer eg. "Sorry ..."**

Every module is a class which is made to answer questions about 1 topic.

**Every module _must implement_ 3 functions:**
1. \_\_init\_\_() - constructor
2. getKeywords() - must return list of words or words combinations
3. genAnswer() - module starting function. It analyzes user input and gives answer
genAnswer() function must **return TUPLE(boolean, string)** - (success?, str_answer_to_user)
if success == False, str_answer can be "" (empty string)

