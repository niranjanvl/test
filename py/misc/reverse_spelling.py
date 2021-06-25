'''
Reverse the spelling of given input (single or multiple strings)

Examples :
   > reverse_spelling.py
      Usage :
	reverse_spelling.py <any thing ...> 

   > reverse_spelling.py abcd
       dcba

   > reverse_spelling.py 1234
       4321

   > reverse_spelling.py 1234 abcd
       dcba 4321

Note :
1. Please ensure you keep the same file names as suggested above for easy reference.
2. Once you finish the program you should test it thoroughly.
'''

import sys

def printUsageAndExit():
    print("Usage:\n\treverse_spelling.py <anything>")

values = sys.argv[1:]

if len(values) == 0:
	printUsageAndExit()

'''
full_str = ""
for v in values:
	full_str += " " + v

print(full_str[-1::-1])
'''
print(" ".join(values)[-1::-1])





