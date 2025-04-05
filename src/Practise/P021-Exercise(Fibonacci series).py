#Fibonaci Series
#Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13


num=int(input("Enter the number\n"))
a = 0
b = 1
for i in range(0,num+1):
    print(a, end = ' ')
    next_num = a + b
    a = b
    b = next_num
