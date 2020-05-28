def devideByZero(GivenNumber):
    try:
        return 22 / GivenNumber
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(devideByZero(2))
print(devideByZero(22))
print(devideByZero(10))
print(devideByZero(0))
print(devideByZero(10))
