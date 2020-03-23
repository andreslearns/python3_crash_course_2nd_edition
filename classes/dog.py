class Dog():
    """ Simple class to create a instance of a dog"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print (f"{self.name} is now sitting.")

    def rollover(self):
        """Simulate a dog rolling over in response to a command"""
        print (f"{self.name} rolled over!")
        

my_dog = Dog('tiny', 3)

print (f"My dog's name is {my_dog.name}.")
print (f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.rollover()

print ("\n")

your_dog = Dog('puru', 2)
print (f"My dog's name is {your_dog.name}.")
print (f"My dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.rollover()
