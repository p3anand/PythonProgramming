#Factorial Series
#Factorial n = 5
# 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24


num=int(input("Enter the number\n"))

fact=1
if num==0 or num==1:
    print(fact)
else:
    for i in range(1,num+1,1):
        fact=fact*i
print (fact)

#USING math function
# from math import factorial
# num=int(input("Enter the number\n"))
# print(f"Factorial of {num}: ",factorial(num))