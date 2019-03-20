''' Calculate the number of BTUs required to make a symmetrically shaped room 72°F.
Prompt for the room's length, height, and width in feet, and for the current temperature in the room.
Display the number of BTUs required to heat or cool the room.  Be sure to indicate if the room needs
to be heated or cooled.  It takes .025 BTUs to cool or heat 1 cubit foot 1°F.
Round to the nearest Integer.'''

# gathers user input, stores values as ints in appropriate variables
length = int(input('Enter length of the room (in feet):  '))
height = int(input('Enter height of the room (in feet):  '))
width = int(input('Enter width of the room (in feet):  '))
temp = int(input('Enter the temperature of the room (in °F):  '))

# Calculates number of BTUs required to change temp to 72°F
volume = length * width * height
change1Degree = .025 * volume
btus = round(change1Degree * (72 - temp))  # 'btus' will be negative if room needs cooling

# prints appropriate answer to user based on the value of 'btus'
if btus > 0:
    print('\nYou need ' + str(btus) + ' BTUs to heat the room to 72°F.')
elif btus < 0:
    print('\nYou need ' + str(0 - btus) + ' BTUs to cool the room to 72°F.')
else:
    print('\nThe room is already at 72°F.')
