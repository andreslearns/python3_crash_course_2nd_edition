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
    
        
        
my_restaurant = Restaurant('Water side', 'Filipino')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.number_served = 430
print ("Number served:" + str(my_restaurant.number_served))



your_restaurant = Restaurant('samgyupsalamat', 'korean')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

your_restaurant.number_served = 560
print ("Number served:" + str (your_restaurant.number_served))