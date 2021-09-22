'''
pass_fail.py  <marks>
Print Pass or Fail given the marks for many subjects
    Pass if marks are greater than or equal to 35. Otherwise Fail.

Also print the Grade if Pass
    Distinction  : >= 85
    First Class  : >= 60 and < 85
    Second Class : >= 50 and <60
    Third Class  : >=35 and < 50 

'''

import sys

marks_list = [int(x) for x in sys.argv[1:]]
print(marks_list)

'''
---- process marks in subject 1
marks = marks_list[0])
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

---- process marks in subject 2
marks = marks_list[1])
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

---- process marks in subject 3
marks = marks_list[2])
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


'''

for marks in marks_list:
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





