# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Method Overriding - Child/Sun class can have same method name as parent/super class
# Super keyword  calls the parent's method/attribute

class Shape():
    a = 50
    def area(self):
        print("Area of Shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        super().area()
        print(super().a)
        return 3.14* self.radius * self.radius

r1 = Rectangle(3,4)
print(r1.area()) #local method is called since it has higher preference

c1= Circle(10)
print(c1.area())
