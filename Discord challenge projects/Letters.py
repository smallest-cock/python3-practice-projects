# /usr/bin/python3 python3
# Letters.py - Takes two letters from input. If the first letter comes before the second letter alphabetically,
# then displays all the letters between them in proper order.  Otherwise, displays them in reverse order.

# defines function that checks to see if a string is one letter, and exits if not
def lettercheck(letter):
    if letter.isalpha():
        if len(letter) > 1:
            print("\nError: That's more than one letter..\n")
            raise SystemExit
    else:
        print("\nError: That's not a letter..\n")
        raise SystemExit

# alphabet as a list
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

# Makes sure user enters valid letters, exits otherwise
num1 = input('Enter a letter:  ')
lettercheck(num1)
num2 = input('Enter a different letter:  ')
lettercheck(num2)

# converts user input into uppercase letters to be used with alphabet list
index1 = alphabet.index(num1.upper())
index2 = alphabet.index(num2.upper())

# prints appropriate sequence of letters based on user input
if index1 < index2:
    for i in range(index1, (index2 + 1)):
        print(alphabet[i], end= '')
    print(' ')
elif index1 > index2:
    for i in range(index1, (index2 - 1), -1):
        print(alphabet[i], end= '')
    print(' ')
else:
    print('\nThat\'s the same letter :(')
