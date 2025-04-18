# OS Modules
# Helps to work with files, paths related to OS
import os

print(os.name)  # nt - windows  posix - mac/linux
if (os.name == 'nt'):
    print("Its Windows")
else:
    print("Its either Mac or Linux")

print(os.getcwd())  # gets current working directory path
os.chdir("paste paste of the directory")  # change directory - throws error coz of no proper path mentioned
print(os.getcwd())

os.mkdir('New Directory')  # New Directory(folder) is created
os.mkdirs('parent/child/grandchild')  # Folder is created under folders

print(os.listdir('.'))  # Lists all files in directory
for file in os.listdir('.'):  # Prints all file names in list
    print(file)

os.remove('filename.txt')  # Removes file
os.rmdir('new_directory')

# Frequently used one -Joins/Adds file in folder path
full_path = os.path.join('paste_folder_path', 'filename.txt')
print(full_path)

#Checks if file exists
print(os.path.exists('file.txt'))

#Check if its a file
print(os.path.isfile('file.txt'))

#Checks if its a directory
print(os.path.isdir('file.txt'))