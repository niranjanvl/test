'''
crypter.py
Encode & Decode

crypter.py encode <file> <key : integer>
crypter.py decode <file> <key : integer>

'''

import sys
DEFAULT_KEY = 121314151

def encode(plain, key):
    cipher = []
    for c in plain:
        cipher.append(ord(c) + key)
    return " ".join([str(x) for x in cipher])

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
key = DEFAULT_KEY
if(len(sys.argv) > 3):
    key  = int(sys.argv[3])

#read the file and store the content in the in_data variable.
file = open(filepath, "r")
in_data = file.read()
file.close()
out_data = None
out_file_path = None

if(action == 'ENCODE'):
    out_data = encode(in_data, key)
    out_file_path = filepath+".cipher"
elif(action == 'DECODE'):
    cipher = [int(x) for x in in_data.split(' ')]
    out_data = decode(cipher, key)
    out_file_path = filepath+".plain"
else:
    print("Invalid Input.")

#write the date to out_file_path
if(out_data and out_file_path):
    out_file = open(out_file_path, "w")
    out_file.write(out_data)


