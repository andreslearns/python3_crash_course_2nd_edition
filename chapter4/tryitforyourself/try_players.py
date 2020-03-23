players = ['charles', 'martina','michael', 'florence', 'eli']

#will start from the start of the list to 3rd item
print (players[0:3])

#will start on the 2nd item on the list to the 4th item
print (players[1:4])

#will print from the start of the list to the 4th item
print (players[:4])

#will print starting from the 3rd item on the list to the last
print (players[2:])

#will print the last 3 players on the list
print (players [-3:])

print ("Here is the first three players on my team:")

for player in players[:3]:
    print (player.title())

print ("Here is the last two players on my team")

for player in players [-2:]:
    print (player.title())
