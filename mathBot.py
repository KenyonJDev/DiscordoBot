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
    
def calculate(stringArr):
    start = 0
    calc = ""
    
    for i in range(0,len(stringArr)):
        if (isNum(stringArr[i])):
            start = i
            break;

    for j in range(start + 1, len(stringArr)):
        if (isNum(stringArr[j]) == False and checkOperator(stringArr[j])) == False or (j == len(stringArr)):
            calc = calc.join(stringArr[start:j + 1])

    return(eval(calc))
