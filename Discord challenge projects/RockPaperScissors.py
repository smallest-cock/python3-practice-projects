# RockPaperScissors.py - Simple rock paper scissors game. Greets player,
# then gives back messages after player won or lost.

from random import randint

rps = ['Rock', 'Paper', 'Scissors']

print('Hello there! Welcome to the Paper Scissors Rock game.')

while True:
    try:
        choice = input('\nEnter scissors, rock, or paper (s/r/p) or ENTER to quit:  ').lower()
        if choice == '':
            print('\nPeace nigga...')
            break
        randChoice = rps[randint(0, 2)]
        dict = {'s': 'Scissors', 'r': 'Rock', 'p': 'Paper'}
        outcome = "\n%s    vs    %s\n" % (randChoice, dict[choice])
        print('\n' + ' Result '.center(len(outcome), '='))
        print(outcome)
        if choice == 's':
            if randChoice == 'Rock':
                print('I just smashed your bitch ass! You lose...')
            elif randChoice == 'Paper':
                print('Ahhhhh! You cut me! You win...')
            else:
                print('Draw... You copied me.')
        elif choice == 'r':
            if randChoice == 'Paper':
                print('I wrapped you up like a mummy boi. You lose...')
            elif randChoice == 'Scissors':
                print('You broke my heart! You win...')
            else:
                print('Draw... You copied me.')
        elif choice == 'p':
            if randChoice == 'Scissors':
                print('I just cut you homie. You lose...')
            elif randChoice == 'Rock':
                print('You wrapped me up like sushi! You win...')
            else:
                print('Draw... You copied me.')
        elif choice == '':
            print('\nPeace nigga...')
            break
    except KeyError:
        print('\nWTF is that?! Enter "p", "r", or "s" dumbass.')
