#! /usr/bin/python3
import re

def regexStrip(string, optChars= "no"):
    whiteBeginRegex = re.compile(r'^\s*|\s*$')
    optBeginRegex = re.compile('^(' + optChars + ')*|(' + optChars + ')*$')
    mo1 = whiteBeginRegex.sub('', string)
    mo2 = optBeginRegex.sub('', string)
    if optChars == "no":
        print('2nd argument not activated')
        print(mo1)
    else:
        print('2nd argument activated')
        print(mo2)

regexStrip('                Penis           ')
