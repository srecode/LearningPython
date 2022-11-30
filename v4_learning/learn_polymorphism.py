class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " Says WOOF!!!"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " Says MEOW!!!"

sam = Dog("Sam")
cam = Cat("Cam")

for pet in [sam, cam]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    return pet.speak()

print(pet_speak(sam))
print(pet_speak(cam))