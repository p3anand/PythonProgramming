# STATIC METHODS
# A static method is a method that belongs to a class rather than an object
#Does not require object creation. Should be called along with class name.
class MathOperations():

    def div(self,a,b):
        return a/b

    @staticmethod
    def sum(a,b):     #Static Method
        return a+b

o = MathOperations()
output=o.div(10,5)
print(output)

#Static Method can be called directly without object
print(MathOperations.sum(4,5))