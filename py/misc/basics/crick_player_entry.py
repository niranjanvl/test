shirt_input = raw_input("White Shirt ?. Y/N : ")
pant_input = raw_input("White Pant. Y/N : ")


shirt = False
if(shirt_input == 'Y'):
    print("Shirt is White.")
    shirt = True
else:
    print("Shirt is not White.")

pant = False
if(pant_input == 'Y'):
    print("Pant is White.")
    pant = True
else:
    print("Pant is not White.")

if(shirt and pant):
    print("Player is Allowed In.");
else:
    print("Player is Not Allowed.");

