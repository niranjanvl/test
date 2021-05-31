import sys

def pow(x,y):
    #x to the power of y
    result = 1

    if y >  0:
        #repetitive multiplication
        i = 0
        while i < y:
            result *= x
            i += 1
    elif y < 0:
        #repetitive division
        i = y
        while i < 0:
            result /= x
            i += 1
    else:
        result = 1
    

    return result


x = float(sys.argv[1])
y = float(sys.argv[2])

print(pow(x,y))


