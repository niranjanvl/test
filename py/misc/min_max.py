"""
Given a list of numbers,
    find the maximum number
      and the minimum number 
      and the count of negative numbers
      and the count of positive numbers


> max_min.py 3 4 5 2 30 -1 6 7 8 -2 
   max : 30
   min : -2
   -ve : 2
   +ve : 8

> max_min.py  31 4 5 2 30 6 7 -8 100
   max : 100
   min : -8
   -ve : 1
   +ve : 8

"""

import sys

if(len(sys.argv) < 2):
    print("Usage :\n\t min_max.py <list of numbers>")
    exit(0)
           
num_list = [int(x) for x in sys.argv[1:]]
print(num_list)

max = num_list[0]
min = num_list[0]
positive = 0
negative = 0
for n in num_list:
    if n > max:
        max = n
    elif n < min:
        min = n

    if(n >= 0) :
        positive += 1
    else:
        negative += 1

print("max : {0}".format(max))
print("min : {0}".format(min))
print("+ve : {0}".format(positive))
print("-ve : {0}".format(negative))




