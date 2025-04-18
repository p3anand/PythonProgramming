# MULTIPLE INHERITANCE
# A class inherits from multiple base classes.

class Father:

    def father_share(self):
        return 5000

    def apartment(self):
        return "From Father"

class Mother:
    def mother_share(self):
        return 2000

    def apartment(self):
        return "From Mother"

class Son1(Mother, Father):  # MRO - Method resolution Order
    pass

class Son2(Father, Mother):
   pass

s1 = Son1()
print(s1.father_share())
print(s1.mother_share())
print(s1.apartment())
s2 = Son2()
print(s2.apartment())