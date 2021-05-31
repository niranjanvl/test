#Calculator
#Command line inputs

import sys

print(sys.argv)

num_of_arguments = len(sys.argv)

if(num_of_arguments < 4):
    print("Invalid Arguments.")
    print("Usage : calc.py <operator> <operand1> <operand2> ... ")
    print("Operators : +, -, x, /")
    exit(1)

operator = sys.argv[1]
result = 0 
success = True

# Compute the Result
if(operator == '+'):
    result = float( sys.argv[2] )
    for i in range(3, num_of_arguments):
        result = result + float( sys.argv[i] )

elif(operator == '-'):
    result = float( sys.argv[2] )
    for i in range(3, num_of_arguments):
        result = result - float( sys.argv[i] )

elif((operator == 'x') or (operator == 'X')):
    result = float( sys.argv[2] )
    for i in range(3, num_of_arguments):
        result = result * float( sys.argv[i] )

elif(operator == '/'):
    result = float( sys.argv[2] )
    for i in range(3, num_of_arguments):
        result = result / float( sys.argv[i] )

else:
    print('Invalid Operator : {0}'.format(operator))
    success = False

if success:
    print('Result : {0}'.format(result))
else:
    print("Failed executing.")


