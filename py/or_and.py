"""
Given the below inputs calculate the result
or_and.py  <or/and> TFFFTTSS...

T : True
F : False

or : disjunction
and : conjunction

e.g.,

or_and.py  or FFFTFFFF
Result : True

or_and.py  and FFFTFFFF
Result : False
"""

import sys

if len(sys.argv) != 3:
    print("invalid arguments")
    exit(0)
operation = sys.argv[1]
tflist = sys.argv[2]

result = None
if (operation in ["and", "or"]):
	result = ((operation == "and") and ("F" not in tflist)) or ((operation == "or") and ("T" in tflist))
else:
    print("Invalid operator")

if result is not None:
    print(result)

