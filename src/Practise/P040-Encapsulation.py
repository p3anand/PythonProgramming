# ENCAPSULATION
# - Wrapping or binding the data variables with the methods - Encapsulation.
# - Refers to the bundling of data and methods that operate on that data within a single unit, or object.
# - Encapsulation helps to promote the principle of "data hiding".
# - This is achieved by declaring the object's data fields as private
# and providing public getter and setter methods to access and modify the data.


class myClass:
    # public var (instance)
    public_var = "I am PUBLIC"
    a = 5

    # private variable
    __private_var = "I am PRIVATE"
    __b = 10

    # protected variable
    _protected_var = "I am PROTECTED"
    _c = 15


object = myClass()
print(object.public_var)
print(object.a)
# print(object.__private_var) #this will throw error when executed.
print(object._protected_var)
print(object._c)
print("------------------------")


# ---------------------------------------
# Example

class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed!")

    def __internal_method(self):
        print("Private Method")
        print(self.__account_number)
        self.show_me_account_number()


b1 = Bank(9876543210, 100)
b1.deposit(100)
b1.check_balance()
b1.show_me_account_number(True)
b1.deposit(100)
b1.check_balance()
