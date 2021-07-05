'''
Given a string - check wether it is a palindrome or not.

A palindrome is a word, number, phrase, or other sequence of characters 
 which reads the same backward as forward, such as madam or racecar. 
There are also numeric palindromes, including date/time stamps using 
 short digits 11/11/11 11:11 and long digits 02/02/2020. 
Sentence-length palindromes ignore capitalization, punctuation, and word boundaries.
'''
import sys

def printUsage():
    print("Usage:\n\tcheck_palindrome.py <word> <word> ...")

if(len(sys.argv) < 2):
    printUsage()
    exit(0)


value = " ".join(sys.argv[1:])
print("Value : \"{0}\"".format(value))

#normalize the case.
value = value.lower()

#if reverse of the string is same as the string, then it is a palyndrome

if(value == value[-1::-1]):
    print("Palyndrome")
else:
    print("Not a Palyndrome")

