'''
An interactive program that takes a list of words 
 from command line. Then user can interactively query 
 if a specific word is exists in the given list of not.

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
item_list = sys.argv[1:]
print(item_list)


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


while(True):
    #read input from the console.
    # use input if using python 3 instead of raw_input
    item = raw_input('Enter item for lookup : ')

    if(find_item(item_list, item)):
        print('Available')
    else:
        if(item.lower() == 'q'):  #quit if user gave q
        #if(len(item) == 0):  #quit if user gave q
            exit(0)
        else:
            print('Not Available')


