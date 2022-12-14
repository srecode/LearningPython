def square():
    while True:
        try:
            num = int(input("Please enter nuber for square result: "))
            result = (num * num)
        except:
            print("This is a ValueError")
            continue
        else:
            print(f"Square of {num} is {result}")
            break
        finally:
            print("This always runs")

square()