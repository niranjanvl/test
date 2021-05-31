import sys
def print_usage():
    print("Usage :")
    print(" or_and.py   <and|or> <TFTFT...>")
    print(" and : Conjunction or : Disjunction")
    print(" TFTF... : List of True, False values")

def print_err_usage_and_exit(err):
    if(err):
        print(err)
    print_usage()
    exit(0)

if len(sys.argv) != 3:
    print_err_usage_and_exit("Invalid arguments.")

operation = sys.argv[1]
operation = operation.lower()
tflist = sys.argv[2]
tflist = tflist.upper()

#validate the operation
if not operation in ["and","or"]:
    print_err_usage_and_exit("Invalid operation.")

#validate the tflist
valid_tflist = True
if (len(tflist) == 0):
    valid_tflist = False

for v in tflist:
    if(not v in "TF"):
        valid_tflist = False

if(valid_tflist == False):
        print_err_usage_and_exit("Invalid tflist.")

result = None
if operation == "and":
    # result is False if F is present
    # result is True if F is not present
    result = ('F' not in tflist)
elif operation == "or":
    result = ('T' in tflist)
else:
    print_err_usage_and_exit("Invalid operator.")
    
if result is not None:
    print(result)

