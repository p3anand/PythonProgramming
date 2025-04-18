#How to get user input

name = input("Enter your name\n")
print("Hi", name)
print(type(name)) #data type for input function is always string


# Take input a & b from user and perform addition, multiplication & division
# Division result is always in decimal (float)
# input function's type is str. Need to convert it to int

num1 = int(input ("Enter number 1\n"))
num2 = int(input ("Enter number 2\n"))
print ("Addition Result = ",num1+num2)
print ("Subtraction Result = ",num1-num2)
print ("Multiplication Result = ",num1*num2)
print ("Division Result = ",num1/num2)

# formatting the number after decimal point
number = 3.14789025366
formated_number = f"{number:.5f}"
print(formated_number)
print("This is the number you are working with "f"{number}")

#Printing tables with the same concept
#Method 1
table = 2
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")

#Method 2 - using user input and loops
Tables_for = int(input ("Enter number \n"))
for i in range(11):
    print(f"{Tables_for}*{i}={Tables_for*i}")
    i=i+1
