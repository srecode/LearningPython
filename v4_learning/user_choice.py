# from ipython.display import clear_output

def user_choice():
    choice = 'wrong'

    while choice not in ['0','1','2']:
        choice = input("Please enter a integer (0,1,2): ")
        if choice not in ['0','1','2']:
            # clear_output()
            print("Sorry, please enter a integer value")

    return int(choice)

print(user_choice())