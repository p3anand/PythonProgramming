# ✅ Understanding Decorators in Python
# Decorators in Python are a powerful and flexible tool
# that allows you to modify the behavior of functions
# or methods without changing their actual code.

def my_decorator(func):
    # two parts
    # wrapper & call
    def wrapper():
        print("1.Before function is called.")
        print("2.Add Helmet, Jackets, Gloves")
        # drive_bike()
        func()
        print("3.After function is called.")
        print("4.Drove Safely")
        print("\n")
    return wrapper()

# definition
@my_decorator #this can be any annotation -> e.g @my_layers
def ridding_motorbike():
   print("Vehicle - Motorbike")

@my_decorator
def riding_cycle():
   print("Vehicle - Cycle")

#---------------------------------------------------

def add_before_and_after_ui(custom_func):
    # two parts
    # wrapper & call
    def wrapper():
        print("Before executing TC")
        print("Start the Browser!")
        custom_func()
        print("Ending execution of TC")
        print("Quit the Browser!")
    return wrapper()

@add_before_and_after_ui
def test_ui():
    print("Testing UI Components")
