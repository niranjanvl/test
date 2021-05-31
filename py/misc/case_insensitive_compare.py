import sys

def compare(a, b):
    result = False

    if(a.lower() == b.lower()):
        result = True

    return result

if (sys.argv < 3):
    print("Usage : case_insensitive_compare.py  <string1> <string2>")

str1 = sys.argv[1]
str2 = sys.argv[2]

if( compare(str1, str2) == True ):
    print("The give strings matched")
else:
    print("The give strings do not match")



