# for i in ['a', 'b', 'c', 'd']:
#     try:
#         print(i ** 2)
#     except TypeError:
#         print("You have a TypeError")
#     finally:
#         print("This is finally")

#Also can be written as

try:
    for i in ['a', 'b', 'c', 'd']:
        print(i ** 2)
except:
    print("An error occured")