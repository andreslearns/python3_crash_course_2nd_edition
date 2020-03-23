def sandwich_order(bread, *toppings):
    """ Will print the persons order for the sandwiches"""
    
    print (f"\nSandwich Order:")
    print (f"\tBread - {bread}")
    
    for topping in toppings:
        print (f"\tToppings - {topping.title()}")
    

sandwich_order ('spanish bread', 'mayonnaise')
sandwich_order ('pandesal', 'mayonnaise', 'tomato', 'chilli sauce')
sandwich_order ('oridinary bread', 'chicken sauce', 'sausage')

