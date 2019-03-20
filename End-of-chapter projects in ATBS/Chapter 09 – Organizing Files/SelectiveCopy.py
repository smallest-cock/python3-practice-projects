#! /usr/bin/python3
# SelectiveCopy.py - Walks through a folder tree and searches for files with a certain file extension
# (such as .pdf or .jpg). Then copies these files from whatever location they are in to a new folder.
import os, shutil

# formats the folder path from user input and stores it in a variable
folderPath = (input('Enter path of the folder you wish to search through:  ')).strip("'")

# prints error message if the given folder path does not exist or is not a folder
if os.path.exists(folderPath) == False or os.path.isdir(folderPath) == False:
    print('Error: That isn\'t a valid folder path')
    exit()

# promts user for filetype extension and stores it in a variable
extension = input('Enter file extension (e.g. .jpg, .pdf, .exe, etc.):   ')

# creates destination folder path (and formats as necessary) then stores it in a variable
destFolderPath = os.path.join(os.getcwd(), extension.strip('.') + 'Files')
os.makedirs(destFolderPath)

# walks given folder, and copies found files of given filetype to new folder in "destFolderPath"
noFiles = True
for curfolder, folderlist, filelist in os.walk(folderPath):
    for file in filelist:
        if file.endswith(extension):
            shutil.copy(os.path.join(curfolder, file), os.path.join(destFolderPath, file))
            print('Copied ' + extension + ' file from ' + curfolder)
            noFiles = False

# prints message if the given filetype is not found in the given folder, otherwise prints success message
if noFiles == True:
    print('\nThere are no "' + extension + '" filetypes in ' + folderPath)
else:
    print('\nNew folder containing ' + extension + ' files: ' + destFolderPath)
