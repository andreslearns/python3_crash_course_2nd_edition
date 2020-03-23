class Restaurant:
    
    """Simple class to demonstrate restaurant"""
    def __init__(self, name, cuisine_type):
        
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 25
        
    def describe_restaurant(self):
        """ will describe the restaurant name and cuisine type """
        print (f"\n{self.name.title()} with cuisine {self.cuisine_type.title()}.")
        
    def open_restaurant(self):
        """Will indicate that a restaurant is open"""
        print (f"{self.name.title()} is now open and serving {self.number_served} customers")
        
   
    def set_number_served(self, set_served):
        """ that let you set the number and the print the value again"""
        self.number_served = set_served
        return set_served
        
    def increment_number_served(self, number_served):
        """Will increment the number served """
        self.number_served += number_served  
        
        
        
    
    
        
    
resto1 = Restaurant('Jollibee', 'filipino')
resto2 = Restaurant('Samgyupsalamat', 'korean')
resto3 = Restaurant('ramenagi', 'japanese')
    

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))