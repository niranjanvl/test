import sys

#input validation
direction = None
valid_args = True
if ( len(sys.argv) > 1):
    if (sys.argv[1] == 'f'):
        direction = "Forward"
    elif(sys.argv[1] == 'r'):
        direction = "Backward"
    else:
        valid_args = False
else:
    valid_args = False

if not valid_args:
    print("Invalid arguments")
    print("Usage :  reverse.py <f/r> ...")
    print("         f : Forward, r : Reverse")

    exit(0)

#actual processing 
values = sys.argv[2:]
values_len = len(values)
print("Length is {0}\nValues are {1}\nDirection is {2}".format(values_len, values, direction))

for i in range(0, values_len):
    if (direction == "Forward"):
        print("-> idx : {0}, val : {1}".format(i, values[i]))
    else:
        ri = (values_len - 1) - i
        print("-> idx : {0}, val : {1}".format(ri, values[ri]))

