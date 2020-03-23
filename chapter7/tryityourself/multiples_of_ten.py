print ("Enter a number and I will tell you if it's multiple of 10's!")
prompt = input("enter a number: ")
prompt = int(prompt)

if prompt % 10 == 0:
    print (f"{prompt} multiples of 10!")
else:
    print (f"{prompt} is not multiple of 10!")