'''
pass_fail.py  <marks>
Print Pass or Fail given the marks.
    Pass if marks are greater than or equal to 35. Otherwise Fail.

Also print the Grade if Pass
    Distinction  : >= 85
    First Class  : >= 60 and < 85
    Second Class : >= 50 and <60
    Third Class  : >=35 and < 50 

'''

import sys

marks = int(sys.argv[1])


'''
if(marks >= 35):
    print("Pass")
else:
    print("Fail")
if (marks >= 50) and (marks < 60):
    print("Second Class")

if (marks >= 60) and (marks < 85):
    print("First Class")

if(marks >= 85):
    print("Distinction")
'''
'''
if(marks >= 85):
    print("Distinction")
else:
    if (marks >= 60):
        print("First Class")
    else:
        if (marks >= 50):
            print("Second Class")

'''
if(marks >= 85):
    print("Distinction")
elif (marks >= 60):
    print("First Class")
elif (marks >= 50):
    print("Second Class")
elif (marks >= 35):
    print("Third Class")
else:
    print("Fail")


