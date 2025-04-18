#File Operations with Exception Handling

try:
    file = open('TextFile.txt', 'r')  # FileNotFoundError if file is not available in directory
    print(file.read())

except FileNotFoundError as fnfe: #If you dont know any type of Exceptions then type Exception
    print("File is not available, Please verify file availability")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)