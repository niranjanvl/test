#---------------------------
# For each of the inputs, classify it as one of
#      Upper
#      Lower
#      Mixed
#      Number
#
#  A string consisting of all gidits is a Number. It can have a leading - or + 
#  Anything that is not a number is a Word. 
#  A word consisting of all Capital letters is 'Upper'. Ignore Digits.
#  A word consisting of all Small letters is 'Lower'. Ignore Digits.
#  A word consisting of Small and Capital letters is 'Mixed'. Ignore Digits.
#  
#  e.g., 
#  find_case.py cat DOG Tiger A1 123 b2
#    cat : Lower
#    DOB : Upper
#    Tiger : Mixed
#    A1 : Upper
#   123 : Number
#   b2 : Lower
#---------------------------
import sys

ALPHABET_CAPITAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
ALPHABET_SMALL = "abcdefghijklmnopqrstuvwxyz"  

def is_number(x):
    result = False
    if( len(x) > 1):
        if x[0] in "-+":
            x = x[1:]
        result = x.isdigit()

    return result

def is_space(x):
	result = True
	for c in x :
		if c not in ' ':
			result = False
			break
	return result

def is_alphabet(c):
	return c in (ALPHABET_SMALL + ALPHABET_CAPITAL)

def is_upper(x):
	result = True
	for c in x :
		if is_alphabet(c) and (c not in ALPHABET_CAPITAL) :
			result = False
			break
	return result

def is_lower(x) :
	result = True
	for c in x :
		if is_alphabet(c) and (c not in ALPHABET_SMALL) :
			result = False
			break
	return result


##
#
# for each of the values,
#  if the value is a number, then say it is 'Number'
#  otherwise,
#    if it has all the Capital letters, then say it is 'Upper'
#    otherwise if it has all the Lower letters, then say it is 'Lower'
#    otherwise say it is 'Mixed'
#
##

values = sys.argv[1:]

for v in values:
	desc = None
	if len(v) == 0:
		desc = "Empty"
	elif is_space(v):
		desc = "Spaces"
	elif is_number(v):
		desc = "Number"
	elif is_upper(v):
		desc = "Upper"
	elif is_lower(v):
		desc = "Lower"
	else:
		desc = "Mixed"

	print("[{0}] : {1}".format(v, desc))

















