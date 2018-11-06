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
#  Code taken from: https://www.pythoncentral.io/use-queue-beginners-guide/
#
#
class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self,data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0,data)
          return True
      return False

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)

  #printing the elements of the queue
  def printQueue(self):
      return self.queue


#  /\
#

difficulty = int()
difficultyQueue = Queue()



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
    difficulty = (0)
    for questionNo in range(1, 11):
        correctCount = int(0)
        print("Question", questionNo)
        Question, answer = getQuestion(difficulty)
        print(Question)
        userInput = input(">")

        if userInput.isnumeric() == True:
            if userInput == answer:
                correctCount = (correctCount + 1)
        else:
            print("Answer must be a number")



#  will store average of last 10 scores
#  used to alter the base difficulty
#  takes 7/10 as a pass, less decreases the difficulty, more increases it
#
def difficultyModifier(score):

    difficulty =





























