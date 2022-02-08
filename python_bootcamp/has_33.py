# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(num_list):
    for i in range(0, len(num_list) - 1):
        if num_list[i] == 3 and num_list[i+1] == 3:
            return True
    return False


print(has_33([5,2,3,3,4]))
print(has_33([1,2,3,4,5,3,3]))
print(has_33([1,2,3,4,5,3,1]))

    