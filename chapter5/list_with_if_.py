#Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print (f"adding {requested_topping}.")
    
print ("\nfinished making your pizza!")

#Checking That a List Is Not Empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print (f"adding {requested_topping}.")
    print ("\nfinished making your pizza!")
else:
    print ("are you sure you wanted a plain pizza?")
        