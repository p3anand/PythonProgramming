# User Defined (Custom) Exceptions

class MyCustomExceptions(Exception):

    def __init__(self,message):
        self.message=message
        super().__init__(message) #Parent constructor is called


balance = 100
withdraw = int(input("Enter the amount to be withdrawn: "))
if withdraw > balance:
    raise MyCustomExceptions("Balance is Low")
else:
    print("Remaining Balance: ",(balance-withdraw))