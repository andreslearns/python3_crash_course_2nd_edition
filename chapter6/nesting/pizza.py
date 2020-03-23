#store information about  a pizza being orderd
#list inside dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#summmarize the orders
print (f"You ordered a {pizza['crust']} -crust pizza with the following toppings: ")

#for loop inside the dictionary targeting the list
for topping in pizza ['toppings']:
    print (f"\ttoppings " + topping)