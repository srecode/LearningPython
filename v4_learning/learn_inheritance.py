class Animal():
    """
    This Class just prints
    """
    def __init__(self):
        print("Just print Animal")
    def who_am_i(self):
        print("I am an Animal")
    def eat(self):
        print("Please Eat")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        Animal.eat(self)
        print("Doc Created")

    def who_am_i(self):
        print("I am a Dog!")

    def bark(self):
        print("WOOF!!!!")

my_animal = Animal()

my_animal.who_am_i()
my_animal.eat()

my_dog = Dog()
my_dog.who_am_i()
my_dog.bark()