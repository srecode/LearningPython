def user_choice():
    choice = 'WRONG'
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter your input (1-10): ")
        if choice.isdigit() == False:
            print("Sorry, please enter a digit")
        if choice.isdigit() == True:
            if int(choice) in range(1,10):
                within_range = True
            else:
                print("Please enter value with in range(1..10)")
                within_range = False

    return int(choice)

print(user_choice())