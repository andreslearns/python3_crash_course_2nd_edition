class Users:
    """ Will attempt to create a class users """
    def __init__(self, firstname, lastname):
        
        self.firstname = firstname
        self.lastname = lastname
        
    def describe_user(self):
        """ will describe the user"""
        print (f"\nUser Information summary:")
        
        print (f"\tFirst name\t: {self.firstname.title()}")
        print (f"\tLast name\t: {self.lastname.title()}")
        
    def greet_user(self):
        """ will greet the user"""
        print (f"\nThank you for participating {self.firstname.title()} mabuhay!")
        
        
user = Users('andrew', 'soltes')
user.describe_user()
user.greet_user()

user = Users('ayie', 'ebora')
user.describe_user()
user.greet_user()