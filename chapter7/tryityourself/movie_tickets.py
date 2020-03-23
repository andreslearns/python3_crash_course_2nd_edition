prompt = "How old are you? "
prompt += "Enter 'quit' if you are done!"

while True:
    age = input (prompt)
    
    if age == 'quit':
        break
    age = int(age)
    
    if age < 3:
        print ("You are free!")
    elif age < 13:
        print ("Your ticket is $10")
    else:
        print ("Your ticket is $15")
        

    
        