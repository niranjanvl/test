'''
Vaastu
------------

  Total Site Area  : SA
Construction Area  : CA

    01.Dhana Varga     : (CA x 8) % 12
    02.Runa Varha      : (CA x 3) % 8 
    03.Vaara Varga     : (CA x 9) % 7
    04.Thidhi Varga    : (CA x 6) % 30
    05.Tatva Varga     : (CA x 3) % 5
    06.Lagna Varga     : (CA x 9) % 12
    07.Yoga Varga      : (CA x 4) % 27
    08.Graha Varga     : (CA x 5) % 9
    09.Kula Varga      : (CA x 9) % 4
    10.Kalaa Varga     : (CA x 12) % 16
    11.Nakshatra Varga : (CA x 8) % 27
    12.Aaya Varga      : (CA x 9) % 8
    13.Aayu Varga      : (CA x 9) % 120
    14.Amsha Varga     : (CA x 6) % 9
    15.Dikhpathi Varga : (CA x 9) % 8
    16.Karana Varga    : (CA x 5) % 11


Aayu Varga : if the value is < 60, then Alert (danger).
Aaya Varga : if the value is == 
                1 : then Dwajaya.
                2 : then Dhoomraya.
                3 : then Simhaya.
                4 : then Shunakaya.
                5 : then Vrushabaya.
                6 : then Kharaya.
                7 : then Gajaya.
                0 : then Kakaya.

  Total Site Area (SA) : 30x40
Construction Area (CA) : 21x29

                   (CA x 8) % 12  = Dhana Varga
                   (CA x 3) % 8   = Runa Varga
                   (CA x 9) % 7   = Vara Varga
                   (CA x 6) % 30  = Thithi Varga
                   
'''

import sys

if(len(sys.argv) < 3):
    print("Usage :\n\tvaastu.py <width> <depth>")
    exit(0)

ca_width = int(sys.argv[1])
ca_depth = int(sys.argv[2])

ca = ca_width * ca_depth

print("Total CA : {0}".format(ca))

#01.Dhana Varga     : (CA x 8) % 12
#02.Runa Varha      : (CA x 3) % 8 
#03.Vaara Varga     : (CA x 9) % 7
#04.Thidhi Varga    : (CA x 6) % 30
#05.Tatva Varga     : (CA x 3) % 5
#06.Lagna Varga     : (CA x 9) % 12
#07.Yoga Varga      : (CA x 4) % 27
#08.Graha Varga     : (CA x 5) % 9
#09.Kula Varga      : (CA x 9) % 4
#10.Kalaa Varga     : (CA x 12) % 16
#11.Nakshatra Varga : (CA x 8) % 27
#12.Aaya Varga      : (CA x 9) % 8
#13.Aayu Varga      : (CA x 9) % 120
#14.Amsha Varga     : (CA x 6) % 9
#15.Dikhpathi Varga : (CA x 9) % 8
#16.Karana Varga    : (CA x 5) % 11

def ret_default_if_zero(val, default):
	if(val == 0):
		return default
	else:
		return val

# 01.Dhana Varga     : (CA x 8) % 12
dhana_varga = ret_default_if_zero( (ca * 8) % 12, 12 )
print("Dhana Varga : {0}".format(dhana_varga))

# 02.Runa Varha      : (CA x 3) % 8
runa_varga = ret_default_if_zero( (ca * 3) % 8, 8 )
print("Runa Varga : {0}".format(runa_varga))

# 03.Vaara Varga     : (CA x 9) % 7
vaara_varga = ret_default_if_zero( (ca * 9) % 7, 7 )
print("Vaara Varga : {0}".format(vaara_varga))

# 04.Thidhi Varga    : (CA x 6) % 30
thidhi_varga = ret_default_if_zero( (ca * 6) % 30, 30 )
print("Thidhi Varga : {0}".format(thidhi_varga))

# 05.Tatva Varga     : (CA x 3) % 5
tatva_varga = ret_default_if_zero( (ca * 3) % 5, 5 )
print("tatva_varga : {0}".format(tatva_varga))

# 06.Lagna Varga     : (CA x 9) % 12
lagna_varga = ret_default_if_zero( (ca * 9) % 12, 12 )
print("lagna_varga : {0}".format(lagna_varga))

# 07.Yoga Varga      : (CA x 4) % 27
yoga_varga = ret_default_if_zero( (ca * 4) % 27, 27 )
print("yoga_varga : {0}".format(yoga_varga))

# 08.Graha Varga     : (CA x 5) % 9
graha_varga = ret_default_if_zero( (ca * 5) % 9, 9 )
print("graha_varga : {0}".format(graha_varga))

# 09.Kula Varga      : (CA x 9) % 4
kula_varga = ret_default_if_zero( (ca * 9) % 4, 4 )
print("kula_varga : {0}".format(kula_varga))

# 10.Kalaa Varga     : (CA x 12) % 16
kalaa_varga = ret_default_if_zero( (ca * 12) % 16, 16 )
print("kalaa_varga : {0}".format(kalaa_varga))

