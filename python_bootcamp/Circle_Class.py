from math import radians
from turtle import circle


class CircleClass():
    # Class Object Attribute 
    pi = 3.14 
    def __init__(self, radius=2):
        self.radius = radius
        self.area = radius * radius * CircleClass.pi
    
    def get_circumfrence(self):
        return round(self.radius * CircleClass.pi * 2, 2)

        
    def about_circle(self):
        print(f"this Circle has radius of {self.radius} with area {self.area}")


my_circle = CircleClass(12)

# print(my_circle.radius)

print(my_circle.get_circumfrence())

my_circle.about_circle()
print(my_circle.area)