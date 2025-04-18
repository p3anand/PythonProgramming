# File Operations with Exception Handling
# When file is in different package

import os
try:
    full_path = os.getcwd()
    print(full_path)
    # file = open('ExampleFile.txt','r')
    file = open(full_path + 'ExampleFile.txt', 'r')
    print(file.read())

except FileNotFoundError as fnfe: #If you dont know any type of Exceptions then type Exception
    print("File is not available, Please verify file availability")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)