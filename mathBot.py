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
    validArgs = ["square root","sqrt","squared"]
    for x in validArgs:
        if x in userInp:
            return True
        else:
            return False
    
class isMath():
    
    num = ""
    start = 0
    currentEval = 0
    eval = False
    
    def __init__(self, stringInp):
        for i in range(len(stringInp)):
            current = stringInp[i]

            if current == "(":
                self.eval = False
                continue  
            elif current in "0123456789.+-/*":
                self.num = str(self.num) + str(current)
                if (i == len(stringInp)-1 or i != len(stringInp)-1 and stringInp[i+1] == ")"):
                    self.eval = True            
            
            if self.eval == True:
                if "square root" in stringInp or "sqrt" in stringInp:
                    self.currentEval = math.sqrt(float(self.num))
                else:
                    self.currentEval = eval(self.num)
                self.num = self.currentEval
                self.eval = False                
                