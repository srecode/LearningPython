#interactions with functions 
from random import shuffle

ex_list = [1,2,3,4,5,6,7,8,9]
o_list = [' ', 'O', ' ']
# shuffle(ex_list)
# print(ex_list)

def shuff_list(ex_list):
    shuffle(ex_list)
    return ex_list

def my_o(o_list):
    shuffle(o_list)
    return o_list

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick up number: 0,1 or 2: ")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong")
        print(mylist)

mylist = [' ', 'O', ' ']
mix_list = shuffle(mylist)
guess = player_guess()
check_guess(mylist, guess)

        
    


    
    