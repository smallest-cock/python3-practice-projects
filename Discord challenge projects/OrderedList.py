'''Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest) and
another number. The function decides whether or not the given number
is inside the list and returns (then prints) an appropriate boolean value.'''

list, num = [0, 1, 3, 8, 15, 26, 89, 949, 16518], 45


def isInTheList(orderedList, number):
    if number in orderedList:
        return True
    else:
        return False


print(isInTheList(list, num))
