class Restaurant:
    """ Will make a restaurant """
    
    def __init__(self, name, cuisine):
        """ Initialized name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
        
    
    def describe_restaurant(self):
        """ will describe the restaurant """
        print (f"\nThe restaurant's name is {self.name.title()} and a {self.cuisine.title()} cuisine")
        
    
    def open_restaurant(self):
        """ will tell the restaurant is open"""
        print (f"The {self.name.title()} Restaurant is now Open")
        
my_restaurant = Restaurant('Water side', 'Filipino')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('samgyupsalamat', 'korean')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()