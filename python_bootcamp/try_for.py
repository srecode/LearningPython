# Handle the exception thrown by the code below by using try and except blocks.
#
# for i in ['a','b','c']:
#     print(i**2)
try:
    for i in ['a', 'b', 'c', 'd']:
        print(i**2)
except TypeError:
        print("We have a type error")
