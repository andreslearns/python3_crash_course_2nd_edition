#Print the message The first three items in the list are:. Then use a slice to
#print the first three items from that program’s list.
nocs = ['rogem', 'ener', 'jerome', 'andrew']
for noc in nocs[:]:

    print ("The last remaining nocs in sparc except me is: ",noc)

nocs.append('rollie')
nocs.append('aljhay')

#Print the message Three items from the middle of the list are:. Use a slice to
#print three items from the middle of the list.

for engineer in nocs[1:4]:
    print ("the list of engineers in the middle is:",engineer)

#Print the message The last three items in the list are:. Use a slice to print the
#last three items in the list.

for network in nocs[-3:]:
    print (f"The last three remaining nocs in sparc is: {network}")


my_pizzas = ['pepperonni', 'macaronni', 'hawaiian', 'pineapple pizza']
my_friend_pizza = my_pizzas[:]

my_pizzas.append('cheeze pizza')
my_friend_pizza.append('kanto pizza')

print (f"The list of my pizza is: {my_pizzas}")
print (f"The list of my friend pizza is {my_friend_pizza}")

#using the for loop to display the pizza

for pizza in my_pizzas:
    print ("Here's the list of my pizza:",pizza)
print (f"I added on my pizza is: {my_pizzas[-1].upper()}")

for friend_pizza in my_friend_pizza:
    print ("Here's the list of my friends pizza:", friend_pizza)
print (f"I added to my friend pizza is {my_friend_pizza[-1].upper()}")



