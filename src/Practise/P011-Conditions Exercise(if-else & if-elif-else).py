# CONDITIONS
# IF ELSE LOOP

# Find if user is eligible to vote using if-else loops
age = int(input("Enter your age:\n"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

print("----------------------------------")

# Program to find max of two numbers (float) using if-else loop
n1 = float(input("Enter number 1:\n"))
n2 = float(input("Enter number 2:\n"))

if n1 > n2:
    print("Max is ", n1)
else:
    print("Max is ", n2)

print("----------------------------------")

#IF ELIF ELSE LOOP
# Program to find max of three numbers (int) using loops
x1 = int(input("Enter number 1:\n"))
x2 = int(input("Enter number 2:\n"))
x3 = int(input("Enter number 3:\n"))

if x1 > x2 and x1 > x3:
    print("Max number is ", x1)
elif x2 > x1 and x2 > x3:
    print("Max number is ", x2)
else:
    print("Max number is ", x3)

print("----------------------------------")
