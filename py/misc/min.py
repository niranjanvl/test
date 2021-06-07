"""
Given a list of numbers,
    find the minimum number 


> min.py 3 4 5 2 30 -1 6 7 8 -2 
   min : -2

> min.py  31 4 5 2 30 6 7 -8 100
   min : -8
"""

import sys

if(len(sys.argv) < 2):
    print("Usage :\n\t min.py <list of numbers>")
    exit(0)
           
num_list = [int(x) for x in sys.argv[1:]]
print(num_list)

min = num_list[0]
for n in num_list:
    if n < min:
        min = n

print("min : {0}".format(min))




