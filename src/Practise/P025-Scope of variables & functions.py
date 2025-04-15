#Scope of Variable
global_a = 12 #global variable

def my_function():
    a = 10 #local variable
    print(a)
    print(global_a)

my_function()
print(global_a)

#Functions Within Functions
def outer_function():
    var1= 40

    def inner_function1():
        print(var1)
    def inner_function2():
        print(var1)

    inner_function1()
    inner_function2()

outer_function()