# Maths Quiz
#
#  Generates a maths quiz with 10 questions
#  consisting of addition subtraction multiplication
#  and division questions, each operator has
#  different parameters for the values to make
#  the questions reasonable
#
import random


#
#  Generates the values for one question
#  returns a question as a string and the answer as an integer
#
def getQuestion():


    #
    #  Randomly selects an operator
    #
    randnum = random.randint(0, 3)
    operator = ""
    num1 = int()
    num2 = int()
    answer = int()

    #
    #
    #
    if randnum == 0:
        operator = ("+")
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

    elif randnum == 1:
        operator = ("-")
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        if num1 < num2:
            (num1, num2) = (num2, num1)
        #subtract

    elif randnum == 2:
        #times
        operator = ("*")
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)

    elif randnum == 3:
        #divide
        operator = ("/")
        num2 = random.randint(1, 12)
        answer = random.randint(1, 12)
        num1 = num2 * answer
    questionString = string(num1, operator, num2)
    return questionString, answer

def runQuiz():
    for questionNo in range(1, 11):
        correctCount = int(0)
        print("Question", questionNo)
        Question, answer = getQuestion()
        print(Question)
        userInput = input(">")

        if userInput.isnumeric() == True:
            if userInput == answer:
                correctCount = (correctCount + 1)
        else:
            print("Answer must be a number")


























