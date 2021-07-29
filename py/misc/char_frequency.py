import sys

file = open( sys.argv[1] )
input_string = file.read()

frequencies = {} 
  
for char in input_string: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

for x in frequencies:
    print("{0} : {1}".format(x, frequencies[x]))


