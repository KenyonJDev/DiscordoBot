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

# Program modules

**Status list**:
a) ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Not started
b) ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) In progress
c) ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) Done

| Status | Task | file name | Developer |
| --- | --- | --- | --- |
| ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) In progress | main code part which connects DISCORD client and modules | bot.py | Jake |
| ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) Done | user input simulator | inputTests.py | Armandas |
| - | basic chat(Personal questions) and greetings | - | Brad |
| ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) In progress | Reminder function | reminder.py | Armandas |
| ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) Done | Math - number operations | mathBot.py | Brad |
| - | Basic game-(s) | - | Phillip |
| - | Weather | - | Josh |
| - | Live sport results | - | Armandas |
| - | Recipes | - | Jake |
| - | Music and Films | - | Phillip |
| - | Currency conversion | - | Armandas |
| - | Maths Quiz | - | Sam |
| - | Bus timetables at Coventry | - | Josh |
| - | University rankings | - | - |

**If a module cannot answer the question, as default, answer eg. "Sorry ..."**

Every module is a class which is made to answer questions about 1 topic.

**Every module(class) _must implement_ 3 functions:**
1. \_\_init\_\_() - constructor
2. getKeywords() - must return list of words or words combinations
3. getAnswer(userInput) - module starting function. It analyzes user input and gives answer

genAnswer() function must **return None(if fail) or Answer string**

