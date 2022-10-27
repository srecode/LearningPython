def add_number(num1, num2):
    num2 = input("Please provide number: ")
    try:
        print(num1+num2)
    except:
        print("Please add numbers not strings")
    else:
        print("Add went well")
    finally:
        print("print this anyway")



if __name__ == '__main__':
    add_number(10,10)