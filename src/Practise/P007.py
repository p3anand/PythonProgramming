# Literals
#variable name (identifiers) = variable value (literals)
'''
#Decimal Literals
age = 65

#Binary Literals
binary_num = 0b1010 #10

#Octal Literal
Oct = 0o130 #88

#Hexadecimal Literal
Hexa = 0X12c
'''

#Escape Sequence
print("Hello World")
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\bWorld")

#Both the following lines will throw error coz it reads\n as new line
#dir = 'C:\Desktop\n.txt'
#dir = "C:\Desktop\n.txt"

#To correct the above lines r should be used. r -> raw data
#r concept is used in Web & API automation -> file_path = r concept
dir = r"C:\Desktop\n.txt"
print(dir)


#Single Escape Sequence Difference of single quote and double quote
a = 'Hello\'World'
b = "Hello'World"
print(a)
print(b)
