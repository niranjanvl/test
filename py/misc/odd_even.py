#---------------------
# Given list of numbers, find out whether they are Odd or Even
# If the input is not a number, ignore it.
#
# odd_even.py 1 2 x 3
# 1 : Odd
# 2 : Even
# x : Invalid Input
# 3 : Odd
#---------------------
import sys

def printUsage():
    print("Usage:\n\todd_even.py <integer> <integer> ...")

def odd_even(v):
    #Check if v is a number
    #If v is not a number then error,
    # otherwise determine if it is Odd or Even

    if not v.isdigit():
        print("{0} : Invalid Input".format(v))
    else:
        int_v = int(v) 
        if(int_v % 2 == 0):
            print("{0} : Even".format(v))
        else:
            print("{0} : Odd".format(v))

values = sys.argv[1:]

if(len(values) == 0):
    printUsage()
else:
    for v in values:
        odd_even(v)


