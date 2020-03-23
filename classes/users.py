class Users:
    """Simulate a user profile"""
    def __init__(self,first_name, last_name, age, sex):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        
    def describe_user(self):
        """Will describe the user """
        print(f"\t\nPersonal Information\n")
        print (f" Firstname\t:{self.first_name.title()}")
        print (f" Lastname\t:{self.last_name.title()}")
        print (f" Age\t\t:{self.age}")
        print (f" Sex\t\t:{self.sex.title()}")
    
        
    def greet_user(self):
        """Will greet the user"""
        print (f"\nGreetings from the hello world! {self.first_name.title()}")


user = Users('andrew', 'soltes', 27 , 'male')
user.describe_user()
user.greet_user()


user = Users('ayie', 'ebora', 26, 'female')
user.describe_user()
user.greet_user()