'''   Hangman Game:
The Goal: Despite the name, the actual “hangman” part isn’t necessary.
The main goal here is to create a sort of “guess the word” game.
The user needs to be able to input letter guesses.
A limit should also be set on how many guesses they can use.
This means you’ll need a way to grab a word to use for guessing.
(This can be grabbed from a pre-made list. No need to get too fancy.)
You will also need functions to check if the user has actually inputted a single letter,
to check if the inputted letter is in the hidden word (and if it is, how many times it appears),
 to print letters, and a counter variable to limit guesses. '''

import random

wordList = ['frog', 'poop', 'mushroom', 'elephant', 'needle',
            'corndog', 'shark', 'cabinet', 'organism', 'meteorite',
            'glue', 'pig', 'avocado', 'cherry', 'light', 'exercise',
            'unique', 'phallus']
guessedList = []

# determines the word to be guessed, and total amount of guesses allowed
randWord = wordList[random.randint(0, len(wordList))]
totalGuesses = (len(randWord) + 5)  # replace 5 with higher or lower number to change difficulty
guessesLeft = totalGuesses


# function to check whether or not user input is a letter (retuns True or False accordingly)


def letterCheck(letter):
    if letter.isalpha() is True and len(letter) == 1:
        return True
    else:
        return False


# function to check whether or not user has won the game (retuns True or False accordingly)


def winCheck(word, triedList):
    for i in word:
        if i in triedList:
            continue
        else:
            return False
        return True


# starts the game by printing underscores for every letter in the word
print('Try to guess this word:\n')
for i in range(len(randWord)):
    print('_ ', end='')

# prompts user to pick a letter, and determines if that letter is in the secret word
# if it is, prints the guessed letters that are in the secret word along with underscores;
# otherwise, deducts 1 from guessesLeft
while guessesLeft > 0 and winCheck(randWord, guessedList) is False:
    print(' ')
    guess = input('\nPick a letter:  ').lower()
    if letterCheck(guess) is False:
        print('\nThat\'s not a letter :(')
        continue
    guessedList.append(guess)
    print(' ')
    if guess in randWord:
        for i in randWord:
            if i == guess or i in guessedList:
                print(i + ' ', end='')
            else:
                print('_ ', end='')
    else:
        guessesLeft -= 1
        if guessesLeft > 1:
            print('Nope... You have %s wrong guesses left.\n' % (str(guessesLeft)))
        else:
            print('Nope... You\'re on your last guess!!!\n')
        for i in randWord:
            if i in guessedList:
                print(i + ' ', end='')
            else:
                print('_ ', end='')

# displays appropriate message if user won or lost the game
if guessesLeft == 0 and winCheck(randWord, guessedList) is False:
    print('\n\nYou guessed wrong %s times... you lose :(' % (str(totalGuesses)))
else:
    print('\n\nCongratulations! You win :)')
