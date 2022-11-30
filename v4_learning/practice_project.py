"""
Getting User Input
Creating Functions that edit variables based on user input
Generating output
Joining User Inputs and Logic Flow
"""
def display_mylist(mylist):
    return mylist

print(display_mylist([1,2,3,4,5]))

result = int(input('Please enter a value: '))
print(result)
print(type(result))
print(type(int(result)))

some_input = '10'

print((some_input.isdigit()))