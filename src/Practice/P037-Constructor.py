#Constructor
# - a constructor is a special method that is automatically called when an object is created from a class.
# - The constructor method in Python is called __init__()
# - Constructor can have unlimited arguments
#Constructor does not return anything

class Dog:
    name = None

    def __init__(self,name):
        print("I am automatically called when Object is created")
        self.name = name

    def sleep(self):
        print("I can sleep")
        print("Who is sleeping: "+self.name)

dog1 = Dog("Tom")
print(dog1.name)
dog1.sleep()
print("--------------------")

dog2 = Dog("Cooper")
print(dog2.name)
dog2.sleep()