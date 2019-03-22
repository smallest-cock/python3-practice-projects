#!  /usr/bin/python3
# Madlibs.py - Reads Madlibs template from a text file, asks user to input appropriate
# words, then creates completed Madlib in new text file and prints results on screen
import re
import sys
import os

# creates regex values to be used for searching the madlibTempFile
regexTxt = re.compile(r'.txt$')
regexNoun = re.compile(r'NOUN')
regexAdjec = re.compile(r'ADJECTIVE')
regexVerb = re.compile(r'VERB')
regexAdverb = re.compile(r'ADVERB')

# checks to see if 2nd argument is a directory path, and is a text file
if len(sys.argv) < 2:
    print("Error: You didn't supply a directory path.")
    exit()
elif len(sys.argv) > 2:
    print('Error: Too many arguments.')
    exit()
elif os.path.isfile(sys.argv[1]) == True:
    if regexTxt.search(sys.argv[1]) == None:
        print("Error: That's not a text file")
        exit()
    else:
        madlibTempFile = open(sys.argv[1])
else:
    print("Error: That's not a file")
    exit()

# reads the madlibTempFile and stores number of items to be replaced in a variable (one variable per word type)
madlibTempString = madlibTempFile.read()
nounCount = len(regexNoun.findall(madlibTempString))
adjecCount = len(regexAdjec.findall(madlibTempString))
verbCount = len(regexVerb.findall(madlibTempString))
adverbCount = len(regexAdverb.findall(madlibTempString))

# gathers & organizes user input; puts words from user input into lists (One list per word type)
nouns = []
for i in range(nounCount):
    nouns.append(input('Enter a noun:  '))
adjectives = []
for i in range(adjecCount):
    adjectives.append(input('Enter an adjective:  '))
verbs = []
for i in range(verbCount):
    verbs.append(input('Enter a verb:  '))
adverbs = []
for i in range(adverbCount):
    adverbs.append(input('Enter an adverb:  '))

# copies content of madlibTempString to new variable newMadlibString
newMadlibString = madlibTempString

# replaces placeholder words in newMadlibString with appropriate words from user input
for noun in nouns:
    newMadlibString = regexNoun.sub(noun, newMadlibString, 1)
for adjective in adjectives:
    newMadlibString = regexAdjec.sub(adjective, newMadlibString, 1)
for adverb in adverbs:
    newMadlibString = regexAdverb.sub(adverb, newMadlibString, 1)
for verb in verbs:
    newMadlibString = regexVerb.sub(verb, newMadlibString, 1)


# creates new file named newMadlibFile.txt and writes content of newMadlibString to it
newMadlibFileDir = os.path.join(os.path.dirname(sys.argv[1]), 'NewMadlibFile.txt')
newMadlibFile = open(newMadlibFileDir, 'w')
newMadlibFile.write(newMadlibString)
newMadlibFile.close()

# prints the resulting newMadlibString
print('\n New madlib created in ' + newMadlibFileDir + ' :')
print('\n' + newMadlibString)


# TODO: add support for plural and past tense placeholders (e.g. NOUNS, PASTVERB, etc.)
