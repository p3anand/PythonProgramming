# Recap - Unlimited arguments -> *args
# User defined Functions
def make_pizza(*toppings):
    for topping in toppings:
        print(topping, end="|")


pizza1 = make_pizza("Onions")
pizza2 = make_pizza("Tomatoes", "Mushrooms", "Peppers")
pizza3 = make_pizza("Olives", "Salami", "Basil")

# Buit-in functions
r = max(145, 678, 89, 34, 9, 0)
print(r)

#Only one unlimited argument can be used in function
#And unlimited argument should be the first element
def pizza_order(*topping, base):
    print(topping, base)

pizza4 = pizza_order("onions", "tomato", "peppers", base="thin crust")
