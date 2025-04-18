# SET
# Collection of Unique items

t = ("a", "b", "c", "a")
print(t)
print(set(t))

#---------------------------
#Union of Set
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}
my_set12 = set1.union(set2)
print(my_set12)

#---------------------------
#Intersection of Set
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
my_set34 = set3.intersection(set4)
print(my_set34)

#---------------------------
#Difference of Set
my_set_1 = set1.difference(set2) #removes duplicates of set2 in set1
my_set_2 = set2.difference(set1) #removes duplicates of set1 in set2
print(my_set_1)
print(my_set_2)

#----------------------------
#Subset
set5 = {1, 2,3, 4,5}
set6 = {2,3,8}
subset=set2.issubset(set1) #tests if every element of set1 is present in set 2
print(subset)

#----------------------------
set10 = set(["abc", "cde", "abc."])
print(len(set10))

for i in set10:
    print(i)

set10.add("Test")
set10.add("Test")
print(set10)
