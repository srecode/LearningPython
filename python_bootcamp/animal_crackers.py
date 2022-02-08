# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# def animal_crackers(string): # didn't work
#     return set('{1}'.format(([s[0] for s in string.split()])))

def animal_crackers(string):
    word_list = string.lower().split()
    return word_list[0][0] == word_list[1][0]
    

print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Sam Ram"))
    