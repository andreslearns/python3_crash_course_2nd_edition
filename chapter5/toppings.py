requested_toppings = ['mushrooms', 'onions', 'pineapple']

if requested_toppings != 'anchovies':
    print ("Hold the Anchovies")
else:
    print ("Fuck!")
    
    
#will check if the item is existing in the list
validity = 'mushrooms' in requested_toppings
validity1 = 'pepperoni' in requested_toppings
print (validity)
print (validity1)

# testing multiple conditions
# if statements

if 'mushrooms' in requested_toppings:
    print ("adding mushrooms.")
if 'onions' in requested_toppings:
    print ("adding onions.")
if 'pepperoni' in requested_toppings:
    print ("adding pepperoni")

print ("\nFinished making your pizza")
