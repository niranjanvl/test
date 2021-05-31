"""
simple_calc.py
Given a simple expression in the below format, calculate the result
    <operand> <operator> <operand>
    operator : +,-,x,/,^,%

e.g.,
 simple_calc.py 1 + 10
    11

 simple_calc.py 1 - 10
    -9
"""

import sys

def is_number(x):
    result = False
    if( len(x) > 1):
        if x[0] in "-+":
            x = x[1:]

    result = x.isdigit()
    return result

def validate_operand(operand):
	value = None
	if is_number(operand):
		value = float(operand)
	else:
		print("Error. [{0}] is Invalid Operand".format(operand))
	return value

OPERATORS = ["+", "-", "x", "/", "^", "%"]
def validate_operator(operator):
	value = None
	if operator in OPERATORS:
		value = operator
	else:
		print("Error. [{0}] is Invalid Operator".format(operator))
	return value

expr = sys.argv[1:]

operand1 = validate_operand(expr[0])
operator = validate_operator(expr[1])
operand2 = validate_operand(expr[2])

if(operand1 is  None) or (operator is None) or (operand2 is None):
	print("Invalid Inputs")
	exit(1)

result  = 0
success = True

if(operator == '+'):
    result = operand1 + operand2
elif (operator == '-'):
    result = operand1 - operand2
elif (operator == 'x'):
    result = operand1 * operand2
elif (operator == '^'):
    result = operand1 ** operand2
elif (operator == '/'):
	if(operand2 == 0):
		print("Error : Denominator can not be Zero")
		success = False
	else:
		result = operand1 / operand2
elif (operator == '%'):
	if(operand2 == 0):
		print("Error : Denominator can not be Zero")
		success = False
	else:
		result = operand1 % operand2
else:
    print ("{0} is Invalid Operator".format(operator))
    success = False

if success:
    print("{0} {1} {2} = {3}".format(operand1, 
        operator, 
        operand2, 
        result))



