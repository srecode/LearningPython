from time import sleep
from unicodedata import name


class Dog():
    # Class object attribute 
    # Same for any instance 
    species = 'mammal'

    def __init__(self, breed, color, name, spots):
        self.breed = breed
        self.color = color
        self.name = name
        self.spots = spots  
    
    def bark(slef):
        print("Bark!!")
    
    def about_dog(self, age):
        print (f"In general Dog is a {self.species}. This dog breed is {self.breed} and his color is {self.color} with name {self.name}. Does it have Spots? {self.spots}. It's {age} year old.")


my_dog = Dog(breed='lab',color='white', name='Johnny', spots=False)

print(type(my_dog))

# print (f"In general Dog is a {my_dog.species}. This dog breed is {my_dog.breed} and his color is {my_dog.color} with name {my_dog.name}. Does it have Spots? {my_dog.spots}")

my_dog.bark()
my_dog.about_dog(10)