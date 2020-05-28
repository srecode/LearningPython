#This script is to pratice list

def getDogList():
    dogNames = []
    while True:
        print("Please enter Dog names here")
        try:
            name = str(input())
            if name == ' ':
                break
            dogNames  = dogNames + [name]
        except (SyntaxError):
            print("Empty input, if you are done please give ' ' as input")
        except (NameError):
            print("Not a string")
    print("Dog names are")
    for dogName in dogNames:
        print(' ' + dogName)

getDogList()