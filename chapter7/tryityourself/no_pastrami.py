sandwich_menus = ['ham', 'cheeze', 'chicken', 'pastrami', 'seafood', 'pastrami','beef', 'pastrami']

finished_sandwich = []

print (f"\nSorry whe're out of pastrami!\t\n")
while 'pastrami' in sandwich_menus:
    current_sandwich = sandwich_menus.remove('pastrami')
    
#    finished_sandwich.append(current_sandwich)
    
while sandwich_menus:
    current_sandwich = sandwich_menus.pop()
    print (f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwich.append (current_sandwich)
    
print ("\n\t...Finishing.....\n")
for sandwich in finished_sandwich:
    print (f"I made a {sandwich} is available!")