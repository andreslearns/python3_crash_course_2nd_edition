
print ("Hi welcome to Andrew's diner! How many companions with you? ")
prompt = input ("please enter the number: ")

prompt = int(prompt)

if prompt >= 8:
    print (f"Sorry you have to wait no {prompt} seaters available!")
else:
    print (f"{prompt} seats available, Enjoy your dinner!")
