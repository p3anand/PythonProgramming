'''
Program to get two input from user
And calculate - max, power of num1 to num2, subtraction,
multiplication, addition & division
format output with string
'''

num1 = int(input("Enter num1\n"))
num2 = int(input("Enter num2\n"))
print("Max of two numbers =",max(num1,num2))
print(f"{num1} to {num2} = ", num1**num2)
print("Addition =",num1+num2)
print("Subtraction =",num1-num2)
print("Multiplication =",num1*num2)
print("Division =",num1/num2)

