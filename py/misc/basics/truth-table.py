'''
Take the boolean binary operator and compute the truth table.
truth-table.py  <and|or|xor|nand|nor>

truth-table.py and
T T : T
T F : F
F T : F
F F : F


truth-table.py or
T T : T
T F : T
F T : T
F F : F

truth-table.py xor
T T : F
T F : T
F T : T
F F : F

... etc.

'''

import sys
if(len (sys.argv) != 2):
    print("Invalid Arguments")
    print("Usage :")
    print("truth-table.py  <and|or|xor|nand|nor>")
    exit(0)

#Convert True as T and False as F
def TF(truth):
    if(truth):
        return 'T'
    else:
        return 'F'

operator = sys.argv[1]
if(operator == 'and'):
    print("T T : {0}".format(TF(True and True)))
    print("T F : {0}".format(TF(True and False)))
    print("F T : {0}".format(TF(False and True)))
    print("F F : {0}".format(TF(False and False)))

elif(operator == 'or'):
    print("T T : {0}".format(TF(True or True)))
    print("T F : {0}".format(TF(True or False)))
    print("F T : {0}".format(TF(False or True)))
    print("F F : {0}".format(TF(False or False)))

elif(operator == 'xor'):
    print("T T : {0}".format(TF(True ^ True)))
    print("T F : {0}".format(TF(True ^ False)))
    print("F T : {0}".format(TF(False ^ True)))
    print("F F : {0}".format(TF(False ^ False)))

elif(operator == 'nor'):
    print("T T : {0}".format(TF(not(True or True))))
    print("T F : {0}".format(TF(not(True or False))))
    print("F T : {0}".format(TF(not(False or True))))
    print("F F : {0}".format(TF(not(False or False))))

elif(operator == 'nand'):
    print("T T : {0}".format(TF(not(True and True))))
    print("T F : {0}".format(TF(not(True and False))))
    print("F T : {0}".format(TF(not(False and True))))
    print("F F : {0}".format(TF(not(False and False))))

else:
    print("Invalid operator")



