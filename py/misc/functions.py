'''
functions.py


def function_name(arguments):
	# Do something on arguments
    # What the function does goes here
    return result # the result of operations on the arguments

01. Syntax
02. Function without argumets
03. Function with argumets
04. Function with return value
05. Positional argumetns
06. Keyword arguments
07. Variable number of arguments
08. Using List for arguments
09. Using Dictionary for arguments
10. List vs Variable Number of Arguments
'''

#Function to greet without any arguments
def	greet():
	print("Hi, how are you doing ?") 

#Function to greet given a person and place
def greet_pp(person, place): 
	print("Hi {0}, how are you doing at {1} ?".
		format(person, place))

def greet_ppd(details): 
	print("Hi {0}, how are you doing at {1} ?".
		format(details["person"], details["place"]))

def greet_ppd_many(*dataset): 
	for details in dataset:
		print("Hi {0}, how are you doing at {1} ?".
			format(details["person"], details["place"]))

def greet_ppd_list(datalist): 
	for details in datalist:
		print("Hi {0}, how are you doing at {1} ?".
			format(details["person"], details["place"]))

#Function to return the result i.e. sum of two integers
def add(a,b):
	result = a+b
	return result

#Function to return the result i.e. sum of any number of intgers
def addn(*args):
	result = 0
	for x in args:
		result = result + x
	return result

#Function to return the result i.e. sum of numbers in a given list
def addl(list_of_values):
	result = 0
	for x in list_of_values:
		result = result + x
	return result

#Main program
greet()

person = "Ram"
place = "Ayodhya"
greet_pp(person, place)

person = "Kris"
place = "Gokul"
greet_pp(person, place)

x = 10
y = 20
sum = add(x,y)

print("Sum of {0} and {1} is {2}.".
	format(x,y,sum))

#positional arguments
print("positional arguments ---")
greet_pp("Kris", "Gokul")
greet_pp("Gokul", "Kris")

#keyword arguments
print("keyword arguments ---")
greet_pp(place="Gokul", person="Kris")
greet_pp(person="Kris", place="Gokul")


#Use variable number of argument
print("variable number of arguments ---")
print( addn(10, 20) )
print( addn(10, 20, 30) )
print( addn(10, 20, 30, 40, 50, 60) )

#Use list of arguments
print("list as a (single) argument ---")
print( addl([10, 20]) )
print( addl([10, 20, 30]) )
print( addl([10, 20, 30, 40, 50, 60]) )

#call a function with a dictionary 
print("Greet with a dictionary---")
greet_ppd( {'person' : 'Ram', 'place' : 'Ayodhya'})

pplist = [
		{'person' : 'Ram', 'place' : 'Ayodhya'},
		{'person' : 'Kris', 'place' : 'Gokul'},
		{'person' : 'Kiran', 'place' : 'Whitefield'},
		{'person' : 'Vali', 'place' : 'Kishkinda'}
	]

greet_ppd(pplist[0])
greet_ppd(pplist[1])
#greet_ppd(pplist[2])

print("About to greet many at once using var args----")
#greet_ppd_many(pplist[0], pplist[1], pplist[2])
greet_ppd_many(pplist[0], pplist[1])

print("About to greet many at once using list----")
greet_ppd_list(pplist)


	

