"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
"""
def spy_game(lst):
    bond = [0,0,7,'x']

    for num in lst:
        if num == bond[0]:
            bond.pop(0)

    return len(bond) == 1

 print(spy_game([1,2,4,0,0,7,5]))
 print(spy_game([1,0,2,4,0,5,7]))
 print(spy_game([1,7,2,0,4,5,0]))