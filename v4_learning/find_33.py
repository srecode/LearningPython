"""
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

def find_33(arg1):
    for i in range(0, len(arg1) - 1):
        if arg1[i:i+2] == [3,3]:
            print(i, i+4)
            return True
    return False
            # print(f"After if ",  i, i + 2)
print(find_33([1, 3, 3]))
print(find_33([1, 3, 1, 3]))
print(find_33([3, 1, 3]))


# def has_33(nums):
#     for i in range(0, len(nums) - 1):
#
#         # nicer looking alternative in commented code
#         # if nums[i] == 3 and nums[i+1] == 3:
#
#         if nums[i:i + 2] == [3, 3]:
#             return True
#
#     return False