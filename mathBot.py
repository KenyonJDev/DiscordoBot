import math
def isNum(item):
    
    """Check if the argument passed is a number"""
    
    try:
        int(item)
        return True
    except ValueError:
        return False

def checkOperator(operator):
    
    """Check if the argument is an operator by comparing
    to a list of valid operators"""
    
    validOperators = ["+","-","*","/","%","**","//"]
    if operator in validOperators:
        return True
    else:
        return False

def checkRoot(userInp):
    
    """Check if any English variations of asking for 
    the square root have been entered"""
    
    validArgs = ["square root","squareroot","sqrt"]
    for x in validArgs:
        if x in userInp:
            return True
        else:
            return False
        
def checkDict(userInp):
    
        """Replace any English words for operators with the python
        symbol for that given operator using the dictionary mathDict"""
        
        mathDict = {
            "to the power of":"**",
            "divided by":"/",
            "over":"/",
            "x":"*",
            "times by":"*",
            "times":"*",
            "multiplied by":"*",
            "plus":"+",
            "add":"+",
            "minus":"-",
            "take away":"-",
            "modulus":"%",
            "mod":"%",
            "modulo":"%"            
        }
        
        for key in mathDict:
            if key in userInp:
                userInp = userInp.replace(key,mathDict[key])  
        return userInp
            
        
    
class isMath():
    
    """A class to instatiate an object of the message 
    input by the user if is it a math question"""
    
    num = ""
    currentEval = 0
    eval = False
    
    def __init__(self, stringInp):
        
        """Goes through the string input and checking for open and closed brackets,
        when the bracket is open the characters are appened to a variable until a closed
        bracket or the end of the sequence. Anything appended is evaluated."""
        
        for i in range(len(stringInp)):    
            current = stringInp[i]
            #Checks if the current character is a number or operator
            if current == "(":
                self.eval = False
                continue  
            elif current in "0123456789.+-/*%":
                self.num = str(self.num) + str(current)
                if current == "/" and stringInp[i + 1] == "0":
                    self.currentEval = "Cannot perform that calculation!"
                    break;
                elif (i == len(stringInp)-1 or i != len(stringInp)-1 and stringInp[i+1] == ")"):
                    self.eval = True            
                    
            if self.eval == True:
                if "square root" in stringInp or "sqrt" in stringInp:
                    self.currentEval = math.sqrt(float(self.num))
                else:
                    self.currentEval = eval(self.num)
                self.num = self.currentEval
                self.eval = False 
                
        
            self.currentEval = 'The answer is {}'.format(self.currentEval)
            