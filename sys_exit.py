#This script is to  test sys.exit()

import sys

while True:
    print("Type exit to EXIT from this program")
    response = input()
    if response == 'exit':
        sys.exit()
    print("Your responce is " + response + ".")