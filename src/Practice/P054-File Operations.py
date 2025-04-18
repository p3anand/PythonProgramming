#File Operations

file = open('ExampleFile.txt','r') #FileNotFoundError if file is not available in directory
print(file.read())

#the following is same as file = open('ExampleFile.txt','w')
with open('ExampleFile.txt','a') as file:
    file.write("Context 1 ")

file = open('ExampleFile.txt','r') #FileNotFoundError if file is not available in directory
print(file.read())

with open("ExampleFile.txt", "r") as file:
    lines=file.readlines()
    for line in lines:
        print(line,end = '|')

print("-------------------------------------------")






