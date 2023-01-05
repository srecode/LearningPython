# def hello(name='Sam'):
#     return 'Hello ' + name
#
# print(hello())
#
# greet = hello
#
# print(greet)
# print(greet())
#
# del hello
#
# print(hello())

# def hello(name='Sam'):
#     print("The hello() function has been executed")
#
#     def greet():
#         return "\t This is inside greet() function"
#
#     def welcome():
#         return "\t This is inside welcome() function"
#
#     if name == 'Dam':
#         return greet
#     else:
#         return welcome
#
# x = hello()
# print(x)

def hello():
    return "Hi Sam"

def other(func):
    print("This is inside other()")
    print(func())

other(hello)