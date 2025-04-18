#Exceptions in Class

class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number: "))
        except Exception as e:
            print("User input should only be an integer")
        else:
            print(a)
        finally:
            print("Finally Block")


x = XYZ()
x.f1()