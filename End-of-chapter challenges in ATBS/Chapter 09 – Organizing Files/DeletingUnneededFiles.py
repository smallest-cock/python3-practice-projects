#!/usr/bin/env python3
# DeletingUnneededFiles.py - Walks through a folder tree and searches for large files or folders (> 100MB).
# Print these files with their absolute path to the screen.
import os

# formats the folder path from user input and stores it in a variable
folderPath = (input('Enter a folder path to search for large files:  ')).strip("'")
if not os.path.isdir(folderPath):
    print('Error: That isn\'t a valid folder path')
    exit()

# walks through the given directory and prints path to each file/folder found that's over 100MB in size
noLargeFiles = True
noLargeFolders = True
for currentdir, subdirs, files in os.walk(folderPath):
    for subdir in subdirs:
        if os.path.getsize(os.path.join(currentdir, subdir)) > 100000000:
            print('Large folder found:  ' + os.path.join(currentdir, subdir))
            noLargeFolders = False
    for file in files:
        if os.path.getsize(os.path.join(currentdir, file)) > 100000000:
            print('Large file found:  ' + os.path.join(currentdir, file))
            noLargeFiles = False

# prints message if no large file/folders were found in the given directory
if noLargeFolders:
    print('\nThere are no folders over 100MB in this directory...')
if noLargeFiles:
    print('\nThere are no files over 100MB in this directory...')
