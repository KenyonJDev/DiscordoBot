# https://discord.gg/GA6bG2g
Link for discord server
# Chatbot
version 1.0
# Discord
This bot has been created to serve as a tool that can be used for useful features
on the discord platform as part of an assignment.

# To test in codio
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
| ![#378c32](https://placehold.it/15/378c32/000000?text=+) Done | Main code part which connects DISCORD client and modules | bot.py | Brad |
| ![#378c32](https://placehold.it/15/378c32/000000?text=+) Done | User input simulator | inputTests.py | Armandas |
| ![#378c32](https://placehold.it/15/378c32/000000?text=+) Done | Basic chat(Personal questions) and greetings | conversation.py dbQueries.py brain.py | Brad |
| ![#378c32](https://placehold.it/15/378c32/000000?text=+) Done | Reminder function | reminder.py | Armandas |
| ![#378c32](https://placehold.it/15/378c32/000000?text=+) Done | Math - number operations | mathBot.py | Brad |
| ![#378c32](https://placehold.it/15/378c32/000000?text=+) Done | Weather | weather.py | Josh |
| ![#378c32](https://placehold.it/15/378c32/000000?text=+) Done | Dog | shibBot.py dogContent| Jake |
| ![#b5ab65](https://placehold.it/15/b5ab65/000000?text=+) In progress | Basic game-(s) | hangBot.py hangman.py | Phillip |
| ![#b5ab65](https://placehold.it/15/b5ab65/000000?text=+) In progress | Maths Quiz | MathsQuiz.py | Sam |
| ![#b5ab65](https://placehold.it/15/b5ab65/000000?text=+) In progress | Bus timetables at Coventry | timetable.py | Josh |
| ![#b5ab65](https://placehold.it/15/b5ab65/000000?text=+) In progress | Music module | bot.py | Josh |


**If a module cannot answer the question, as default, answer eg. "Sorry ..."**

Every module is a class which is made to answer questions about 1 topic.

**Every module(class) _must implement_ 3 functions:**
1. \_\_init\_\_() - constructor
2. getAnswer(userInput) - module starting function. It analyzes user input and gives answer

genAnswer() function must **return None(if fail) or Answer string**

