import random
possibilities = {0: 'heads', 1: 'tails'}
guess = ''
while guess not in possibilities.values():
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# 'toss == guess' was never gonna be true, bc toss is an int (0 or 1) and guess is a string (heads or tails)
if possibilities[toss] == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()    # guess was incorrectly spelled 'guesss'
    if possibilities[toss] == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
