'''Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.
[Extra: Randomly generate two lists to test this]'''

from random import randint

listA, listB = [], []


# fills list with random numbers

def generateRandom(list):
    for i in range(randint(8, 15)):
        list.append(randint(0, 50))


# finds the common elements between two lists and returns those elements in a list

def compare(list1, list2):
    commonItems = []
    for item in list1:
        if item in list2 and item not in commonItems:
            commonItems.append(item)
    return commonItems


generateRandom(listA)
generateRandom(listB)
print(listA)
print(listB)
print(compare(listA, listB))
