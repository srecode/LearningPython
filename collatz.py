#This program prints number // 2 if the number is even
# 3 * number + 1 if the number is odd

def collatz(givenNumber):
    # print ("Please provide input")
    # givenNumber = input()
    print("Given input " + str(givenNumber))
    try:
        if givenNumber % 2 == 0:
            return givenNumber // 2
        else:
            return 3 * givenNumber + 1
    except TypeError:
        print("Not a numaric input") 

print(collatz(20))
print(collatz(21))
print(collatz('sam'))
print(collatz(30))