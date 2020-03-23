responses = {}

#set a flag to indicatte that polling is active.
polling_active =True

while polling_active:
    #promts for the persons name and response:
    name = input ("\nWhat's your name?: ")
    response = input ("Which mountain would you like to climb someday?")

    #store the response in the dict
    responses[name] = response
    
    #findout if anyone else is going to take the poll
    repeat = input ("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
        
#polling is complete. show the results.
print ("\n--- Poll results --- ")

for name, response in responses.items():
    print (f"{name} would like to climb {response}")

    