def ask_for_int():
    while True:
        try:
            result = int(input("Please enter a number: "))
        except:
            print("It doesn't look like a number, please enter a number")
            continue
        else:
            print(f"We got number {result}, thank you")
            break
        finally:
            print("I always run")

ask_for_int()