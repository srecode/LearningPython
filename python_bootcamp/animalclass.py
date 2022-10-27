class Animal():

    def __init__(self) -> None:
        print("Animal Class Created")

    def who_am_i(self):
        print("I am Animal")

    def eat(slef):
        print("I am eating")

my_animal = Animal()

my_animal.who_am_i()
my_animal.eat()

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        # return super().who_am_i()
        print("I am a Dog!!!")
    
    def eat(self):
        print("Dog is eating!!!")

    def bark(self):
        print("WOOF!!")

my_dog = Dog()

my_dog.who_am_i()
my_dog.eat()
my_dog.bark()