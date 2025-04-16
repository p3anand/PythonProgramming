'''
TUPLES
- Tuple is a collection of Items
- represented my ()
- They are immutable - values cannot be changed
'''

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# my_tuple[3] = 9 #This will give Type error - 'tuple' object does not support item assignment

# -----------------------------
# Conversion of Tuple -> List
converted_list = list(my_tuple)  # Tuple to List conversion
print(converted_list)

# -----------------------------
# Conversion of List -> Tuple
print(converted_list)
converted_tuple = tuple(converted_list)  # List to Tuple conversion
print(converted_tuple)

# -----------------------------
# TUPLE inside another tuple

h1 = ("A", "B")
h2 = ("C", "D", "E", "F")
new_tuple = (h1, h2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[0][1])

# -----------------------------
# Search in Tuple
cities = ("Paris", "Berlin", "Munich", "Tokyo")
print("Paris" in cities)

# -----------------------------
# Concatenating two Tuple
t = (12, 34, 56)
created_tuple = t + (4,)
print(created_tuple)
