'''
An interactive program that takes a list of items
 from a file. 
Then user can interactively query 
 if a specific item exists in the list of not.

e.g.,

find_item.py   Kichidi  idly  "jeera rice" pulav biriyani roti dosa
Enter am item for lookup :     <idly>
Available.

Enter am item for lookup :  <naan>
Not Available

Enter am item for lookup :  <jeera Rice>
Available
'''
import sys
if(len(sys.argv) != 2):
    print("Usage :\n\tfind_item_ex.py <filename for the items>")
    exit(0)

file_name = sys.argv[1]
print(file_name)

def load_data(file_name):
    #open the fil
    file = open(file_name)
    #read the contents and split each line
    #return the split lines as alist
    return file.read().splitlines()

def find_item(item_list, item):
    #find if the item is present in the item list.
    found = False
    for x in item_list:
        #compare case insensitively to tollerate mixed case
        if (x.lower() == item.lower()):
            found = True
            #we can stop looking if already found
            break

    return found


#populate item_list with the content from the given file
item_list = load_data(file_name)
print(item_list)

while(True):
    #read input from the console.
    # use input if using python 3 instead of raw_input
    item = raw_input('Enter item for lookup : ')
    if(len(item) > 0):
        if(find_item(item_list, item)):
            print('Available')
        else:
            if(item.lower() == 'q'):  #quit if user gave q
            #if(len(item) == 0):  #quit if user gave q
                exit(0)
            else:
                print('Not Available')


