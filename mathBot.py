import math
def isNum(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

def checkOperator(operator):
    validOperators = ["+","-","*","/","%","**","//"]
    if operator in validOperators:
        return True
    else:
        return False

def checkRoot(userInp):
    validArgs = ["square root","squareroot","sqrt"]
    for x in validArgs:
        if x in userInp:
            return True
        else:
            return False
        
def checkDict(userInp):
        
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
    
    num = ""
    currentEval = 0
    eval = False
    
    def __init__(self, stringInp):
        print(stringInp)
        for i in range(len(stringInp)):
            
            current = stringInp[i]

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
            