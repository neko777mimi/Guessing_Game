import json
import secrets
# file opens and closes file
# read reads the file
# RandoWordo is the random word the computer selects
# BlankSpace is the a list of _ 
# GameTime is full of _ as long as RandoWordo
# MakeAList is a list of '_' to make swapping ordered string values possible
# FindAddGuess is a function that responds to Guess by either adding Guess into the correct spot or returning the string as it was before
# Guess is the user's attempt at guessing RandoWordo
# NewGame is a function that allows the user to keep playing until they input a correct end string




# Header
print('Let\'s Play a Game!')


# open a file to select a word
file = open('words_alpha.txt')
read = file.read().splitlines()
file.close()


# selects a random word from file and makes it lower case
RandoWordo = secrets.choice(read)
RandoWordo = RandoWordo.lower()


# Uses an empty list to make a string of blankspaces
BlankSpace = []
for t in RandoWordo:
    BlankSpace.append('_')
GameTime = ''.join(BlankSpace)



#Turns GameTime into a list to allow for the swapping of items
MakeAList = list(GameTime)


# function to match Guess to i in RandoWordo and swap if there is an existence
x = 0
def FindAddGuess(Guess):
    for i in range(len(MakeAList)):
        if MakeAList[i] == '_' and  RandoWordo[i] == Guess:
            MakeAList[i] = Guess
            GameTime = ''.join(MakeAList)
        else:
            GameTime = ''.join(MakeAList)
    return(GameTime)
    


# Allows 7 guesses, Have the user guess letter or string, Check if the string is str vs int, str is made lower case, Check if letter exists in RandoWordo
# if the string is exactly 1 value long, FindAddGuess occurs
# if the string is greater than 1 value long, but not as long as the word, has user try again
def Game():
    print(f'This is your word: {GameTime}. It\'s guessing time!')
    x = 0
    while (x < 7 and '_' in MakeAList):
        Guess = input(f'Guess a letter or the entire word if you can! Go on now: ')
        Guess = Guess.lower()
        if len(Guess) == 1:
                # Check that string does not contain integer
            if Guess.isdigit() == 1:
                print('No thank you. We both know numbers do not exist in words.')
            else:
                print(FindAddGuess(Guess))


        elif len(Guess) > len(GameTime) or (len(Guess) > 1 and len(Guess) < len(GameTime)):
            print('Please check the length and try again.')


        elif Guess == RandoWordo:
            print(f'{RandoWordo}\n You\'re done kiddo! You guessed the word!')
            break
        x = x + 1
Game()
print('Good game right?!')


#recreates the game to allow the user a never ending fun experience
def NewGame():
    for s in read:
        NewGame = (input('Wanna play again? '))
        NewGame = NewGame.lower()
        if NewGame == 'y' or NewGame == 'yes' or NewGame == 'yass':
            Game()
        else:
            print('Thanks for playing!')
            break

NewGame()