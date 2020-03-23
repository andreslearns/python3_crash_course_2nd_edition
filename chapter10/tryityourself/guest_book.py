filename = 'guest_list.txt'

print ("Enter quit when your finished.")

while True:
    name = input ("Write your name: ")
    if name == 'quit':
        break
    else:
        with open (filename, 'a') as file_object:
            file_object.write(name + "\n")
            print (f"Hi {name.title()}, you've been added to the guest books")
