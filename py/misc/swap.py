'''
Given two variable swap their values
i.e.,
    n = 10
    m = 12
    print("m : {0}, n : {1}".format(m,n))
        --> m : 10, n : 12
    #-    
    #TODO : Swap values of m and n
    #-
    print("m : {0}, n : {1}".format(m,n))
        --> m : 12, n : 10
'''

n = 12
m = 10
print("m : {0}, n : {1}".format(m,n))

#-    
# Swap values of m and n
#-

#-- begin your code - cant use constants like 10, 12.
#   only variables and logic is permitted
if m != n:
    temp = n
    n = m
    m = temp

print("m : {0}, n : {1}".format(m,n))

#python supports the below
if m != n:
    m, n = n, m
print("m : {0}, n : {1}".format(m,n))

