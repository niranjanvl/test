'''
crypter.py
Encode & Decode

crypter.py encode <file> <key : integer>
crypter.py decode <file> <key : integer>

'''

import sys

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

if(len(sys.argv) < 4):
    print("Usage:\n\tcrypter.py <encode> <data> <key:integer>")
    exit(0)

action = sys.argv[1].upper()
data = sys.argv[2]
key  = int(sys.argv[3])

if(action == 'ENCODE'):
    cipher = encode(data, key)
    print(cipher)
elif(action == 'DECODE'):
    cipher = [int(x) for x in data.split(' ')]
    plain = decode(cipher, key)
    print(plain)
else:
    print("Invalid Input.")


