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
    ACTION_ADD = 0
    ACTION_DEL = 1
    ACTION_SHOW = 2
    
    def __init__(self):
        self.sched = sched.scheduler(time.time, time.sleep)
    
    ''' <summary>Gives tags which are used to detect user action</summary>
        <return>dict of {'str': list}</return>'''
    def getTags(self):
        d = {'create': ['set', 'create', 'make', 'send', 'message me'],
             'delete': ['remove', 'cancel', 'dont', 'do not', 'stop', 'delete'],
             'show': ['show', 'list'],
             'keywords': ['reminder', 'notification', 'write', 'alarm', 'remind', 'notif', 'recall']}
        return d
    
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
    
    # __________ public functions __________ #
    ''' <summary>It joins all tag sections to a list</summary>
        <return>list</return> '''
    def getKeywords(self):
        tag_dict = self.getTags()
        keyword_list = []
        for key in tag_dict:
            keyword_list += tag_dict[key]
        return keyword_list
    
    ''' <summary>Analyze user input, sets reminder and 
                 Returns note for user</summary>
        <return>str</return> '''
    def getAnswer(self, userInput):
        #self.setReminder(userInput, 6)
        
#         usr_action = -1
#         for key in self.getTags():
#             print(key)
        
        return "Sorry but I cannot set you a reminder!"
    
    
    
    