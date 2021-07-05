'''
Reverse the spelling of given input (single or multiple strings)
  without changing the positions of individual strings (inplace)

Examples :
   > reverse_spelling.py
      Usage :
	reverse_spelling.py <any thing ...> 

   > reverse_spelling.py abcd
       dcba

   > reverse_spelling.py 1234
       4321

   > reverse_spelling.py 1234 abcd
       4321 dcba

   > reverse_spelling.py madam radar racecar
       madam radar racecar

Note :
1. Please ensure you keep the same file names as suggested above for easy reference.
2. Once you finish the program you should test it thoroughly.
'''

import sys

def printUsageAndExit():
    print("Usage:\n\treverse_spelling_inplace.py <anything>")

values = sys.argv[1:]

if len(values) == 0:
	printUsageAndExit()

result = ""
for v in values:
    result += v[-1::-1] + " "

print("{0} ".format(result))

'''
# python 2
for v in values:
   print(v[-1::-1]),
'''

'''
# python 3
for v in values:
   print(v[-1::-1], end=" ")
'''




