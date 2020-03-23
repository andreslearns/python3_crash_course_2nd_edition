#5-8. Hello Admin:
usernames = ['root', 'admin','noc', 'asoltes']

for username in usernames:
    if username == 'admin':
        print (f"Hello master {username.upper()} have a nice day!")
    else:
        print (f"Hello ordinary guy {username.upper()} whatever!")
        


######################################################################
#5-9. No Users:
print ('*' * 70 )

users = []
 
if users:
    for user in users:
        print (f"Hello user {user.title()}")
else:
    print (f"You have an empty user!!")

print ('*' * 70 )

######################################################################
current_users = ['root','admin', 'noc', 'asoltes', 'enerjr']
new_users = ['asoltes', 'Admin', 'newguy', 'networkguy']

lowercase_user = current_users[:]
#lower case comparison or insensituive comparison
lowercase_user = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in lowercase_user:
        print (f"Sorry {new_user} username exist!")
    else:
        print (f"Thank you, {new_user} username available")
        
print ('*' * 70 )

numbers = ['1','2','3','4', '5', '6', '7', '8', '9']

for number in numbers:
    if number == '1':
        rank = "1st"
    elif number == '2':
        rank = "2nd"
    elif number == '3':
        rank = '3rd'
    elif number == '4':
        rank = '4th'
    elif number == '5':
        rank = '5th'
    elif number == '6':
        rank = '6th'
    elif number == '7':
        rank = '7th'
    elif number == '8':
        rank = '8th'
    elif number == '9':
        rank = '9th'
    print (f"\nThe ranking will be {rank}!")
        
        
