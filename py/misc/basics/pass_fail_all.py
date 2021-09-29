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
#print(marks_list)
num_subjects = 0
oveall_pass = True
pass_count = 0
fail_count = 0
average = 0
total_marks = 0

#Iterate over the the marks list. 
for marks in marks_list:

    passMark = True
    print(marks)
    if(marks >= 85):
        print(" -Distinction")
    elif (marks >= 60):
        print(" -First Class")
    elif (marks >= 50):
        print(" -Second Class")
    elif (marks >= 35):
        print(" -Third Class")
    else:
        print(" -Fail")
        oveall_pass = False
        passMark = False

    total_marks = total_marks + marks
    if(passMark):
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

num_subjects = pass_count + fail_count
average = total_marks / num_subjects

#Find out Pass / Fail overall.
#       Calculate the correct oveall_pass
if(oveall_pass):
    print("Oveall Result : Pass")
else:
    print("Oveall Result : Fail.") 
    print(pass_count)
    print(" -Number of Subjects Cleared.")
    print(fail_count)
    print(" -Number of subjects Failed.")
    print(num_subjects)
    print(" -Number of Subjects.")
    print(total_marks)
    print(" -Total Marks.")
    print(average)
    print(" -Average Mark.")









