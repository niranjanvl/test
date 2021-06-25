'''
Given two numbers ( command line argument ) check wether one of them is divisible by the other.
    Ensure thorough error handling and help. Numbers can be given in any oder.

Examples :

> check_divisible.py
   Usage :
	check_divisible.py <non zero integer> <non zero integer>

> check_divisible.py 30 5
   30 is divisible by 5

> check_divisible.py 6 30
   30 is divisible by 6

> check_divisible.py  30 4
   30 is not divisible by 4

> check_divisible.py  0 4
   Invalid input.
   Usage :
	check_divisible.py <non zero integer> <non zero integer>
'''
import sys

def printUsageAndExit():
    print("Usage :\n\tcheck_divisible.py <non zero integer> <non zero integer>")
    exit()

if len(sys.argv) != 3:
    print("Invalid input")
    printUsageAndExit()

numerator = int(sys.argv[1])
denominator = int(sys.argv[2])

if (numerator == 0) or (denominator == 0):
    print("Invalid input")
    printUsageAndExit()

#Ensure the Numerator is >= Denominator
if numerator < denominator:
    #swap
    temp = numerator
    numerator = denominator
    denominator = temp

if numerator % denominator == 0:
    print("{0} is divisible by {1}".format(numerator,denominator))
else:
    print("{0} is not divisible by {1}".format(numerator,denominator))

