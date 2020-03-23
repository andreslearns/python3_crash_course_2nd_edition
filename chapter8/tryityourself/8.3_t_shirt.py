def make_tshirt(size, message):
    print (f"T shirt size will be {size} with the message {message.title()}")
    
make_tshirt('25','God is love') #Positional arguments
make_tshirt(size = '32', message = 'Punk not dead!') #keyword arguments