from unicodedata import name


class Dog():

    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        return self.name + " says woof!!!"

class Cat():

    def __init__(self, name) -> None:
        self.name = name
    
    def speak(self):
        return self.name + " says meow!!!"


niko = Dog("Niko")
feelix = Cat("Feelix")

print(niko.speak())
print(feelix.speak())

for pet in [niko, feelix]:
    print(type(pet))
    print(pet.speak())

print(f"Nice: {type(pet)}")

def pet_speaks(pet):
    print(pet.speak())

pet_speaks(niko)
pet_speaks(feelix)