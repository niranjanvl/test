'''
An interactive program that takes a list of items
 from a file. 
Then user can interactively query 
 if a specific item exists in the list of not.

Ignore case while comparing
Ignore spaces while comparing

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
    #open the file and load the contents 
    file = open(file_name)
    #read the contents and split each line
    #return the split lines as alist
    return file.read().splitlines()

def remove_spaces(x):
    res = ''
    for char in x:
        if(char != ' '):
            res += char
    return res

def compare_item(x, y):
    #compare items 
    #ignore case 
    #ignore spaces
    return remove_spaces(x.lower()) == remove_spaces(y.lower())

def find_item(item_list, item):
    #find if the item is present in the item list.
    entry = None
    for x in item_list:
        temp = x.split(',')
        #compare case insensitively to tollerate mixed case
        if (compare_item(temp[0], item)):
            #we can stop looking if already found
            entry = temp
            break

    return entry


#populate item_list with the content from the given file
item_list = load_data(file_name)
print(item_list)
selected_items = {}

while(True):
    #read input from the console.
    # use input if using python 3 instead of raw_input
    item = raw_input('Enter item for lookup : ')
    if(len(item) > 0):
        entry = find_item(item_list, item)
        if(entry != None):
            print('Available.\n Item : {0}, Price : {1}'.format(
                    entry[0], entry[1]))
            #Check if the selected item is already in our dict
            #if not present - then add an new entry with count:1
            #if alreaedy present - then just increment the count
            if not selected_items.has_key(entry[0]):
                selected_items[entry[0]] = {
                            'count' : 1,
                            'price' : entry[1]
                        }
            else:
                selected_items[entry[0]]['count'] += 1
        else:
            if(item.lower() == 'q'):  #quit if user gave q
                break
            else:
                print('Not Available')

#print the summary
# All the selected items and 
# total amount
total = 0
if(len(selected_items) > 0):
    print("Selected Items :")
    for item in selected_items.items():
        name = item[0]
        count = item[1]['count']
        price = int(item[1]['price'])*count
        total += price
        print("{0}({1}) : {2}".format(name.rjust(25), 
            str(count).rjust(2),
            str(price).rjust(5))
            )
    
    print("-----------------------------")
    print("{0} : {1}".format("total".rjust(29), 
        str(total).rjust(5)))


