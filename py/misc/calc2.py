#Calculator
#Command line inputs

import sys

print(sys.argv)
num_of_arguments = len(sys.argv)

if(num_of_arguments < 4):
    print("Invalid Arguments.")
    print("Usage : calc2.py 1 + 3 - 2 + .... ")
    print("Operators : +, -")
    exit(1)

result = 0 
success = True

result = 0
operator = '+'
for i in range(1, num_of_arguments):
    input = sys.argv[i]
    if( i % 2 == 0): #even position i.e., operator
        operator = input
        #if( operator == '+' or operator =='-'):
        if( operator not in ['+', '-'] ):
            print('Invalid Operator : {0}'.format(operator))
            success = False
            break
    else: #odd position i.e, number
        if(input.isdigit()):
            num = float(input)
            if (operator == '+'):
                result = result + num
            elif (operator == '-'):
                result = result - num
        else:
            print('Invalid input : {0}. Digit expected.'.format(input))



if success:
    print('Result : {0}'.format(result))
else:
    print("Failed executing.")


