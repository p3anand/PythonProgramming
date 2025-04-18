#import keyword
#print(keyword.kwlist)

#VARIABLE
age = 10
print (age)
print (type(age))

pi=3.14
name = "PREETHI"
isFemale = False
print (type(pi))
print (type(name))
print (type(isFemale))

complex_number = 2+3j
print(complex_number.real)
print(complex_number.imag)

#IDENTIFIERS
a=10
_ = 45
print(_)
_ = _+10
print(_)

#Changing Datatypes of Variables -> Dynamic
age = 45
age = "Forty Five"
print(age)

#Working with variable
a = 10
b = 20
c = 30
sum = a + b + c
sum = sum - 10
sum = sum + 20
print (sum)
sum-70 #The result is not assigned to the variable sum
print(sum)

# Ways of creating & initializing variables
a, b, c = 45, 54, 67
print (a, b, c, sep = '-')