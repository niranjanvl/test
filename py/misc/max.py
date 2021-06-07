"""
Given a list of numbers,
    find the maximum number 


> max.py 3 4 5 2 30 -1 6 7 8 -2 
   max : -2

> max.py  31 4 5 2 30 6 7 -8 100
   max : -8
"""

import sys

if(len(sys.argv) < 2):
    print("Usage :\n\t max.py <list of numbers>")
    exit(0)
           
num_list = [int(x) for x in sys.argv[1:]]
print(num_list)

max = num_list[0]
for n in num_list:
    if n > max:
        max = n

print("max : {0}".format(max))




