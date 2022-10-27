# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

from re import L

from pyrsistent import l


def uniq_list(l):
    return set(l)

l = [1,1,1,1,2,2,3,3,3,3,4,5]

print(uniq_list(l))

