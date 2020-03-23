class Users:
    """ Will attempt to create a class users """
    def __init__(self, firstname, lastname, email, location):
        
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.login_attempts = 1
        
    def describe_user(self):
        """ will describe the user"""
        print (f"\nUser Information summary:")
        
        print (f"\tFirst name\t: {self.firstname.title()}")
        print (f"\tLast name\t: {self.lastname.title()}")
        print (f"\temail\t\t: {self.email}")
        print (f"\tlocation\t: {self.location.title()}")
        
    def greet_user(self):
        """ will greet the user"""
        print (f"\nThank you for participating {self.firstname.title()} mabuhay!")
    
    def increment_login_attempts(self, login_attempts):
        """ Will increment the login attempts """
        self.login_attempts += login_attempts
        
    def reset_login_attempts(self):
        """ Will reset the login attempts"""
        self.login_attempts = 0
        
        
        
user = Users('andrew', 'soltes', 'soltesandrew@gmail.com', 'jose panganiban')
user.describe_user()
user.greet_user()

user.increment_login_attempts(6)
print ("login attempt: " + str(user.login_attempts))
user.reset_login_attempts()
print ("reset login attempt:" + str (user.login_attempts))

user = Users('ayie', 'ebora', 'ayiebora@gmail.com', 'marikina')
user.describe_user()
user.greet_user()


user.login_attempts = 3
print ("login attempt: " + str(user.login_attempts))
user.reset_login_attempts()
print ("reset login attempt:" + str (user.login_attempts))