import random

def guessNumber():
    print("Guess nuber between 1 to 100")
    randNum = random.randint(1,100)
    while True:
        guess =  input()
        if randNum < guess:
            print("Guess is too high") 
            continue
        elif randNum > guess:
            print("Guess is too low")
            continue
        else:
            print("You are right")
            break
        

guessNumber()