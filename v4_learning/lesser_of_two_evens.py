"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""

def lesser_of_two_evens(arg1, arg2):
    if arg1 % 2 == 0 and arg2 % 2 == 0:
        if arg1 > arg2:
            return arg2
        else:
            return arg1
    else:
        if arg1 > arg2:
            return arg1
        else:
            return arg2

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

#also can be writter as

def lesser_of_two_evens_v2(arg1, arg2):
    if arg1 % 2 == 0 and arg2 % 2 == 0:
        return min(arg1, arg2)
    else:
        return max(arg1, arg2)

print(lesser_of_two_evens_v2(2,4))
print(lesser_of_two_evens_v2(2,5))