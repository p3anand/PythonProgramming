#Passing list as function parameter
my_shopping_list = ["milk","bread","butter"]
print(my_shopping_list[1])
print(len(my_shopping_list))

def add_to_list(my_shopping_list):
    #my_shopping_list.append ("jam")
    new_item = input("Enter the items to be added to list: \n")
    #my_shopping_list.append(new_item)
    #my_shopping_list.remove(new_item)
    my_shopping_list.insert(1, new_item)
    return my_shopping_list

A = add_to_list(my_shopping_list)
print(A)