#--------------------------
# for each of the given argument 
#  find out if it is a word or not
#
# Note : Anything not a number is a Word
#
# word_or_not.py 12 1 -1 abc 123b
# 12 : Not a Word
# 1 : Not a Word
# -1 : Not a Word
# abc : Word
# 123b : Word
#--------------------------

import sys

values = sys.argv[1:]

def is_number(x):
    result = False
    if( len(x) > 1):
        if x[0] in "-+":
            x = x[1:]

    result = x.isdigit()
    return result
    

for v in values:
    if not is_number(v):
        print("{0} : Word".format(v))
    else:
        print("{0} : Not a Word".format(v))


