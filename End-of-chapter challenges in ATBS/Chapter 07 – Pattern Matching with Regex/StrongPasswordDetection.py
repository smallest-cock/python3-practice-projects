#! /usr/bin/python3
# strongPasswordDetection.py - Detects whether a password is strong or not
import re


def passChecker(string):
    passRegexCaps = re.compile(r'[A-Z]+')   # regex that has at least one capital letter
    passRegexLow = re.compile(r'[a-z]+')    # regex that has at least one lowercase letter
    passRegexDigit = re.compile(r'\d')      # regex that has at least one digit
    passRegexLen = re.compile(r'.{8,}')     # regex that has at least 8 characters
    passRegexSpace = re.compile(r'\s')      # regex that has a space character
    mo1 = passRegexCaps.search(string)
    mo2 = passRegexLow.search(string)
    mo3 = passRegexDigit.search(string)     # assigns variables to compiled regex objects
    mo4 = passRegexSpace.search(string)
    mo5 = passRegexLen.search(string)
    if mo1 != None:
        if mo2 != None:
            if mo3 != None:
                if mo4 == None:
                    if mo5 != None:
                        print('\nThis is a strong password.')
                    else:
                        print('\nWeak password. Needs to be at least 8 characters long.')
                else:
                    print('\nInvalid password. Cannot contain space characters.')
            else:
                print('\nWeak password. Needs at least one digit.')
        else:
            print('\nWeak password. Needs at least one lowercase letter.')
    else:
        print('\nWeak password. Needs at least one uppercase letter.')


password = input('Enter a password to check:  ')
passChecker(password)
