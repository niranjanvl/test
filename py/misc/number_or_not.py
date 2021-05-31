#--------------------------
# for each of the given argument 
#  find out if it is a number or not
#
# number_or_not.py 12 1 -1 abc 123b
# 12 : Number
# 1 : Number
# -1 : Number
# abc : Not a Number
# 123b : No a Number
#--------------------------

import sys

values = sys.argv[1:]

def is_number(x):
    result = False #Initialization
    if( len(x) > 1):
        if x[0] in "-+":
            x = x[1:]
        result = x.isdigit()

    return result
    

for v in values:
    if is_number(v):
        print("{0} : Number".format(v))
    else:
        print("{0} : Not a Number".format(v))


