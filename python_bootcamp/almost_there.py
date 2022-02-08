# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

def almost_there(num):
    # if (num + 10) <= 110 or (num - 10) <= 90 or (num + 10) <= 210 or (num - 10) <= 190: # garbage 

    # if num in range(90,110) or num in range(190, 210): # works
    #     return True
    # else:
    #     return False
 
    return num in range(90,110) or num in range(190, 210) # this is simple

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))