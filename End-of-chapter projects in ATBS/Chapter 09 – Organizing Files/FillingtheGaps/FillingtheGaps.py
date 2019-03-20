#! /usr/bin/python3
# FillingtheGaps.py - Finds all files with a given prefix, such as spam001.txt, spam002.txt,
# and so on, in a single folder and locates any gaps in the numbering
# (e.g. spam001.txt and spam003.txt, but no spam002.txt). Renames all the later files to close this gap.

import os, re, shutil

# Prompts user for the directory path that contains the numbered files, then stores that path in a variable.
# Then stores list of filenames in that directory in a variable (fileList)
directory = (input('Enter the directory that contains the numbered files:  ')).strip("'")
if not os.path.isdir(directory):
    print('Error: That isn\'t a valid directory')
    exit()
fileList = os.listdir(directory)

# Prompts user for the prefix of the numbered files, then uses that prefix to create a regex.
# Then stores the list of filenames (from fileList) that match the regex in a variable (matchedFiles)
prefix = input('Enter the prefix for the numbered files (what comes before the numbers):  ')
prefixRegex = re.compile(prefix + r'\s?\(?\d+\)?.\w+')
matchedFiles = prefixRegex.findall(str(fileList))

# adds a correct number to the beginning of every filename from matchedFiles, and appends them to new list (sortList)
# (only corrects for wrong numbers that are up to 100*(rhe number of files in matchedFiles))
sortList = []
for i in range(len(matchedFiles) * 100):
    matchNotFound = True
    for filename in matchedFiles:
        fileRegex = re.compile(prefix + r'\s?\(?0*' + str(i + 1) + r'\)?.\w+')
        if fileRegex.search(filename) != None:
            sortList.append(str(i + 1) + '_' + filename)

# uses the correct number at the beginning of every filename in sortList to make a new list (orderedList)
# with the filenames in ascending order (and also stips the correct number that was attatched previously)
orderedList = []
for i in range(len(sortList) * 100):
    for file in sortList:
        if file.startswith(str(i + 1) + '_'):
            orderedList.append(file.strip(str(i + 1) + '_'))

# corrects wrong numbering (in filenames from orderedList) using a regex
# then stores the new filenames (with correct numbering) in a new list (finalList)
finalList = []
numRegex = re.compile(r'\d+')
for i in range(len(orderedList)):
    for name in orderedList:
        if str(i + 1) in name:
            finalList.append(name)
            break
        else:
            newName = numRegex.sub(str(i + 1), name)
            finalList.append(newName)
            break

# renames the filenames (in user-given directory) if they have wrong numbering,
# then prints total amount of renamed files
renameCount = 0
for i in range(len(orderedList)):
    shutil.move(os.path.join(directory, orderedList[i]), os.path.join(directory, finalList[i]))
    if orderedList[i] != finalList[i]:
        print("Renamed '" + orderedList[i] + "' to '" + finalList[i] + "'")
        renameCount += 1
print('\nRenamed ' + str(renameCount) + ' files.')
