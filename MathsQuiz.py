# Maths Quiz
#
#  Generates a maths quiz with 10 questions
#  consisting of addition subtraction multiplication
#  and division questions, each operator has
#  different parameters for the values to make
#  the questions reasonable
#
import random



difficulty = int()
difficultyQueue = []



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
        num1 = random.randint(1, 100 + difficulty)
        num2 = random.randint(1, 100 + difficulty)

    elif randnum == 1:
        operator = ("-")
        num1 = random.randint(1, 100 + difficulty)
        num2 = random.randint(1, 100 + difficulty)
        if num1 < num2:
            (num1, num2) = (num2, num1)
        #subtract

    elif randnum == 2:
        #times
        operator = ("*")
        num1 = random.randint(1, 12 + round(difficulty /3))
        num2 = random.randint(1, 12 + round(difficulty /3))

    elif randnum == 3:
        #divide
        operator = ("/")
        num2 = random.randint(1, 12 + round(difficulty /3))
        answer = random.randint(1, 12 + round(difficulty /3))
        num1 = num2 * answer
    questionString = str(num1, operator, num2)
    return questionString, answer


def runQuiz():
    difficulty = (0)
    correctCount = int(0)
    for questionNo in range(1, 11):

        genAnswer("Question", questionNo)
        (Question, answer) = getQuestion(difficulty)
        genAnswer(Question)
        userInput = getAnswer()

        if userInput.isnumeric():
            if userInput == answer:
                correctCount = (correctCount + 1)
        else:
            genAnswer("Answer must be a number")






class Quiz:
    __init__()
        runQuiz()