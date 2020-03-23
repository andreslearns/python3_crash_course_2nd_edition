guest = ['Mau', 'Ronnie', 'MC']

cant_attend = guest.pop(0)


print (f"My friend {cant_attend.title()} Mauricio cannot attend to the dinner")

new_guest = 'Cedie'

guest.append(new_guest)

print (f"So I will invite {new_guest.title()} instead in behalf of {cant_attend.title()}")

print (f"So all my confirmed guest was {guest[0].title()}")
print (f"So all my confirmed guest was {guest[1].title()}")
print (f"So all my confirmed guest was {guest[2].title()}")