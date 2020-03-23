def make_tshirt(size, message = 'I love python'):
    """A function that will call the size and default value of the message """
    
    print (f"Shirt size is {size.title()} with the message {message.title()}")
    
make_tshirt('small')
make_tshirt('medium','I love programming')
make_tshirt('large')

    