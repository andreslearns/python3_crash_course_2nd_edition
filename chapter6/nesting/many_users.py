users = {
    'aenstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last': 'curie',
        'location': 'paris',
    },
}


for username, user_info in users.items():
    print (f"\nUsername: {username}")
    fullname = f'{user_info}'
    
    print (f"Personal information\n\tFullname: {user_info['first'].title()} {user_info['last'].title()}")
    print (f"\tLocation: {user_info['location'].title()}")
    print ('-' * 40)