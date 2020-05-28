#This script is to learn return in function

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "it's 1"
    elif answerNumber == 2:
        return "it's 2"
    elif answerNumber == 3:
        return "it's 3"
    elif answerNumber == 4:
        return "It's 4"
    elif answerNumber == 5:
        return "It's 5"
    elif answerNumber == 6:
        return "It's 6"
    elif answerNumber == 7:
        return "It's 7"
    elif answerNumber == 8:
        return "It's 8"
    elif answerNumber == 9:
        return "it's 9"

#r will get random numbers from 1 to 9
r = random.randint(1,9)
#fortune is new variable which gets value assigned from getAnswer returns 
#based on the random number it got
fortune = getAnswer(r)
print(fortune)

# #you can write above in single line like this
# print(getAnswer(random.randint(1,9)))