"""
pass_or_fail.py

Given the marks of multiple subjects, Report Pass or Fail.
Crieteria for Pass : minimum 35 for all the Subjects.

e.g.,

pass_or_fail.py  35 36 80
Pass

pass_or_fail.py  80 90 45 34
Fail
"""
import sys

def is_number(x):
    result = False
    if( len(x) > 1):
        if x[0] in "-+":
            x = x[1:]

    result = x.isdigit()
    return result

values = sys.argv[1:]

#input validation
# check all the given values are numbers. Exit therwise.
for v in values:
    if not is_number(v):
        print("Error : {0} is not a valid input".format(v))
        exit(1)

#All the inputs are valid. We can process now.
#Check each of the marks. And if any of them is <35, declare Failure
#Otherwise (i.e, none of the marks is <35), declare Pass.


# Fail : Any subject < 35, Otherwise Pass
result = True #Assume Pass
for v in values:
   print("Checking {0}".format(v))
   if float(v) < 35:
       result = False
       print("{0} is Fail".format(v))
       break

"""
# Pass : All the subjects >= 35, Otherwise Fail
result = False #Assume Fail
subject_checked = False
for v in values:
   subject_result = False
   if float(v) >= 35:
       subject_result = True
       print("{0} is Pass".format(v))
   else:
       print("{0} is Fail".format(v))
       subject_result = False
   if(not subject_checked):
       subject_checked = True
       result = subject_result

   result = result and subject_result
"""

if(result):
    print("Result : Pass")
else:
    print("Result : Fail")








