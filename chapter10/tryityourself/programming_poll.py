filename = 'poll.txt'

responses = []
while True:
    response = input("What can you say about Python Programming? ")
    responses.append(response)
    
    continue_poll = input("Would you like other's to respond? yes/no")
    if continue_poll != 'yes':
        break
    
with open (filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
        