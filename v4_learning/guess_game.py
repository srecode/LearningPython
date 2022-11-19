"""
The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
"""

import random

guess_input = int(input("Please provide your guess: "))
correct_number = random.randint

while True:
    if guess_input > 100 or guess_input < 1:
        print("Your guess is out of bound")
        break
    elif:
        guess_input in range(correct_number-10, correct_number+10)
        print("WARM!")
        break
    elif:
        guess_input in range(correct_number-10, correct_number+10)
        print("COLD!")
        break

print(random.randint(1, 100))