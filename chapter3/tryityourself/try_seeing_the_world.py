#Store the locations in a list. Make sure the list is not in alphabetical order
locations = ['Taiwan', 'Japan', 'New Zealand', 'Denmark', 'Norway']

#Print your list in its original order. Don’t worry about printing the list neatly,
#just print it as a raw Python list
print(f"Here is the original order of the list\n {locations}")

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print (f"Here is the sorted list:\t") 
print (sorted(locations)) 

#Show that your list is still in its original order by printing it
print (f"Here's the original list again\n {locations}")

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print (f"Here is the sorted list again:\t")
print (sorted(locations))

#Show that your list is still in its original order by printing it again.
print (f"Here is the original list again:\t")
print (locations)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
print (f"Here to show the reverse of the list:\t")
locations.reverse()
print (locations)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
print (f"Here the reverse of reversed list:\t")
locations.reverse()
print (locations)

#use sort() to change your list so it’s stored in alphabetical order. Print the
#list to show that its order has been changed.
print (f"Here's the sort list")
locations.sort()
print (locations)

#Use sort() to change your list so it’s stored in reverse alphabetical order.
#Print the list to show that its order has changed.
print (f"Here's the sort list again")
locations.sort(reverse= True)
print (locations)

count = len(locations)
print (f"The count of locations you wanted to visit is:",count)