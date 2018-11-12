''' ----- USAGE -----
from reminder import Reminder

def onNotification(sender, message):
    print(message)    

# create reminder object
rmndr = Reminder()
# add function to execute
rmndr.listener += onNotification
# analyse user string and set reminder with this function
rmndr.getAnswer('User string')

# manually set reminder args(text, secondsToWait)
rmndr.setReminder('This is my message', 8)
'''


import sched, time
import event
import _thread
    
class Reminder():
    # functions list to be executed on call of invokeListener()
    listener = event.Event()
    ACTION_NONE = -1
    ACTION_ADD = 0 # requires: time stamp, message
    ACTION_DEL = 1 
    ACTION_SHOW = 2
    KEYWORDS = 3
    DEFAULT_STRINGS = ['Hmm, can you give me more details?', 'Sorry, I cannot set you a reminder! Can you be more precise?', 'I missunderstand :(. Can you explain in a different way?']
    
    def __init__(self):
        self.sched = sched.scheduler(time.time, time.sleep)
    
    ''' <summary>Gives tags which are used to detect user action</summary>
        <return>dict of {'str': list}</return>'''
    def getTags(self):
        d = {self.ACTION_ADD: ['set', 'create', 'make', 'send', 'message me', 'type', 'write'],
             self.ACTION_DEL: ['remove', 'cancel', 'dont', 'do not', 'stop', 'delete'],
             self.ACTION_SHOW: ['what', 'when', 'show', 'list'],
             self.KEYWORDS: ['reminder', 'notification', 'write', 'alarm', 'remind', 'notif', 'recall', 'note']}
        return d
    
    def check(self, msg):
        keywords = self.getTags()[self.KEYWORDS]
        for keyw in keywords:
            if keyw in msg:
                return True
        return False
        
    
    def pickRandom(self, _list):
        import random
        return _list[random.randint(0, len(_list)) - 1]
    
    ''' <summary>Function to be threaded</summary>'''
    def reminderThread(self, text, delayInSec):
        self.sched.enter(delayInSec, 1, self.invokeListener, (text, ))
        self.sched.run()
    
    ''' <summary>Sets a timer for invokation</summary>'''
    def setReminder(self, text, delayInSec):
        _thread.start_new_thread(self.reminderThread, (text, delayInSec) )
    
    ''' <summary>Notifies caller class to pull reminder</summary> '''
    def invokeListener(self, text):
        self.listener(text)
    
    ''' <summary>Keywords for finding the right module</summary>
        <return>list of strings</return> '''
    def getKeywords(self):
        return self.getTags()[self.KEYWORDS]
    
    def timeStrToMillis(timeStr):
        pass
    
    ''' <summary>Analyze and add reminder</summary>
        <return>str(feedback to user)</return> '''
    def actionAdd(self, userInput):
        # example: Make a reminder to call my mom after 10 seconds
        # time recognition: at, after
        # message recognition: to, :
        try:
            # determine time string
            timeIdentificator = ""
            timeIdentificators = [' at ', ' after ', ' in ']
            for identificator in timeIdentificators:
                if identificator in userInput:
                    timeIdentificator = identificator
                    break
            if timeIdentificator == "":
                return "Bro... Repeat one more time with specified time ;)"
            else:
                timeStartId = userInput.find(timeIdentificator) + len(timeIdentificator)
            # determine note message
            msgIdentificator = ""
            msgIdentificators = [' with message to ', ' with message of ' ,' with the message of ' ,' with a message of ', ' with text of ', ' to ', ':']
            for identificator in msgIdentificators:
                if identificator in userInput:
                    msgIdentificator = identificator
                    break            
            msgStartId = userInput.find(msgIdentificator) + len(msgIdentificator)
            if msgStartId == -1: # a reminder without text
                message = "empty"
                time = userInput[timeStartId:]
#                 self.setReminder(message, self.timeStrToMillis(time))
            else:
                if msgStartId > timeStartId: # time is defined before text
                    message = userInput[msgStartId:]
                    userInput = userInput[:int(msgStartId - len(msgIdentificator))]
                    time = userInput[timeStartId:]
                elif timeStartId > msgStartId:
                    time = userInput[timeStartId:]
                    userInput = userInput[:int(timeStartId - len(timeIdentificator))]
                    message = userInput[msgStartId:]                  
            return "I set a reminder{}{} with a message: {}".format(timeIdentificator, time, message)
        except:
            return self.pickRandom(self.DEFAULT_STRINGS)
        
    ''' <summary>Analyze user input, sets reminder and Returns note for user</summary>
        <return>str</return> '''
    def getAnswer(self, userInput):
        #self.setReminder(userInput, 6)
        userInput = filterUserInput(userInput)
        userAction = self.determineAction(userInput)
        
        if userAction == self.ACTION_NONE: # no action was detected, exiting...
            return self.pickRandom(self.DEFAULT_STRINGS)
        
        if userAction == self.ACTION_ADD:
            return self.actionAdd(userInput)
        elif userAction == self.ACTION_DEL:
            return self.pickRandom(self.DEFAULT_STRINGS)
        elif userAction == self.ACTION_SHOW:
            return self.pickRandom(self.DEFAULT_STRINGS)
    
    ''' <summary>chooses action to perform(add,del or show)</summary>
        <return>int</return>'''
    def determineAction(self, userInput):
        # extra case
        if str(userInput).startswith('remind'):
            return self.ACTION_ADD
        # other cases
        actionDict = self.getTags()
        for i in range(4): # i = 0, 1, 2
            for value in actionDict[i]:
                if value in userInput:
                    return i                                                                   
        return self.ACTION_NONE

''' <summary>preparing a string for analyses</summary>
    <return>str</return>'''
def filterUserInput(text):
    text = " ".join(text.split()) # replace(with space) multiple spaces, tabs and new lines
    text = text.lower()
    text = text.replace('!', '.')
    import string
    allowedChars = string.ascii_lowercase + string.digits + ' :.?'
    for letter in text: # removes not allower chars
        if not letter in allowedChars:
            text = text.replace(letter, '')
    return text
    
if __name__ == '__main__':
    r = Reminder()
    while True:
        userInput = input("\nEnter reminder text: ")
        print(r.getAnswer(userInput), '\n')