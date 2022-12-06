class Animal():
    def __init__(self, name ):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method only")

class Dog(Animal):
    def speak(self):
        return self.name + " Says WOOF!!!"

class Cat(Animal):
    def speak(self):
        return self.name + " Says MEAO!!!"


sam = Dog('Sam')
dam = Cat('Dam')

print(sam.speak())
print(dam.speak())