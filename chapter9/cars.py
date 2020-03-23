class Car:
    """ A simple attempt to represent a car """
    
    def __init__ (self, make, model, year):
        """Inialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement that will show car mileage"""
        print (f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """ set the odometer reader to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odemeter!")
            
            
    def increment_odometer(self, miles):
        """ add the given amount to the odometer reading """
        self.odometer_reading += miles
        
        
my_new_car = Car('audi', 'a4', 2019)
print (my_new_car.get_descriptive_name())
#Modifying an Attribute’s Value Directly
#my_new_car.edometer = 23
#my_new_car.odometer_reading()

#Modifying an Attribute’s Value Through a Method
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print (my_used_car.get_descriptive_name())

my_used_car.update_odometer (23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

