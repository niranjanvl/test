import sys
print(sys.argv)
print("Arguments are : {0}".format(sys.argv))

if(len(sys.argv) == 3):
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    sum = x + y
    print("{0} + {1} = {2}".format(x,y,sum))
else:
    print("Usage\n\thello.py <x:integer> <y:integer>")
