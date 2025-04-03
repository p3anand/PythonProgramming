#Operator
print(5//2) # Gives Quotient
print(5%2)  # Gives Remainder
print(4**2) # power
print(2==3) #compare
is_today_weekend = False
print(not is_today_weekend) #not operator

#Logical operators
x = 10
y = 20
print(x>y)
print(x<y)

a=10
b=10
print(a>=b)
print(a==b)

#AND & OR (Gates) Operator
f = False
t = True
print(f or t)
print(f and t)

c=10
d=20
result = (c != d)
print(result)

#Ternary Operator
age= int(input("Enter your age"))
print("You can vote" if age>=18 else "You cannot vote")

'''
#Same can be done in if loop.
if age>=18:
    print("You can vote")
else:
    print("You cannot vote")
'''
#Same can we written in 1 line of code
print("You can vote" if int(input("Enter your age")) >=18 else "You cannot vote")


