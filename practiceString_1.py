#this code check if the input is alph if not it asks untill
#it's alpha

# def checkAlpha():
#     while True:
#         print("Please enter your age")
#         age = input()
#         if age.isdecimal():
#             break
#         print("Please enter your age in numarics")

# checkAlpha()

def checkPassword():
    while True:
        print("Give me your password")
        password = input()
        if password.isalnum():
            break
        print("Please only use alph and num for password")

checkPassword()