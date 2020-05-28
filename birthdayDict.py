#this is script is to practice dict values

def birthdaayDict():
    birthdays = {'Sam': 'Sep 1', 'Ram': 'Sep2', 'Gam': 'Sep 3'}

    while True:
        print("Enter your name, (Enter plant to quit")
        name = input()
        if name == ' ':
            break

        if name in birthdays:
            print(birthdays[name] + " is " + name + "'s Birthday...Happy Birthday " + name)
        else:
            print("I don't have birthday information of " + name)
            print("Please enter information")
            bday = input()
            birthdays[name] = bday
            print("Birthday DB updated.")

birthdaayDict()