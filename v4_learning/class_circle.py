class Circle():
    """
    This class takes radius and give circumference of the Circle
    """
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
        self.area   = radius*radius*Circle.pi

    def circumference(self):
        return self.radius * 2 * Circle.pi


my_circle = Circle(30)

print(my_circle.circumference())
print(my_circle.area)

