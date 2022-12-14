def divide():
    x = 5
    y = 0
    try:
        z = x / y
    except ZeroDivisionError:
        print("We found an exception")
    finally:
        print("This finally prints")

divide()