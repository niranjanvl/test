"""
Evaluate a Polynomial (single variable) given the value of x and the expression

    polynomial.py <x> <coefficients>

    polynomial.py 2 3 5 7
        x : 2, polynomial : 3x^2 + 5x + 7
        29

Given an polinomial (over x) and values of x, evaluate the polynomial.

    3x^2 + 5x + 7
        3 5 7

    8x^3 + 3x^2 + 5x + 7
        8 3 5 7

    8x^3 + 5x + 7
        8 0 5 7

    8x^3 - 5x + 7
        8 0 -5 7

    A polynomial is represented by the list coefficients
"""
import sys

def print_expr(coefficients):
    expr = ""
    power = len(coefficients) - 1

    for coeff in coefficients:
        operator = " + "
        if(coeff[0] == "-"):
            operator = " - "
            coeff = coeff[1:] #if negative then take the absolute value
        
        #expr += "{0}({1})x^{2}".format(operator,coeff, power)

        if(power == 0): #constant
            expr += "{0}{1}".format(operator,coeff)
        elif(power == 1): #power one  i.e., x
            expr += "{0}{1}x".format(operator,coeff)
        else: #power greater than one i.e., x^power
            expr += "{0}{1}x^{2}".format(operator,coeff, power)

        power -= 1

    print("polynomial : {0}".format(expr))

def eval_expr(coefficients, x):
    value = 0
    power = len(coefficients) - 1
    for coeff in coefficients:
        value += float(coeff) * (float(x)**float(power))
        power -= 1
    print("value : {0}".format(value))

x = sys.argv[1]
coefficients = sys.argv[2:]

print("x : {0}".format(x))
print("coefficients : {0}".format(coefficients))
print_expr(coefficients)
eval_expr(coefficients, x)

