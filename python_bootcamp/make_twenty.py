def make_twenty(num1, num2):
    if num1 == 20 or num2 == 20:
        return True
    elif sum([num1,num2]) == 20:
        return True
    else:
        return False

print(make_twenty(9, 11))
        
#Single line

def make_twenty(num1, num2):
    return num1 + num2 == 20 or num1 == 20 or num2 == 20

print(make_twenty(9, 13))
    