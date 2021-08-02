'''
crypter.py
Encode & Decode

crypter.py encode <file> <key : integer>
crypter.py decode <file> <key : integer>

'''

import sys   #used for command line arguments
import random    #used for random number generation

DEFAULT_KEY = 121314151   #use when no key is supplied

'''
Encoding : Add the key to the plain text
           Cipher = Plain + Key
'''
def encode(plain, key):
    cipher = []
    for c in plain:
        cipher.append(ord(c) + key)
    return cipher

'''
Decoding : Subtract the key from the Cipher text
           Plain = Cipher - Key
'''
def decode(cipher, key):
    plain = []
    for c in cipher:
        plain.append(chr(c - key))
    return ''.join(plain)

if(len(sys.argv) < 3):
    print("Usage:\n\tcrypter.py <encode> <file path> [key:integer]")
    exit(0)

action = sys.argv[1].upper()
filepath = sys.argv[2]
okey = DEFAULT_KEY

if(len(sys.argv) > 3):
    okey  = int(sys.argv[3])

#read the file and store the content in the in_data variable.
file = open(filepath, "r")
in_data = file.read()
file.close()

out_data = None
out_file_path = None

'''
Doing encoding or decoding as per the arguments
'''

if(action == 'ENCODE'):
    '''
    Add a random number to the original key 
       and use the result as the key for encoding.

    Store the random part as the first element in the result
      so that it can used again during the decoding.
    '''
    #generate a randome number
    rnd = random.randint(1,100000)

    #add the rnd to the original key and use the sum as the key
    cipher = encode(in_data, okey+rnd) 

    #store the rnd as the first element in the result
    data = [rnd] + cipher
    
    #convert the list of integers into a single string
    out_data = ' '.join([str(i) for i in data])

    #genrate the filename to store the cipher text
    out_file_path = filepath+".cipher"
elif(action == 'DECODE'):
    '''
    Retrieve the random part from the first element in the result
      so that it can used again for decoding.

    Need to subtract the random number from the original key 
       and use the result as the key for decoding.
    '''
    #convert the string into a list of integers
    cipher = [int(x) for x in in_data.split(' ')]

    #first element of the list is the rnd used during encoding.
    rnd = int(cipher[0])

    #the elements other than the rnd is the ciphertext to be decoded.
    #Add the rnd to the original key to generate the key for encoding.
    out_data = decode(cipher[1:], okey+rnd)

    #genrate the filename to store the plain text
    out_file_path = filepath+".plain"
else:
    print("Invalid Input.")

#write the date to out_file_path only if the data is available.
if(out_data and out_file_path):
    #open the file
    out_file = open(out_file_path, "w")
    #store/write the data the file
    out_file.write(out_data)
    #close the file
    out_file.close()


