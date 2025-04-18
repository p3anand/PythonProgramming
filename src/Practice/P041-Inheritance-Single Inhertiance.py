# INHERITANCE
# Allows a class (child class) to inherit attributes and methods from parent class
# Types -> Single, Muliple, Multi Level, Hybrid & Hierarchical

# SINGLE INHERITANCE
# A class inherits from a single base class.
class Father:
    key1 = "Apartment 1"

    def car(self):
        print("Father's Car")

class Son(Father):
    key2 = "Apartment 2"

    def truck(self):
        print("Son's Truck")


father_obj = Father()
father_obj.car()
son_obj = Son()
son_obj.car()



