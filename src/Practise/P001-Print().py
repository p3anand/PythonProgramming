# Learning print function:
# def print(self, *args, sep=' ', end='\n', file=None):  # known special case of print

print("Hello", "This", "is", "a", "trial", 123, True, 78.9)

# sep
print("Hello", "This", "is", "a", "trial", 123, True, 78.9, sep='-')
print("Hello", "This", "is", "a", "trial", 123, True, 78.9, sep='|')

# end="-"
print("Hello", end="=")
print("There")

# Program to find the biggest number between integers using max function

print(max(35, 100))

print(max(35, 100, 300, 400))

print(max(35, -1, -2, 400, 78.90, 45.90))