# 11.Nakshatra Varga : (CA x 8) % 27
nakshatra_varga = ret_default_if_zero( (ca * 8) % 27, 27 )
print("nakshatra_varga : {0}".format(nakshatra_varga))

# 12.Aaya Varga      : (CA x 9) % 8
aaya_varga = ret_default_if_zero( (ca*9) % 8, 8 )
print("Aaya Varga : {0}".format(aaya_varga))

# 13.Aayu Varga      : (CA x 9) % 120
aayu_varga = ret_default_if_zero( (ca*9) % 120, 120 )
print("Aayu Varga : {0}".format(aayu_varga))

# 14.Amsha Varga     : (CA x 6) % 9
amsha_varga = ret_default_if_zero( (ca * 6) % 9, 9 )
print("amsha_varga : {0}".format(amsha_varga))

# 15.Dikhpathi Varga : (CA x 9) % 8
dikhpathi_varga = ret_default_if_zero( (ca * 9) % 8, 8 )
print("Dikhpathi Varga : {0}".format(dikhpathi_varga))

# 16.Karana Varga    : (CA x 5) % 11
karana_varga = ret_default_if_zero( (ca * 5) % 11, 11 )
print("Karana Varga : {0}".format(karana_varga))

#-- Basic Paramters are done Above

print("---")

# Runa vs Dhana impact
#
if(runa_varga >= dhana_varga):
	print(" Runa Varga({0}) >= Dhana Varga({1}) !!!".format
			(runa_varga, dhana_varga) )

#
# Thithi Varga - 
#
inauspicious_thidhi_list = [1, 4, 6, 8, 9, 14, 15, 16, 19, 21, 23, 29, 30]
if( thidhi_varga in inauspicious_thidhi_list):
	print("Thidhi Varga ({0}) is Inauspicious !!!".format(thidhi_varga))


#
# Vaara Varga
#
vaara_list_ip = [
		None, #0
		"Ravi Vasara",   #1
		"Indu Vaasara",  #2
		"Bhowmya Vasara", #3
		"Sowmya Vaasara", #4
		"Bruhaspati Vasara", #5
		"Lakshmi Vaasara", #6
		"Manda Vaasara" #7
	]

inauspicious_vaara_list = [1, 3, 7]
if(vaara_varga in inauspicious_vaara_list):
	print("Vaara Varga({0}) : {1} is Inauspicious".format(
			vaara_varga, vaara_list_ip[vaara_varga]))


#
# Yoga Varga
#
yoga_list_ip = [
		None, #0
		"Vishkambha", #1
		"Preethi", #2
		"Aayushmaan", #3
		"Sowbhagya", #4
		"Shobhana", #5
		"Athiganda", #6
		"Sukarma", #7
		"Dhruthi", #8
		"Shoola", #9
		"Ganda", #10
		"Vruddhi", #11
		"Dhruva", #12
		"Vyaghatha", #13
		"Harshana", #14
		"Vajra", #15
		"Siddhi", #16
		"Vyathipaata", #17
		"Variayaan", #18
		"Parigha", #19
		"Shiva", #20
		"Siddha", #21
		"Saadhya", #22
		"Shubha", #23
		"Shukla", #24
		"Bramha", #25
		"Ayindra", #26
		"Vaidhruthi" #27
	]
inauspicious_yoga_list = [1, 6, 9, 10, 13, 15, 17, 19, 27]
if(yoga_varga in inauspicious_yoga_list):
	print("Yoga Varga({0}) : {1} is Inauspicious".format(
			yoga_varga, yoga_list_ip[yoga_varga]))


#
#Aaya Varga Classification
#
aaya_varga_ip = [
        "Kakaya",
        "Dwajaya",
        "Dhoomraya",
        "Simhaya",
        "Shunakaya",
        "Vrushabaya",
        "Kharaya",
        "Gajaya" ]
print("Aaya Varga({0}) is  {1}".format(aaya_varga, 
                                aaya_varga_ip[aaya_varga]))

#
inauspicious_aaya_list = [2, 4, 6, 8]
auspicious_aaya_list = [1,5]
if( aaya_varga in inauspicious_aaya_list):
	print("Aaya Varga ({0}) is Inauspicious !!!".format(aaya_varga))
elif( aaya_varga in auspicious_aaya_list):
	print("Aaya Varga({0}) is Very Auspicious !!!".format(aaya_varga))

#
# Aayu Varga
#

if(aayu_varga < 60):
	print("Aayu Varga ({0}) < 60 !!!".format(aaya_varga))


#
# Amsha Varga
#
amsha_varga_ip = [
		"Good",   #0
		"Nashtaha", #1
		"Good", #2
		"Good", #3
		"Shaapaha", #4
		"Maranaha", #5
		"Choraha", #6
		"Good", #7
		"Good", #8
		"Good" #9
	]

if(amsha_varga_ip[amsha_varga] != "Good"):
	print("Amsha Varga({0}) is {1}".format(
			amsha_varga,
			amsha_varga_ip[amsha_varga]))





