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
            
            if current in "0123456789.":
                self.num = self.num + str(current)
                if (i != len(stringInp)-1 and stringInp[i+1] == ")") or i == len(stringInp)-1:
                    self.eval = True                   
            elif current in  "+-/*":
                self.num = self.num + str(current)
                
            if self.eval == True:
                self.currentEval = eval(self.num)
                self.eval = False      