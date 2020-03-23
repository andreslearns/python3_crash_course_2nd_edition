def show_messages(msg):
    for message in message_list:
        print (f"This is the message in a bottle: {message.title()}")
    

message_list = ['hi im lost', 'help me', 'i love python']
show_messages(message_list)
