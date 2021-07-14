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
from colorama import Fore

if(len(sys.argv) < 5):
    print("Usage :\n\tvaastu.py <building width> <building depth> <site width> <site depth>")
    exit(0)

ca_width = int(sys.argv[1])
ca_depth = int(sys.argv[2])

sa_width = int(sys.argv[3])
sa_depth = int(sys.argv[4])

ca = ca_width * ca_depth
sa = sa_width * sa_depth

print("Total CA : {0}".format(ca))
print("Total SA : {0}".format(sa))
set_back = (sa - ca)*100.0/(sa)

if( ca == sa ):
    print("Not recommended as there is no Set Back")
elif (set_back < 20):
    print("Not recommended as the Set Back is < 20%")


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
print("Dhana Varga    : {0}".format(dhana_varga))

# 02.Runa Varha      : (CA x 3) % 8
runa_varga = ret_default_if_zero( (ca * 3) % 8, 8 )
print("Runa Varga     : {0}".format(runa_varga))

# 03.Vaara Varga     : (CA x 9) % 7
vaara_varga = ret_default_if_zero( (ca * 9) % 7, 7 )
print("Vaara Varga    : {0}".format(vaara_varga))

# 04.Thidhi Varga    : (CA x 6) % 30
thidhi_varga = ret_default_if_zero( (ca * 6) % 30, 30 )
print("Thidhi Varga   : {0}".format(thidhi_varga))

# 05.Tatva Varga     : (CA x 3) % 5
tatva_varga = ret_default_if_zero( (ca * 3) % 5, 5 )
print("Tatva Varga    : {0}".format(tatva_varga))

# 06.Lagna Varga     : (CA x 9) % 12
lagna_varga = ret_default_if_zero( (ca * 9) % 12, 12 )
print("Lagna Varga    : {0}".format(lagna_varga))

# 07.Yoga Varga      : (CA x 4) % 27
yoga_varga = ret_default_if_zero( (ca * 4) % 27, 27 )
print("Yoga Varga     : {0}".format(yoga_varga))

# 08.Graha Varga     : (CA x 5) % 9
graha_varga = ret_default_if_zero( (ca * 5) % 9, 9 )
print("Graha Varga    : {0}".format(graha_varga))

# 09.Kula Varga      : (CA x 9) % 4
kula_varga = ret_default_if_zero( (ca * 9) % 4, 4 )
print("Kula Varga     : {0}".format(kula_varga))

# 10.Kalaa Varga     : (CA x 12) % 16
kalaa_varga = ret_default_if_zero( (ca * 12) % 16, 16 )
print("Kalaa Varga    : {0}".format(kalaa_varga))

# 11.Nakshatra Varga : (CA x 8) % 27
nakshatra_varga = ret_default_if_zero( (ca * 8) % 27, 27 )
print("Nakshatra Varga : {0}".format(nakshatra_varga))

# 12.Aaya Varga      : (CA x 9) % 8
aaya_varga = ret_default_if_zero( (ca*9) % 8, 8 )
print("Aaya Varga     : {0}".format(aaya_varga))

# 13.Aayu Varga      : (CA x 9) % 120
aayu_varga = ret_default_if_zero( (ca*9) % 120, 120 )
print("Aayu Varga     : {0}".format(aayu_varga))

# 14.Amsha Varga     : (CA x 6) % 9
amsha_varga = ret_default_if_zero( (ca * 6) % 9, 9 )
print("Amsha Varga    : {0}".format(amsha_varga))

# 15.Dikhpathi Varga : (CA x 9) % 8
dikhpathi_varga = ret_default_if_zero( (ca * 9) % 8, 8 )
print("Dikhpathi Varga : {0}".format(dikhpathi_varga))

# 16.Karana Varga    : (CA x 5) % 11
karana_varga = ret_default_if_zero( (ca * 5) % 11, 11 )
print("Karana Varga    : {0}".format(karana_varga))

#-- Basic Paramters are done Above

print("---")

# Runa vs Dhana impact
#
if(runa_varga >= dhana_varga):
    print((Fore.RED+"Runa Varga({0}) >= Dhana Varga({1}) !!!"+Fore.BLACK).
            format(runa_varga, dhana_varga) )

#
# Thithi Varga - 
#
inauspicious_thidhi_list = [1, 15, 16, 30]
if( thidhi_varga in inauspicious_thidhi_list):
    print((Fore.RED+"Thidhi Varga ({0}) is Inauspicious !!!"+Fore.BLACK).
            format(thidhi_varga))


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
	print((Fore.RED+"Vaara Varga({0}) : {1} is Inauspicious"+Fore.BLACK).format(
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
	print((Fore.RED+"Yoga Varga({0}) : {1} is Inauspicious"+Fore.BLACK).format(
			yoga_varga, yoga_list_ip[yoga_varga]))


#
#Aaya Varga Classification
#
aaya_varga_ip = [
        None, #0
        "Dwajaya", #1
        "Dhoomraya", #2
        "Simhaya", #3
        "Shunakaya", #4
        "Vrushabaya", #5
        "Kharaya", #6
        "Gajaya", #7
        "Kakaya"
        ]
print("Aaya Varga({0}) is {1}".format(aaya_varga, 
                                aaya_varga_ip[aaya_varga]))

#
inauspicious_aaya_list = [2, 4, 6, 8]
auspicious_aaya_list = [1,5]
if( aaya_varga in inauspicious_aaya_list):
	print((Fore.RED+"Aaya Varga ({0}) is Inauspicious !!!"+Fore.BLACK).format(aaya_varga))
elif( aaya_varga in auspicious_aaya_list):
	print((Fore.GREEN+"Aaya Varga({0}) is Very Auspicious !!!"+Fore.BLACK).format(aaya_varga))

#
# Aayu Varga
#

if(aayu_varga < 60):
	print((Fore.RED+"Aayu Varga ({0}) < 60 !!!"+Fore.BLACK).format(aaya_varga))


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




#
# Dikhpathi Varga
#
dikhpathi_varga_ip = [
		None,   #0
		"Indra", #1
		"Agni", #2
		"Yama", #3
		"Nirruti", #4
		"Varuna", #5
		"Aayu", #6
		"Kubhera", #7
		"Eeshana", #8
	]


auspicious_dikpathi_list = [ 1,5 ]
if( dikhpathi_varga in auspicious_dikpathi_list ):
    print("Dikhpathi Varga({0}) is very auspicious.".
            format(dikhpathi_varga_ip[dikhpathi_varga]))


#
# Karana Varga
#

karana_varga_ip = [
            None, #0
            "Bhava", #1
            "Balava", #2
            "Kaulava", #3
            "Thaitale", #4
            "Garaje", #5
            "Vanik", #6
            "Bhadre", #7
            "Shakuni", #8
            "Chatushpath", #9
            "Naagavaan", #10
            "Kimstughna", #11
        ]

auspicious_karana_varga = [ 1, 2, 3, 4 ]

if(karana_varga not in auspicious_karana_varga):
    print((Fore.RED+"Karana Varaga({0}) is inauspicious !!!"+Fore.BLACK).
            format(karana_varga_ip[karana_varga]))


