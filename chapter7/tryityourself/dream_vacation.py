name_prompt = "what's your name: "
place_prompt = "If you could visit one place in the world, where would it be?: "
continue_prompt = "Would you like to let someone else respond? yes/no?"

responses = {}

while True:
    #ask the user where they'd like to go.
    name = input (name_prompt)
    place = input (place_prompt)

    #store the response.
    responses[name] = place

    #ask if there's anyone else responding
    repeat = input (continue_prompt)
    if repeat != 'yes':
        break
    
    #show results of the survey
    
print ("\n----Results----")

for name, place in responses.items():
    print (f"{name.title()} would like to visit {place.title()}.")