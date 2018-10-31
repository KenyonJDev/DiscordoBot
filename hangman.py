import random
from colorama import Fore  #Colors

def isWordGuessed(secretWord, lettersGuessed):
    count=0
    for letters in secretWord:
        if letters in lettersGuessed:
            count+=1
    if count==len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    temp=[]
    string=""
    for key in secretWord:
        if key in lettersGuessed:
            string+=key
        else:
            string+="_ "
    return string


def getAvailableLetters(lettersGuessed):
    string=""
    count=0
    s='abcdefghijklmnopqrstuvwxyz'
    for letter in s:
        if letter in lettersGuessed:
            count+=1
        else:
            string+=letter
    return string
    

def hangman(secretWord):
    length=len(secretWord)
    print("Welcome to Hangman!")
    print("The word has",length, "letters.")
    chances=2*len(secretWord)
    i=0
    lettersGuessed=[]
    while (chances!=0):
        print("-----------")
        if secretWord!=getGuessedWord(secretWord, lettersGuessed):
            print("You have", chances, "guesses left.")
            print("Available letters: ",getAvailableLetters(lettersGuessed))
            guess=input("Please guess a letter: ")
            guessInLowerCase = guess.lower()
            
            if guessInLowerCase  in lettersGuessed:
                print("Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed))
            
            elif guessInLowerCase not in secretWord: 
                print(Fore.RED + "Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed))
                chances-=1
            else:
                lettersGuessed.append(guessInLowerCase)
                print(Fore.GREEN + "Good guess: ",getGuessedWord(secretWord, lettersGuessed))
                #chances+=1
            lettersGuessed.append(guessInLowerCase)
        elif secretWord==getGuessedWord(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
    else:
        print("-----------")
        print("Sorry, you ran out of guesses. The word was "+secretWord+".")
        


list=['phillip', 'armandas', 'josh', 'testing', 'test', 'letter', 'help', 'school']
r=random.randint(0,7)

        
secretWord=(list[r])
hangman(secretWord)