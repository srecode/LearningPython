class Dog():
    def __init__(self, name, breed, spots):
        self.name  = name
        self.breed = breed
        self.spots = spots

    def bark(self, number):
        print("Woff, my name is {} and number is {}".format(self.name, number))


my_dog = Dog(name='Sam', breed='Lab', spots=False)

print(my_dog.name)
my_dog.bark(10)