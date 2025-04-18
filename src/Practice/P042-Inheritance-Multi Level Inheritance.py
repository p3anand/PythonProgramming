# MULTI LEVEL INHERITANCE
# A class inherits from a derived class, forming a hierarchy of inheritance.

class GrandFather():
    plot = " One "

    def truck(self):
        print("Truck")

class Father(GrandFather):
    house = "Two"

    def car(self):
        print("Car")

class Son(Father):
    apartment = "Three"

    def camper(self):
        print("Camper Van")

s = Son()
s.camper()
s.car()
s.truck()
print("-----------")
f= Father()
f.car()
f.truck()
