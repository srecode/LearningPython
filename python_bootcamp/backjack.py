# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(c1,c2,c3):

    if c1 + c2 + c3 > 21:
        return 'BUST'
    else:
        if 11 in {c1, c2, c3}:
            result = c1 + c2 + c3 
            result = result - 10
            return result
        else:
            result = c1 + c2 + c3 
    return result
            
print(blackjack(11,1,3))
print(blackjack(11, 10,5))
print(blackjack(10,10,1))
print(blackjack(5,5,5))
    