import sched, time
s = sched.scheduler(time.time, time.sleep)

def print_time(stt):
    print("From print_time", stt, time.time())
    
def print_some_times():
    print(time.time())
    global s
    s.enter(5, 1, print_time, ("stt",))
    s.enter(10, 1, print_time, ("stt",))
    s.run()
    print(time.time())
    
print_some_times()
    
    
class Reminder:
    
    def __init__(self, userString):
        self.userStr = userString
        self.isSet = False
        
    def setNotification():
        pass
    
    def getStatus():
        return self.isSet
    
    def getKeywords():
        # returns all associatedWords
        mKeywords = ['set', 'reminder', 'message me', 'notification', 
                     'notify me', 'send notification']
        return mKeywords