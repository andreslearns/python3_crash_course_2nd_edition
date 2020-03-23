motorcycles = ['honda', 'yamaha', 'suzuki']

print (motorcycles)

#will remove the [0 index in the list which is the honda]
motorcycles[0] = 'ducati'
print (motorcycles)

motorcycles.append('ducati')
print (motorcycles)

#will append the value to the empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print (motorcycles)

# will add the value to the first of the list
motorcycles.insert(0, 'Karag')
print (motorcycles)

#will delete the inserted value at the 0 index
del motorcycles[0]
print (motorcycles)

#using pop()

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

popped_motorcycles = motorcycles.pop()
print (motorcycles)

print (popped_motorcycles)

first_owned = motorcycles.pop()
print (f"The first motorcycle I owned was a {first_owned.title()}.")

last_owned = motorcycles.pop(0)
print (f"The last motorcycle I owned was a {last_owned.title()}.")

#removing an item vy value

motorcycles = ['Honda', 'Yamaha', 'Suzuki', 'Ducati']
print (motorcycles)

#motorcycles.remove('Ducati')
#print (motorcycles)

too_expensive = 'Ducati'
motorcycles.remove(too_expensive)
print (motorcycles)
print (f"\nA {too_expensive.title()} is too expensive for me")