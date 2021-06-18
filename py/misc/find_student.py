'''
An interactive program that takes a list of students
 from a file. 
Then user can interactively query 
 if a specific roll number exists in the list of not.

 Assume roll number if an alphanumeric string

Ignore case while comparing
Ignore spaces while comparing

Capitalize Names i.e., rama should be printed as Rama

e.g.,

find_student.py student_list.txt 
Enter am student for lookup :     1
Rama

Enter am student for lookup :  20
Not Available

Enter am student for lookup :  3
Sita
'''
import sys
if(len(sys.argv) != 2):
    print("Usage :\n\tfind_student.py <filename for the student list>")
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

def compare_student(x, y):
    #compare students 
    #ignore case 
    #ignore spaces
    return remove_spaces(x.lower()) == remove_spaces(y.lower())

def find_student(student_list, student):
    #find if the student is present in the student list.
    entry = None
    for x in student_list:
        temp = x.split(',')
        #compare case insensitively to tollerate mixed case
        if (compare_student(temp[0], student)):
            #we can stop looking if already found
            entry = temp
            break

    return entry


#populate student_list with the content from the given file
student_list = load_data(file_name)
print(student_list)
selected_students = []
selected_roll_num = []

while(True):
    #read input from the console.
    # use input if using python 3 instead of raw_input
    student = raw_input('Enter roll number for lookup : ')
    if(len(student) > 0):
        entry = find_student(student_list, student)
        if(entry != None):
            print('Available.\n No : {0}, Name : {1}'.format(
                    entry[0], entry[1].capitalize()))
            if( student not in selected_roll_num ):
                selected_roll_num.append(student)
                selected_students.append(entry)
        else:
            if(student.lower() == 'q'):  #quit if user gave q
                break
            else:
                print('Not Available')

#print the summary
# All the selected list of students (unique)
# total number of students
if(len(selected_students) > 0):
    print("Selected Students :")
    for student in selected_students:
        print("{0} : {1}".format(student[0].rjust(25), 
            student[1].rjust(5)))

    print("\nSelected Student Count....: {0}".format(
        len(selected_students)))
    

