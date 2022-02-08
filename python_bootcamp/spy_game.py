# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

# def spy_game(my_list):
#     my_bond = []
#     if 0 not in my_list:
#         return "No 007"
#     else:
#         for num in my_list:
#             if num in {0,0,7}:
#                 my_bond.append(num)
        
#         if my_bond == [0, 0, 7]:
#             return True
#         else:
#             return False
                    

## Efficient way 

def spy_game(nums):
    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1



print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print(spy_game([1,7,2,1,4,5,1]))