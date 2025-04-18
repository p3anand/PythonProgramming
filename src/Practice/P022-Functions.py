#FUNCTIONS

# With no return type + no arguments
def greet_one():
    print("Hello There")

def greet_all():
    print("Hello All")
    greet_one()

result = greet_all()
print(result)
print("-------------")

# With Default Arguments + No return type
def say_hello_default_args(name = "Henry"):
    print("Hello ",name)
say_hello_default_args("Rose")
say_hello_default_args()
say_hello_default_args(name = "Mike")
print("-------------")


# With Arguments + No return
def greet_by_name(name):
    print("Hello ",name)

greet_by_name("Jack")
greet_by_name("3.56")
print("-------------")

#FUNCTIONS - Taking input from user
def greet(x):
    print("Hello ",x)

x= input("Enter your name\n")
greet(x)
print("-------------")

# With Argument + Return Type
def sum_of_two_numbers(n1,n2):
    return n1+n2

result = sum_of_two_numbers(10,20)
print(result)
print("-------------")

# With Default Argument + Return Type
def sum_of_two_numbers_default(n3=100,n4=200):
    return n3+n4

result= sum_of_two_numbers_default()
print(result)
print("-------------")

# With *args
def print_arguments(*args):
    print(args[1])
print_arguments("a","Test","456","d","e", True, False)
