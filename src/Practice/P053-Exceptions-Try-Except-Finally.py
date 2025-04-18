# Try - Except - Finally

try:
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    result = n1/n2
except ValueError as ve:
    print("Value Error - Your input should be an integer instead of string")
except ZeroDivisionError as ve:
    print("ZeroDivision Error - Your second input cant be zero (0)")
else:
    print("Result: ",result)
finally:
    print("Finally Block")