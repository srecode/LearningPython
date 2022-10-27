def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Not 'int', I am going to ask again")
            continue
        else:
            print("Thank you!!!")
            break
        # finally:
        #     print("print this anyway")

if __name__ == '__main__':
    ask_for_int()