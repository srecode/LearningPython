#This script it to generate two random numbers and add them
#and compare respose from user to see if he is right

# import random
# for i in range(1,100):
#     num1 = random.randint(1, 100)
#     num2 = random.randint(1, 100)
#     print str(num1) + str num2

import random


score = 0

player_name = input('Enter your name: ')
    
for i in range(50):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    math_options = ['+', '-']
    random_choice = random.choice(math_options)
    if num2 > num1 and random_choice == '-':
        print ("What is " + str(num2) + random_choice  + str(num1))
        answer = num2 - num1
    elif num1 > num2 and random_choice == '-':
        print ("What is " + str(num1) + random_choice  + str(num2))
        answer = num1 - num2
    elif num1 == num2 and random_choice == '-':
        print ("What is " + str(num1) + random_choice  + str(num2))
        answer = num1 - num2
    else:
        print ("What is " + str(num1) + random_choice + str(num2))
        answer = num1 + num2

    while True:
        yourAnswer = int(input())

        if answer != yourAnswer:
            print ("Nope, " + str(player_name) + ", your current score is : " + str(score))
            score -= 1
            continue
        else:
            score += 1
            print ("Awesome " + str(player_name) + ", your current score is : " + str(score))
            break

    

# answer = num1 + num2

# while True:
#     yourAnswer = int(input())

#     if answer != yourAnswer:
#         print ("Nope Ista")
#         continue
#     else:
#         print  ("Awesome Ista, great job!!!!")
#         break
