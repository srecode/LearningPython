def multi_list(lst):
    """
    Write a Python function to multiply all the numbers in a list.
    Sample List : [1, 2, 3, -4]
    Expected Output : -24
    :param lst:
    :return: x
    """
    total = 1
    for x in lst:
        total *= x
    return total

print(multi_list([1, 2, 3, -4]))