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

def find_min(start, values):
    #
    # Given list and starting position,
    #  find the minimum value and return it along with it's position
    #


    if(len(values) == 0):
        #if the list is empty then return with None.
        return None, None

    #assume the first elemet is the minimum
    #find the minimum values starting with index : start
    j = start
    min = values[j]
    pos = start
    while j < len(values):
        if values[j] < min:
            min = values[j] #remember the smaller value
            if DEBUG:
                print("> {0}, i : {1}, j : {2}, min : {3} <> {4}".format(
                    values, start, j, min, values[pos]))
            pos = j #remember the position where we found the smaller value

        j += 1

    #return the minimum value as well as its position in the list
    return min, pos




#The list of position<i are already sorted and position>=i are yet to be sorted
#Start with i = 0
i = 0
#for each position in the list starting from i to the end
while i < len(values):
    #find the minimum value in the list for positions >= i
    min, pos = find_min(i, values)

    #swap the values at current i and the position of the new minimum
    values[pos] = values[i]
    values[i] = min

    #move the i to the next position. 
    i += 1


print("  {0}".format(values))


    

