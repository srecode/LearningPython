'''
This program is to print mat
'''
import random

for i in range(1,50):
    num1 = random.randint(100, 1000)
    num2 = random.randint(100, 1000)
    math_options = ['+', '-']
    random_choice = random.choice(math_options)
    if num2 > num1 and random_choice == '-':
        print (str(num2) + ' ' + random_choice + ' '   + str(num1) + ' =')
    elif num1 > num2 and random_choice == '-':
        print (str(num1) + ' ' + random_choice + ' '   + str(num2) + ' =')
    elif num1 == num2 and random_choice == '-':
        print (str(num2) + ' ' + random_choice + ' '   + str(num1) + ' =')
    else:
        print (str(num2) + ' ' + random_choice + ' '   + str(num1) + ' =')
    print ('\n')