#this program ramdomly prints numbers

import random

def listMagic8():
    message = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    print(message[random.randint(0, len(message) -1 )])

listMagic8()