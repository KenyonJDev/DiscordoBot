userInp = "What is 2 / 2"
stringArr = userInp.split(" ")
validOperators = ["+","-","*","/","%","**","//"]

start = 0
calc = ""

def isNum(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

def checkOperator(operator):
    if operator in validOperators:
        return True
    else:
        return False

for i in range(0,len(stringArr)):
    if (isNum(stringArr[i])):
        start = i
        break;

for j in range(start + 1, len(stringArr)):
    if (isNum(stringArr[j]) == False and checkOperator(stringArr[j])) == False or (j == len(stringArr)):
        calc = calc.join(stringArr[start:j + 1])

print(eval(calc))
