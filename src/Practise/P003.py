#Math Functions
a =pow (2,3)
print (a)

b = abs (-10) #absolute value of -10 would be 10 (gives positive number)
print (b)

#LITERALS
a = 10 #integer
b = 'c' #char
c = 'Hello' #str
pi = 3.14 #char
are_you_learner = True #boolean
complex_number = 1+8j #j is root of 1 #

# Special literal
drink = "Available"
food = None


def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)


menu(drink)
menu(food)

# Advanced Literal Collections
fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

