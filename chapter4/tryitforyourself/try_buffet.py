buffet_foods = ('adobo','longganisa', 'mechado', 'menudo', 'afritada')

for buffet in buffet_foods:
    print (f"Here's the list of the menu: {buffet.title()}")

#buffet_foods[0] = 356 # WILL REJECT THIs

modified_foods = buffet_foods[:]
print (modified_foods)

modified_foods = ('lechon', 'paksiw')


for mod in modified_foods:
    print (f"Here is the list of modified foods: {mod.upper()}")