# Lambda Expressions
# A lambda is an anonymous function
# that returns some form of data.
# Syntax: lambda parameters: expression
import math


# Usual way of writing
def triple_of_num(num):
    return num ** 3

o = triple_of_num(10)
print(o)

# writing same code with lambda
o = lambda num: num ** 3
print(o(10))
# ----------------------------------------------------

# Usual way of writing
def add_10(n):
    return n + 10

o = add_10(10)
print(o)

# Using lambda expression
o = lambda n: n + 10
print(o(10))


#-----------------------------------------------------
#Addition of 3 numbers
p = lambda a,b,c: a+b+c
print(p(1,2,3))

#-----------------------------------------------------
#Even & Odd using lambda

check_even = lambda n : "Even" if n%2==0 else "Odd"
print(check_even(3))

#-----------------------------------------------------
#Getting user input & pow math function

#Usual way of writing
def pow_func(num):
    return math.pow(num,2)
op=pow_func(2)
print(op)



op2 = lambda : math.pow(int(input("Enter the number:\n")), 2)
print(op2())