# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
#
# x = 5
# y = 0
#
# z = x/y

def zero_division(x, y):
    z = 0
    try:
        z = x/y
    except ZeroDivisionError:
        print("Getting ZeroDivisionError error")
    return z

if __name__ == '__main__':
    print(zero_division(5,0))