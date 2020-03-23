sandwich_orders = ['ham', 'potato', 'chicken']

finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print (f"Currently making your {finished_sandwich.title()} Sandwich")
    finished_sandwiches.append(finished_sandwich)
    
print ("\n\t.....Finishing.....\n")   
for sandwich_orders in finished_sandwiches:
    print (f"Finished making your {sandwich_orders.title()} sandwich")
    