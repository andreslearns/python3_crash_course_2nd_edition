guest = ['Mau', 'Ronnie', 'MC']

cant_attend = guest.pop(0)


print (f"My friend {cant_attend.title()} Mauricio cannot attend to the dinner")

new_guest = 'Cedie'

guest.append(new_guest)

print (f"So I will invite {new_guest.title()} instead in behalf of {cant_attend.title()}")

print (f"So all my confirmed guest was {guest[0].title()}")
print (f"So all my confirmed guest was {guest[1].title()}")
print (f"So all my confirmed guest was {guest[2].title()}\n\n")

# 3- 6 more guest

print (f"Hi all {guest} I just found out that I have a bigger dining table so I will add someone on the list")

guest.insert(0 , 'Diane')
guest.insert(2 , 'Ayie')
guest.insert(1 , 'Mark')

print (f"So I will send additional invitation for them but first I will invite {guest[0].title()}")
print (f"I will also send an invitation to {guest[3].title()} which is the love of my life! <3")
print (f"And my last guest would be {guest[1]}\n\n")

print ('*' * 110)
print (f"Sadly my Dining table wont arrive so soon so I need to remove some of my guest and accomodate only two")
print ('*' * 110)


guest0 = 'Ronnie'
guest.remove(guest0)

guest1 = 'Diane'
guest.remove(guest1)


print (f"Sorry to inform you {guest0.upper()} Canteros that I can't invite you to dinner")
print (f"Sorry to inform you {guest1.upper()} You are not invited")
print (f"Sorry to inform you {guest.pop(0).upper()} that I can't invite you to dinner")
print (f"Sorry to inform you {guest.pop(1).upper()} that I can't invite you to dinner\n\n")



print (f"I'm Happy to invite {guest[0]} to dinner so I can propose")
print (f"I'm Happy to invite {guest[1]} to dinner so we can play games all night\n")

# will delete the list

del guest[0]
del guest[0]


print (f"See my empty list {guest}")


