class Dog():
    def __init__(self,name):
        self.name = name

    def bark(self):
        return self.name + " says WOOF!!!"

class Cat():
    def __init__(self, name):
        self.name = name

    def bark(self):
        return self.name + " says MEAO!!!"

sam = Dog('Sam')
dam = Cat('Dam')

print(sam.bark())
print(dam.bark())

for pet in [sam, dam]:
    print(pet.bark())

def pet_speak(pet):
    print(pet.bark())

pet_speak(sam)
pet_speak(dam)