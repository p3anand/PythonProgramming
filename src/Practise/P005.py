#Strings
name = "University"
print(type(name))

#str functions
print(name.upper())
print(name.lower())
print(len(name))
print(len(name)) #considers spaces also

#String Concatenation
name = "This is a sentence"
print(name)
print(type(name))

name  = name + "1"
print (name)
name = name + str (20)
print (name)

#None Type
no_of_sick_days = None
print(type(no_of_sick_days))

#ID
#Value is different -> the id is different
age1 = 10
age2 = 11
print(id(age1))
print(id(age2))

#Value is same -> the id is same since the value is same - to save memory
age3 = 13
age4 = 13
print(id(age3))
print(id(age3))