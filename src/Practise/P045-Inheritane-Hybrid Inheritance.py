# HYBRID INHERITANCE
# A combination of multiple inheritance and multilevel inheritance.

class A:
    def methodA(self):
        return "Method A"


class B(A):  # Single Inheritance
    def methodB(self):
        return "Method B"


class C(A):  # Hierarchical Inheritance
    def methodC(self):
        return "Method C"


class D(B, C):  # Multiple Inheritance
    def methodD(self):
        return "Method D"

d= D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())