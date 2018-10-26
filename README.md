# https://discord.gg/WSQ2DK
Link for discord server
# Chatbot
version 1.0
# Discord
This bot has been created to serve as a tool that can be used for useful features
on the discord platform as part of an assignment.



# Program modules
• Math - number operations
• Weather
• Sports
• Basic chat(Personal questions) and greetings
• Basic game-(s)
• Recipes
• Music and Films
• Reminder function (android notification)
• University rankings (worldwide or UK)
• Bus timetables at Coventry
• Currency conversion
If a module cannot answer the question, as default, answer eg. "Sorry ..."
#• One more task!!!:is main code part which connects DISCORD client and redirect a sentance to a module


Every module is a class which is made to answer questions about 1 topic.
# Every module must implement 3 functions:
♦ __init__() - constructor
♦ getKeywords() - must return list of words or words combinations
♦ genAnswer() - module starting function. It analyzes user input and gives answer
genAnswer() function must return TUPLE(boolean, string) - (success?, str_answer_to_user)
if success == False, str_answer can be "" (empty string)

