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
b) ![#b5ab65](https://placehold.it/15/b5ab65/000000?text=+) In progress
c) ![#378c32](https://placehold.it/15/378c32/000000?text=+) Done

| Status | Task | file name | Developer |
| --- | --- | --- | --- |
| ![#b5ab65](https://placehold.it/15/b5ab65/000000?text=+) | main code part which connects DISCORD client and modules | bot.py | Jake |
| ![#378c32](https://placehold.it/15/378c32/000000?text=+) | user input simulator | inputTests.py | Armandas |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | basic chat(Personal questions) and greetings | - | Brad |
| ![#b5ab65](https://placehold.it/15/b5ab65/000000?text=+) | Reminder function | reminder.py | Armandas |
| ![#378c32](https://placehold.it/15/378c32/000000?text=+) | Math - number operations | mathBot.py | Brad |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | Basic game-(s) | - | Phillip |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | Weather | - | Josh |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | Live sport results | - | Armandas |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | Recipes | - | Jake |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | Music and Films | - | Phillip |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | Currency conversion | - | Armandas |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | Maths Quiz | - | Sam |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | Bus timetables at Coventry | - | Josh |
| ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) | University rankings | - | - |

**If a module cannot answer the question, as default, answer eg. "Sorry ..."**

Every module is a class which is made to answer questions about 1 topic.

**Every module(class) _must implement_ 3 functions:**
1. \_\_init\_\_() - constructor
2. getKeywords() - must return list of words or words combinations
3. getAnswer(userInput) - module starting function. It analyzes user input and gives answer

genAnswer() function must **return None(if fail) or Answer string**

