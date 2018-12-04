''' ----- USAGE explanation -----
    from reminder import Reminder
    def onNotification(sender, message):
        print(message)    

    # create reminder object
    rmndr = Reminder()
    # add function to execute
    rmndr.listener += onNotification
    # analyse user string and set reminder with this function
    rmndr.getAnswer('User string')

    # manually set reminder {args(text, secondsToWait)}
    rmndr.setReminder('This is my message', 8)
'''

# event-driven programming. Read wikipedia to know how it works
import event # copyright explained in event.py file
# ------------------------
import datetime # system date
import sched, time # delay commands AND system time
import _thread
import re # regular expressions standart library
import traceback # used for debugging exeptions
from pyfcm import FCMNotification # google firebase cloud messaging library

class Reminder():
    listener = event.Event() # functions list to invoke
    listenerEnabled = False # if false then use android app notification
    
    # ENUM used as dictionary key in getTags() function:
    ACTION_NONE = -1
    ACTION_ADD = 0
    ACTION_DEL = 1 
    ACTION_SHOW = 2
    KEYWORDS = 3
    MESSAGE_IDENT = 4 # message identificators
    TIME_IDENT = 5 # time identificators
    
    # ENUM used as dictionary key to get time regexes:
    AFTER = 0 # i.e. 'after 1hour 5 minutes'
    OCLOCK = 1 # i.e. 5 o`clock or 5 oclock
    DEFAULT_TIME = 2 # i.e. 15.25 or 15:25
    AMPM_TIME = 3 # i.e. 5am 11pm
    
    REGEXES = {AFTER: '(\d{1,2} *((seconds?)|(minutes?)|(hours?)))',
               OCLOCK: '(\d{1,2} *[oO]?(clock))',
               DEFAULT_TIME: '(([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)',
               AMPM_TIME: '([0-1]?\d([:.][0-5]\d)? *[aApP]\.?[mM]\.?)',
               MESSAGE_IDENT: '(( with (a|the)? ?(message|text) (of|to) )|( (to|that|I have) ))'}
    DEFAULT_STRINGS = ['Hmm, can you give me more details?', 
                       'Sorry, I cannot set you a reminder! Can you be more precise?', 
                       'I missunderstand :(. Can you explain in a different way?']
    
    def __init__(self, enableListener=False):
        self.sched = sched.scheduler(time.time, time.sleep)
        self.listenerEnabled = enableListener
    
    ''' <summary>Gives tags which are used to detect user action</summary>
        <return>dict of {'str': list}</return>'''
    def getTags(self):
        d = {self.ACTION_ADD: ['set', 'create', 'make', 'send', 'message me', 'type', 'write'],
             self.ACTION_DEL: ['remove', 'cancel', 'dont', 'do not', 'stop', 'delete'],
             self.ACTION_SHOW: ['what', 'when', 'show', 'list'],
             self.KEYWORDS: ['reminder', 'notification', 'write', 'alarm', 
                             'remind', 'notif', 'recall', 'note'],
             self.MESSAGE_IDENT: [' with message to ', ' with message of ', 
                                  ' with the message of ', ' with a message of ', 
                                  ' with text of ', ' to ', ':', ' that ', ' I have '],
             self.TIME_IDENT: [' at ', ' after ', ' in '] }
        return d
    
    ''' <summary>Picks random value in a list</summary>'''
    def pickRandom(self, _list):
        import random
        return _list[random.randint(0, len(_list)) - 1]
    
    ''' <summary>Function to be threaded</summary>'''
    def reminderThread(self, text, delayInSec):
        self.sched.enter(delayInSec, 1, self.invokeListener, (text, ))
        self.sched.run()
    
    ''' <summary>Sets a timer for invokation</summary>'''
    def setReminder(self, text, delayInSec):
        # threads are used because 'sched' library delay main program flow
        _thread.start_new_thread(self.reminderThread, (text, delayInSec) )
    
    ''' <summary>Notifies caller class to pull reminder</summary> '''
    def invokeListener(self, text):
        device_token = "fQg_YPhiS-c:APA91bGgxjJJvwwSR8r5zFdN-qyerR5gP5aa1g-E0yqLumV56ZOuubAcNyJCIOeF_0rEvk9BCAN2WqgNkB23kxACP6AFD1c5ON0jMaJanV1JXzvgR7gNA0sn3rlW1WQPUmO_cqv7xT76"
        key = "AAAA-PO7Lds:APA91bEkn-rmOegVXChsx0MAxKy0N9JCy6-S7NtSa3cp6uiPFz150zRMijet-3VrWjw_GKxxHnKuBvJ6D5-j7Krjhb6aWTq9avgaSS-SldbdrNT4WyAMh6AoXWqfg5L-3IV1le8IkMM_"
        if self.listenerEnabled:
            self.listener(text)
        else: # send android notification through google firebase
            notificationService = FCMNotification(api_key=key)
            notificationService.notify_single_device(registration_id=device_token, message_title=text, message_body='Discord Reminder')
    
    ''' <summary>Gives keywords used to identify if it's associated with reminder</summary>
        <return>list of strings</return> '''
    def getKeywords(self):
        return self.getTags()[self.KEYWORDS]
    
    ''' <summary>Checks if input is associated with module</summary>
        <return>boolean</return> '''
    def check(self, userInput):
        userInput = userInput.lower()
        kwList = self.getKeywords()
        for kw in kwList: # tries to find at least 1 keyword
            if kw in userInput:
                return True
        return False
    
    ''' <summary>extracts time str part from input</summary>
        <return>str(time part) or list of strings, and (ENUM)time type</return>'''
    def detectTime(self, text):
        for i in range(4):
            regex = re.findall(self.REGEXES[i], text)
            if regex: # match found
                if i == self.AFTER:
                    # i.e. str(5minutes 6 seconds) gets splited into list of 2 elements
                    newList = []
                    for match in regex: 
                        newList.append(match[0])
                    return newList, i
                else:
                    return regex[0][0], i
        return None
    
    ''' <summary>extracts reminder text from input</summary>
        <return>str(user note)</return>'''
    def detectMessage(self, text):
        regexTime = re.findall('( (at|after|in) )', text)
        regexMsg = re.findall(self.REGEXES[self.MESSAGE_IDENT], text)
        
        if regexMsg and regexTime: # match found
            ident_msg = regexMsg[0][0] # message identicative string
            ident_time = regexTime[0][0] # time identicative string
            if text.find(ident_time) > text.find(ident_msg): # message is typed first then time
                _returnText = text[text.find(ident_msg) + len(ident_msg) : text.find(ident_time)]
                return _returnText[0].upper() + _returnText[1:] # capitalize first letter
            else:
                _returnText = text[text.find(ident_msg) + len(ident_msg) :]
                return _returnText[0].upper() + _returnText[1:] # capitalize first letter
        else:
            return None
                
    ''' <summary>Finds first number in string</summary>
        <return>int</return>'''
    def findIntInString(self, string):
        regex = re.search(r'\d+', string)
        if regex != None:
            return int(regex.group()) 
        else:
            return None
    
    ''' <summary>convert time string to seconds left for event to fire</summary>
        <note>recursive calls are used to reduce redundancy</note>
        <param name="timeTuple">[0]: contains time string, [1]: (ENUM-int)time format</param>
        <return>int(delay in seconds)</return>'''
    def calculateDelay(self, timeTuple):
        totalSeconds = 0
        if timeTuple[1] == self.AFTER:
            for timePiece in timeTuple[0]: # iterates hour, min, sec
                num = self.findIntInString(timePiece)
                if num == None:
                    return None
                if 'hour' in timePiece:                   
                    totalSeconds += 3600 * num
                elif 'min' in timePiece:
                    totalSeconds += 60 * num
                elif 'sec' in timePiece:
                    totalSeconds += num
            return totalSeconds
        elif timeTuple[1] == self.OCLOCK:
            num = self.findIntInString(timeTuple[0])
            if not(num >= 1 and num <= 12): # if non sence time, return Error
                return None
            if num == 12:
                return self.calculateDelay(("12:00", self.DEFAULT_TIME)) # recursive call for 24 format time
            else:
                now = datetime.datetime.now() # current system time
                if num > now.hour: # ie. hour: now = 9:00, given = 11oclock then counts as morning 
                    return self.calculateDelay((str(num) + ':00', self.DEFAULT_TIME)) # recursional call for 24 format time
                else:
                    return self.calculateDelay((str(num + 12) + ':00', 2)) # recursive call for 24 format time
        elif timeTuple[1] == self.DEFAULT_TIME:
            # i.e. time str "12:34" becomes list ['12', '34']
            nums = list(map(int, re.findall(r'\d+', timeTuple[0]))) 
            if len(nums) != 2: 
                return None # something went wrong
            now = datetime.datetime.now() # current system time
            nowSeconds = now.hour * 3600 + now.minute * 60 # realtime day seconds count
            givenSeconds = nums[0] * 3600 + nums[1] * 60
            nowSysSec = int(round(time.time())) # seconds past after 1 January 1970
            day = now.day
            if nowSeconds >= givenSeconds: # ie. now 16:56, given time 13:12. Shifts reminder to next day
                day = now.day + 1
            givenInSysSec = int(time.mktime(datetime.datetime(now.year, now.month, day, nums[0], nums[1]).timetuple()))
            return givenInSysSec - nowSysSec
        elif timeTuple[1] == self.AMPM_TIME:
            # time string is trusted of am pm because regex already filtered it
            # until this point. So i check for 'a' rather than 'AM'
            isAM = 'a' in timeTuple[0].lower()
            num = self.findIntInString(timeTuple[0]) # find number(hour)
            if not(num >= 1 and num <= 12):
                return None
            if isAM and num == 12:
                num = 0 # in other am cases num is the same so I dont change it
            # if num = 12 then it is right so I dont need to change it
            if not isAM and num != 12: # means isPM
                num += 12
            return self.calculateDelay((str(num) + ":00", self.DEFAULT_TIME)) # recursive call for 24 format time
        return None # it case of error
    
    def actionAdd(self, userInput):
        try:
            time = self.detectTime(userInput) # finds str part of time from input
            message = self.detectMessage(userInput) # finds reminder message
            delaySec = self.calculateDelay(time) # calculates DELAY in seconds after which raises reminder
            if message == None or delaySec == None: # on failure-escape case
                return self.pickRandom(self.DEFAULT_STRINGS) 
            if delaySec != None: # if successful
                self.setReminder('Reminder: ' + str(message), int(delaySec))
                prefixStrs = ['Ofcourse', 'No worries', 'Yup buddy', 'Sure mate']
                if time[1] == self.AFTER:
                    return '{} ;)! I set you a reminder after {} with note: {}'.format(self.pickRandom(prefixStrs), time[0], message)
                else:
                    return '{} ;)! I set you a reminder at {} with note: {}'.format(self.pickRandom(prefixStrs), time[0], message)
            else:
                raise Exception('Time string was not converted!')
        except:
            traceback.print_exc() # console debugging
            return self.pickRandom(self.DEFAULT_STRINGS)
        
    ''' <summary>Analyze user input, sets reminder and Returns note for user</summary>
        <return>str</return> '''
    def getAnswer(self, userInput):
        #self.setReminder(userInput, 6)
        userInput = filterUserInput(userInput) # deletes unnecessarily punctuation, lower case all letters
        
        # at this moment only ADD function is enable/developed
        userAction = self.determineAction(userInput) # what user wants to do. Add, remove, get list of reminders
        
        if userAction == self.ACTION_ADD: # setting reminder
            return self.actionAdd(userInput)
        else: # unable to do user requested action
            return self.pickRandom(self.DEFAULT_STRINGS) 
    
    ''' <summary>chooses action to perform(add,del or show)</summary>
        <return>int</return>'''
    def determineAction(self, userInput):
        # extra case
        if str(userInput).startswith('remind'):
            return self.ACTION_ADD
        # other cases
        actionDict = self.getTags()
        # searh for matches in dictionary of lists
        # return i - which is ENUM action(defined above)
        for i in range(4): # i = 0, 1, 2
            for value in actionDict[i]:
                if value in userInput:
                    return i                                                                   
        return self.ACTION_NONE # default case

''' <summary>preparing a string for analyses</summary>
    <return>str</return>'''
def filterUserInput(text):
    text = text.replace(',', ' ') # removes commas
    text = " ".join(text.split()) # replace(with space) multiple spaces, tabs and new lines
    text = text.lower()
    text = text.replace('!', '.') # ! becomes .
    import string
    allowedChars = string.ascii_lowercase + string.digits + ' :.?'
    for letter in text: # removes not allowed chars
        if not letter in allowedChars:
            text = text.replace(letter, '')
    # exeption with 'I have' -> replaces to 'that I have'
    iHavePos = text.find('i have')
    if iHavePos != -1:
        text = text[:iHavePos] + 'that ' + text[iHavePos:]
    # ______________________________________
    return text

# Console chat version
if __name__ == '__main__':
    r = Reminder()
    while True:
        userInput = input("\nEnter reminder text: ")
        print(r.getAnswer(userInput), '\n')
        