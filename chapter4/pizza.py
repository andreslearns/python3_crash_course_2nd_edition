#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
#pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas = ['macaronni','peperroni','hawaiian']

for pizza in pizzas:
    print (f"My top favorite pizzas flavor is: {pizza.title()}")

count = len(pizzas)
print (f"\nThat is only {count} flavors of pizza's that I like.")