"""
Take a series of True or False and compute disjunction
conjunction : x OR y OR z ...

T : True, F : False
"""
import sys
values = sys.argv[1:]
result = False
for v in values:
    if (v == 'T'):
        result = True
        break
    else:
        result = False

print("Result : {0}".format(result))



