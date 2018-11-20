import math
    
class isMath():
    
    """A class to instatiate an object of the message 
    input by the user if is it a math question"""
    
    num = ""
    currentEval = 0
    eval = False
    
    #Flags to decide if the question is a math one
    numCheck = False
    opCheck = False
    rootCheck = False
    
    mathQ = False
    
    def __init__(self, stringInp):
        """Manipulate user input as string to check if it follows the pattern of a math question"""

        #Change english to operators and overwrite the input 
        stringInp = self.checkDict(stringInp)

        #Loop through string, check if both and operator and number are included or there is a square root using mathBot
        for i in range(len(stringInp)):
            if (self.isNum(stringInp[i])):
                self.numCheck = True
            elif (self.checkOperator(stringInp[i])):
                self.opCheck = True
            elif (self.checkRoot(stringInp)):
                self.rootCheck = True

        #If both operator and number are included or there is a square root then run calculate from mathBot
        if (self.numCheck == True and self.opCheck == True) or self.rootCheck:
            self.mathQ = True
            self.getAns(stringInp)
            
        
    def getAns(self, stringInp):
        
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
                    if int(self.num) < 0:
                        self.currentEval = "Cannot perform that calculation!"
                        break;
                    else:
                        self.currentEval = math.sqrt(float(self.num))
                else:
                    self.currentEval = eval(self.num)
                self.num = self.currentEval
                self.eval = False 
                
        
            self.currentEval = 'The answer is {}'.format(self.currentEval)
            
    def isNum(self, item):
    
        """Check if the argument passed is a number, 
        input can be of any type and output will be a boolean"""

        try:
            int(item)
            return True
        except ValueError:
            return False

    def checkOperator(self, operator):

        """Check if the argument is an operator by comparing
        to a list of valid operators, input is a string and output is a boolean"""

        validOperators = ["+","-","*","/","%","**","//"]
        if operator in validOperators:
            return True
        else:
            return False

    def checkRoot(self, userInp):
    
        """Check if any English variations of asking for 
        the square root have been entered, takes thse user input as a string 
        and returns a boolean"""

        validArgs = ["square root","squareroot","sqrt"]
        for x in validArgs:
            if x in userInp:
                return True
            else:
                return False
        
    def checkDict(self, userInp):
    
        """Replace any English words for operators with the python
        symbol for that given operator using the dictionary mathDict
        user input is a string and the output is a string of the new userInp variable"""
        
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
        
        #Checks every key in the dictionary to see if it is in the user input
        #and replaces any found with python equivalent
        for key in mathDict:
            if key in userInp:
                userInp = userInp.replace(key,mathDict[key])  
        return userInp