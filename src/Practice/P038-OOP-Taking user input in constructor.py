# Create an Employee Class
# Attributes -> Name, age, phone number, address, Eid
# Methods -> Walk, Talk, Print
# Create a constructor to set values
# Ask user about information for two objects - E1 & E2
# Print details of E1 and E2 through print function

class Employee:
    name = None
    age = None
    contact_number = None
    address = None
    EID = None

    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.contact_number = input("Enter your contact number: ")
        self.address = input("Enter your address: ")
        self.EID = input("Enter your ID: ")

    def walk(self):
        print("Walk method")

    def talk(self):
        print("Talk Method")

    def print_details(self):
        print("--------------------")
        print("Employee Details")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Contact Number: ", self.contact_number)
        print("Address: ", self.address)
        print("EID: ", self.EID)
        print("--------------------")

E1 = Employee()
E1.print_details()
