def unique_list(lst):
    """
    Write a Python function that takes a list and returns a new list with unique elements of the first list.

    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]
    :return:
    """
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

s_lst = [1,1,1,1,2,2,3,3,3,3,4,5]

print(unique_list(s_lst))