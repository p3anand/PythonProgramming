'''
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
'''

l1 = float(input("Enter length of  side 1: "))
l2 = float(input("Enter length of  side 2: "))
l3 = float(input("Enter length of  side 3: "))

if l1 == l2 == l3:
    print("It's a Equilateral triangle")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("It's a Isosceles triangle")
else:
    print("It's a Scalene triangle")
