#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            n = int(input("Ask for 'init' input: "))
        except:
            print("Not an 'int', I am going to ask again")
            continue
        else:
            print("Thanks for providing number")
            print(n**2)
            break

if __name__ == '__main__':
    ask()