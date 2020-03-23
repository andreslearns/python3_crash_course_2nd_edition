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

class Battery:
    """ A simple attempt to model a battery for an electric car. """
    def __init__(self,battery_size=75):
        """ Initialized the battery attributes"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print (f"This car can go about {range} miles on a full charge.")
    
    def battery_upgrade(self):
        """Will check the battery size """
        if self.battery_size == 75:
            self.battery_size == 100
            print("Upgraded the battery to 100 kwh")
        else:
            print("The battery is already upgaded")
           

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""
    
    def __init__ (self, make, model, year):
        self.battery_size = 75
        """ Initialzed attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def describe_battery(self):
        """ Print a statement describing battery size"""
        print (f"This car has a {self.battery_size}-kWh battery")
        
    def fill_gas_tank(self):
        """Electric cars dont have a gas tanks"""
        print("This car does'nt need a gas tank!")
        
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print (my_tesla.get_descriptive_name())
my_tesla.battery_size = 75
my_tesla.battery.battery_upgrade()
        
    
        

