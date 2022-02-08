# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 ==0:
        if num1 < num2:
            result = num1
        else:
            result = num2
    else:
        if num1 > num2:
            result = num1
        else:
            result = num2

            
    
    return result

print(lesser_of_two_evens(14,2))

# minimizing the code

def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 ==0:
        return min(num1, num2) # removing variable "result" will reduce the number of lines in code executes it without having to run all the code
    else:
        return max(num1, num2)

print(lesser_of_two_evens(14,21))