"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""
def makes_twenty(arg1, arg2):
    if (arg1 + arg2 == 20) or arg1 == 20 or arg2 == 20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))