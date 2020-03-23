def show_messages(msg):
    for message in message_list:
        print (f"showing messages: {message.title()}")
        

def send_message(sent_msg, sent_messages):
    while message_list:
        msgs = message_list.pop()
        print (f"sending the messages: {msgs.title()}")
        sent_messages.append(msgs)
 #       print (message_list)
        
        
message_list = ['hi im lost', 'help me', 'i love python']
show_messages(message_list)

sent_messages = []
send_message(message_list[:],sent_messages)

print ("final list is: \n")
print (message_list)
print (sent_messages)

u8PboHcW23NhDA9