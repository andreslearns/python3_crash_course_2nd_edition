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


class Admin(Users):
    """Will attempt to create admin class """
    def __init__ (self, firstname, lastname, email, location):
        
        super().__init__ (firstname, lastname, email, location)
        self.privileges = Privileges()

            
            
class Privileges:
    """A class that will stor admin privilege"""
    
    def __init__(self, privileges = []):
        self.privileges = privileges
        
    
    def show_privileges (self):
        """ Will show the privilege """
        if self.privileges:
            for priv in self.privileges:
                print (f"- {priv.title()}")
        else:
            print ("\n- This user has no privileges!")
                

admin_user = Admin ('Andrew', 'Soltes', 'asoltes.sparc@gmail.com', 'bicol')

admin_user.describe_user()
admin_user.privileges.show_privileges()
print ("\nAdding privileges...")

admin_priv = [
   'can add post',
   'can delete post',
   'can ban users'
]

admin_user.privileges.privileges = admin_priv
admin_user.privileges.show_privileges()


    