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

oveall_pass = True
pass_count = 0
fail_count = 0
average = 0
for marks in marks_list:
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

#TODO : Find out Pass / Fail overall.
#       Calculate the correct oveall_pass
if(oveall_pass):
    print("Oveall Result : Pass")
else:
    print("Oveall Result : Fail.") 
    print(pass_count)
    print(" -Number of Subjects Cleared.")
    print(fail_count)
    print(" -Number of subjects Failed.")
    #TODO : Print Average







