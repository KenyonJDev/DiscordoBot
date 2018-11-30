import random
from colorama import Fore  #Colors

def wordg(word, lettersGuessed):
    count=0
    for letters in word:
        if letters in lettersGuessed:
            count+=1
    if count==len(word):
        return True
    else:
        return False


def findwordg(word, lettersGuessed):
    temp=[]
    string=""
    for i in word:
        if i in lettersGuessed:
            string+=i
        else:
            string+="_ "
    return string


def lettersAvail(lettersGuessed):
    string=""
    count=0
    s='abcdefghijklmnopqrstuvwxyz'
    for letter in s:
        if letter in lettersGuessed:
            count+=1
        else:
            string+=letter
    return string
    

def game(word):
    length=len(word)
    print("The word has",length, "letters.")
    guesses=2*len(word)
    i=0
    lettersGuessed=[]
    while (guesses!=0):
        print("----------")
        if word!=findwordg(word, lettersGuessed):
            print("You have", guesses, "guesses left.")
            print("Available letters: ",lettersAvail(lettersGuessed))
            guess=input("Please guess a letter: ")
            guessInLowerCase = guess.lower()
            
            if guessInLowerCase  in lettersGuessed:
                print("Sory, letter already guessed: ",findwordg(word, lettersGuessed))
            
            elif guessInLowerCase not in word: 
                print(Fore.RED + "Letter not in this word:",findwordg(word, lettersGuessed))
                guesses-=1
            else:
                lettersGuessed.append(guessInLowerCase)
                print(Fore.GREEN + "Good guess: ",findwordg(word, lettersGuessed))
            lettersGuessed.append(guessInLowerCase)
            
        elif word==findwordg(word, lettersGuessed):
            print("Amazing, you've guessed the word!")
            break
    else:
        print("----------")
        print("You have no more guesses available. The word was "+word+".")
        


words=['computer', 'science', 'laptop', 'desktop', 'school', 'screen', 'python', 'coventry university']
r=random.randint(0,7)

        
word=(words[r])
game(word)