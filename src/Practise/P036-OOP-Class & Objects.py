# OOPS
# Attributes are called as → properties | Data variables.
# Behavior are also called as → Methods(functions) | Data members | Member functions.
# First argument of method is always self

class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behavior
    def talk(self):  # No Argument No Return
        print("I can talk")

    def sleep1(self, name):  # Argument with No Return
        print("I am sleep Method")
        print("Sleep", name)

    def sleep2(self, name):  # Argument with Return
        print("I am a Method")
        return None

    def walk_return(self):  # No Argument with Return
        return "I can walk"


# Creating objects
martin = Person()
martin.name = "Martin"
print(martin.name)
martin.sleep1("Martin")

max = Person()
max.name = "Max"
print(max.name)
max.sleep1("Max")
