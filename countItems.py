#this is to count items from dictionary

allGuests = {'sam': {'apples': 5, 'pineapples': 10},
             'Ram': {'gold': 10, 'silver': 5},
             'Kam': {'apples': 22, 'gold': 11},
             'Pri': {'pineapples': 22, 'silver': 11, 'mine': 99},
             'Ista': {'silver': 33, 'gold': 11}}

def totalBought(guests, items):
    numBought = 0

    for k, v in guests.items():
        numBought = numBought + v.get(items, 0)
    
    return numBought

print('Number of things bought')
print('--Apples ' + str(totalBought(allGuests, 'apples')))
print('--PineApples ' + str(totalBought(allGuests, 'pineapples')))
print('--Gold ' + str(totalBought(allGuests, 'gold')))
print('--Silver ' + str(totalBought(allGuests, 'silver')))
print('--Mine ' + str(totalBought(allGuests, 'mine')))