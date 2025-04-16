# List
# It's a collection of items

my_list = [1, 2, 3]

print(my_list)
print(len(my_list))  # length of list

print(my_list[0])
# print(my_list[10])  # List index out of range - exception

# ----------------------------------------

# INDEXING - updating value of current list
my_list[0] = "A"
my_list[1] = "B"
my_list[2] = "C"
print("Element at index 0 is:", my_list[0])
print("Element at index 1 is:", my_list[1])
print("Element at index 2 is:", my_list[2])

print(my_list)
for element in my_list:
    print(element)

# ----------------------------------------
# List - Adding new items

my_list.append(4)
print(my_list)

my_list.extend([5, 6, 7, "G"])
print(my_list)

#-----------------------------------------
#List - Adding items in list at specific position
print(my_list)
my_list.insert(3,99)
print(my_list)

#-----------------------------------------
# Index -1
print(my_list)
my_list.insert(-1,88)
print(my_list)

#-----------------------------------------
# Removing list items
print(my_list)
my_list.remove("G")
print(my_list)

#-----------------------------------------
# Creating copy of list items
print(my_list)
my_list_copy = my_list.copy()
print(my_list_copy)

#-----------------------------------------
# Clearing list items
my_list.clear()
print(my_list)
print(my_list_copy)

#-----------------------------------------
# Sorting list items
#Needs str values to be removed
my_list_copy.remove("A")
my_list_copy.remove("B")
my_list_copy.remove("C")
print(my_list_copy)
my_list_copy.sort()
print(my_list_copy)
my_list_copy.reverse()
print(my_list_copy)

#------------------------------------------
#Pop()
squares = [1,4,9,16,25]
print(squares.pop())
print(squares)