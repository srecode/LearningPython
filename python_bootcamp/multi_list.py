# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multi_list(lst):
    r_lst  = 1
    for i in lst:
        r_lst = i * r_lst
    return r_lst

lst = [1, 2, 3, -4, 2]
print(multi_list(lst))