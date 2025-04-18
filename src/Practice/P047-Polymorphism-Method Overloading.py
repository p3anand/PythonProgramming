# Method Overloading:
# Python does not support method overloading
# in traditional way

class MathUtils(object):  # is- A object - single inheritanace

    def add(self, a, b):
       return a + b

    def add(self, a, b, c):
        return a + b + c

math = MathUtils()
op1 = math.add(1, 2) #Method Overloading is not supported here
print(op1)

#---------------------------------------
# Method Overloading is supported here.
# Third addition method is executed.

class MUtils(object):  # is- A object - single inheritance

    def addition(self, a, b):
       return a + b

    def addition(self, a, b, c):
        return a + b + c

    def addition(self, a, b, c=10, d=1):
        return a + b + c + d

m = MUtils()
op1 = m.addition(1, 2) #Method Overloading is supported here
print(op1)