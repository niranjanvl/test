'''
Given a list of numbers, sort them.
e.g.,

sort.py 3 4 1 9
  1 3 4 9


sort.py 3 4 -4 0 -1
  -4 -1 0 3 4
'''

import sys

if(len(sys.argv) < 2):
    print("Usage : \n\t sort.py <list of numbers>")
    exit(0)

values = [ int(x) for x in sys.argv[1:]]
print("  {0}".format(values))

'''
0. 3  9  4  1
1. 1, 9  4  3  - Swapped 3 and 1. Sorted list is upto 1.
2. 1  3, 4  9  - Swapped 9 and 3. Sorted list is upto 2.
3. 1  3  4, 9  - No swapping took place. Sorted list is upto 3.
'''
DEBUG = True
i = 0
min = None
j = 0

if DEBUG:
    print("  {0}, i : {1}, j : {2}, min : {3}".format(
        values, i, j, min))

#start from 0 and cover all the values 
while i < len(values):
    #sort the remaining list
    j = i
    min = values[i] #assume the first value is the minimum
    while j < len(values) :
        #find the minimum value in the remaing list
        if min > values[j]:
            #swap the smaller number with the initial position
            min = values[j]
            values[j] = values[i]
            values[i] = min
            if DEBUG:
                print("> {0}, i : {1}, j : {2}, min : {3} <> {4}".format(
                    values, i, j, min, values[j]))

        j += 1
    i += 1


print("  {0}".format(values))


    

