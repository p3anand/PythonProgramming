#Program to create sum of three numbers

num1= int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))
num3= int(input("Enter number 3: "))

def sum_of_three_numbers(n1,n2,n3):
    return n1+n2+n3

result=sum_of_three_numbers(num1,num2,num3)
print("Sum: ",result)