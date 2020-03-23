class Restaurant:
    """ Will make a restaurant """
    
    def __init__(self, name, cuisine):
        """ Initialized name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
        
    
    def describe_restaurant(self):
        """ will describe the restaurant """
        print (f"\nThe restaurant's name is {self.name.title()} and a {self.cuisine.title()} cuisine")
        
    
    def open_restaurant(self):
        """ will tell the restaurant is open"""
        print (f"The {self.name.title()} Restaurant is now Open")
        
    
    def set_number_served(self, number_served):
        """ that let you set the number and the print the value again"""
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        """Will increment the number served """
        self.number_served += additional_served
        

class IceCreamStand(Restaurant):
    """Will show the Icream stand """
    
    def __init__ (self, name, cuisine_type='ice cream'):
        super().__init__ (name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display icecream flavors"""
        print ("\nThis is the flavors available: ")

        for flavor in self.flavors:
            print (f"- {flavor.title()}")
            
            
big_one = IceCreamStand('The big one')
big_one.flavors = ['vanilla', 'chocolate', 'black berry']

big_one.describe_restaurant()
big_one.show_flavors()
        
         


