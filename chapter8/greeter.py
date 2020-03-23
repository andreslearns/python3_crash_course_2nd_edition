def greet_user(): #no need of information
    """Display a simple greeting""" # docstring
    print ("Hello!") # the code that will run
    
greet_user() # function call


#A simple function that passes information to username 
def greet_user(username):
    """Display a simple greeting"""
    print (f"Hello, {username.title()}!")

greet_user('jesse')