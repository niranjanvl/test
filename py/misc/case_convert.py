import sys

#input validation
case = None
valid_args = True
if ( len(sys.argv) > 1):
    #case normalization for the mode
    mode = sys.argv[1].upper()

    if (mode == '--CAPITAL'):
        case = "Upper"
    elif(mode == '--SMALL'):
        case = "Lower"
    else:
        valid_args = False
else:
    valid_args = False

if not valid_args:
    print("Invalid arguments")
    print("Usage :  upper.py <--capital/--small> ...")
    print("         --capital : Upper case, --small : Lower case")

    exit(0)

#actual processing 
values = sys.argv[2:]
values_len = len(values)

for i in range(0, values_len):
    if (case == "Upper"):
        print(values[i].upper())
    elif (case == "Lower"):
        print(values[i].lower())


