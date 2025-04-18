# ABSTRACTION
# allows us to represent complex systems by simplifying and hiding unnecessary details
# - focuses on hiding complex implementation details while exposing only the essential features of an object

'''
from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def debt(self):
        pass

class Son(Father):
    # def debt(self):
    #   print("Loan Repaid")
    #   pass
    pass

s = Son()
# The next line of code would throw error
# This is because unless the debt method of Father Class is completed
# the object creation of Son Class wont be allowed
s.debt()
'''

#----------------------------------------------

from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def debt(self):
        pass

class Son(Father):
     def debt(self):
        print("Loan Repaid")

s = Son("AK")
s.debt()
