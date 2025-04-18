# HIERARCHICAL INHERITANCE
# Multiple derived classes inherit from a single base class.

class Father():
    def house(self):
        print("Father's House")

class Son1(Father):
    def apartment(self):
        print("Son 1's Apartment")

class Son2(Father):
    def vehicle(self):
        print("Son 2's Vehicle")

s1 = Son1()
s1.house()
s2 = Son2()
s2.house()