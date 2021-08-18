'''
Generate odd/even numbers between the given numbers (inclusive).
The choice and the range is given as command line arguments.
e.g.,

gen_odd_even.py <odd/even> <int> <int>

    odd/even : can be case insensitive
    range can be ascending or descending

gen_odd_even.py odd 2 10
  3, 5, 7, 9

gen_odd_even.py odd 10 2
  9, 7, 5, 3

gen_odd_even.py odd 7 15
  7, 9, 11, 13, 15

gen_odd_even.py even 2 10
  2, 4, 6, 8, 10

gen_odd_even.py even 10 2
  10, 8, 6, 4, 2

'''
# Import necessary modules
# Read the commmand line argumets
# Validate the arguments. If valid, 
#  proceed, otherwise print usage
# Generate the result.
# Present the result.

import sys

def print_usage():
    print("Usage :")
    print("gen_odd_even.py <choice> <begin> <end>")
    print(" choice : odd | even")
    print("  begin : integer")
    print("    end : integer")

def process_arguments(args):
    #Process arguments
    #  gen_odd_even.py <odd/even> <int> <int>
    choice = None
    begin = None
    end = None
    valid_args = True

    if(len(sys.argv) != 4):
        print("Invalid number of arguments : {0}".
                format(len(sys.argv)))
        valid_args = False

    if(valid_args):
        arg = sys.argv[1]
        if(arg.lower() not in ["odd", "even"]):
            print("Invalid choice : {0}".format(arg))
            valid_args = False
        else:
            choice = arg.lower()

    if(valid_args):
        arg = sys.argv[2]
        if(not arg.isdigit()):
            print("Invalid begin : {0}".format(arg))
            valid_args = False  
        else:
            begin = int(arg)

    if(valid_args):
        arg = sys.argv[3]
        if(not arg.isdigit()):
            print("Invalid end : {0}".format(arg))
            valid_args = False  
        else:
            end = int(arg)

    if(valid_args):
        return choice, begin, end
    else:
        print_usage()
        exit()
        #return None, None, None

def print_result(choice, begin, end, result):
    #Print the result
    print("The {0} numbers in the range {1},{2} :".
            format(choice, begin, end))
    print(", ".join([str(x) for x in result]))
    return None

def generate_result(choice, begin, end):
    result = None
    #Compute the result
    # TODO
    result = [1, 2, 3, 4]
    return result

def main():
    choice, begin, end = process_arguments(sys.argv)
    result = generate_result(choice, begin, end)
    print_result(choice, begin, end, result)

if __name__ == "__main__":
    main()



