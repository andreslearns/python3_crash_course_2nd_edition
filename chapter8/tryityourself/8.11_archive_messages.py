def show_messages(msg):
    for message in message_list:
        print (f"This is the message in a bottle: {message.title()}")
        

def send_message(sent_msg):
    while message_list:
        msgs = message_list.pop()
        print (f"The messages is: {msgs.title()}")
        sent_messages.append(msgs)
#        print (message_list)
        
        
message_list = ['hi im lost', 'help me', 'i love python']
sent_messages = []
show_messages(message_list)

send_message(sent_messages)
send_message(sent_messages[:], msg)

print("\nFinal lists:")
print (msg)
print(sent_msg)
