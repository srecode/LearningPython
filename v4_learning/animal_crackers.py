"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""
def animal_crackers(text):
    words = text.split()
    return words[0][0] == words[1][0]
    # print(words[0][0])

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo') )