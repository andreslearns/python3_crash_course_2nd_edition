
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

#Will check if the item is not in the list
if user not in banned_users:
    print (f"{user.title()} you can post a response if you wish.")

#Will check if the item is in the list

user = "andrew"
if user in banned_users:
    print (f"{user.title()}, you are in the list of banned user. you cannot post comment!")

    
