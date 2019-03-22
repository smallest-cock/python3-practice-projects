''' create a "Guess the Number' program. It needs to welcome the player and then
ask for a number between 1-50 if the user is too low tell them it's too low, if
it's too high tell them too high. If they get the right number congratulate them
and then have it ask whether or not if the want to play again. '''

from random import randint
import sys


def numCheck(number):
    global guessCount
    global randNum
    global won
    if number == randNum:
        print('\nCongratulations! %s is the correct number :)' % number)
        won = True
    elif number < randNum:
        print('Nope. Too low...')
        guessCount -= 1
    elif number > randNum:
        print('Nope. Too high...')
        guessCount -= 1


print('Hi! Welcome to my number guessing game.\nI have chosen a secret number between 1 and 50, and you must guess it.')
print('You get 8 tries.')
guessCount = 7
wantsToPlay = True
while wantsToPlay is True:
    guessCount = 8
    won = False
    randNum = randint(1, 50)
    while won is False and guessCount > 0:
        try:
            guess = input('\nGuess the number (or ENTER to exit):  ')
            if guess == '':
                print('\nGoodbye...')
                sys.exit()
            numCheck(int(guess))
        except ValueError:
            print('That\'s not a number dumbass.')
    if guessCount == 0:
        print('\nYou couldn\'t guess it in 8 tries.. You\'re a bum.')
    choice = input('\nDo you wanna play again? (y/n):  ')
    if choice.lower() == 'y':
        continue
    elif choice.lower() == 'n':
        print('\nAight peace...')
        wantsToPlay = False
    else:
        print('\nI assume that means no. Peace...')
        wantsToPlay = False
