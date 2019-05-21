'''Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order. For example, say I type the
string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.'''

string = input("Type a sentence:  ")

wordList = string.strip('.?!').split(' ')

backwardsList = []

for i in range(-1, (-len(wordList) - 1), -1):
    backwardsList.append(wordList[i])
print("\nYour sentence backwards:")
for word in backwardsList:
    print(word, end=' ')
