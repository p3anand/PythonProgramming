#Exception Handling

#Program with errors
'''
print(" --- Start of the program --- ")
a = int(input("Ent the num1: ")) # abc -> ValueError: invalid literal for int()
b = int(input("Ent the num2: ")) # abc ->  ValueError
#Type error is not possible coz of int conversion
c = a / b # ZeroDivisionError: division by zero - Lab149.py", line 3
print("Result Div is ", c)
print(" --- End of the program ---")

'''
#-------------------------------
#Program with Exception Handling

print(" --- Start of the program --- ")
try:
    a = int(input("Ent the num1")) # ValueError: invalid literal for int()
    b = int(input("Ent the num2")) # Lab150.py", line 4, ValueError
    c = a / b # ZeroDivisionError: division by zero - Lab149.py", line 3
    print("Result Div is ", c)

except Exception as e: # as - alias , Exception is a Class
    print(e)
    print("Please check your inputs, it should not be a string or zero")
print(" --- End of the program ---")

