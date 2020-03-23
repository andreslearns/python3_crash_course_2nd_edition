filename = 'guest.txt'
name = input ("Write your name: ")

with open (filename, 'w') as file_object:
    file_object.write(name)