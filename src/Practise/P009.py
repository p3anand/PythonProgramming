#Program to calculate the area of a circle given its radius using formula
# area = pi * r ^ 2 (Take pi as 3.14)
import math

radius = float(input("Enter the radius of circle\n"))
area = math.pi* math.pow(radius,2)
# area = 3.14 * (radius**2)
print("Area of the circle =", area)
print(f"Area of the circle = {area:.3f}")
